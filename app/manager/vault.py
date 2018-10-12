import os
import hvac
from hvac.exceptions import InvalidPath
from django.conf import settings

class Vault():
    
    def __init__(self, mount_point=os.environ.get('VAULT_MOUNT_POINT', 'pwdmng/')):
        path_prefix = self._path_prefix = mount_point
        client = self._client = hvac.Client(url=settings.VAULT_HOST, token=settings.VAULT_TOKEN)
        assert client.is_authenticated() # => True
        
        engines = client.list_secret_backends()
        if engines.get(path_prefix) == None:
            client.enable_secret_backend('kv', mount_point=path_prefix, options={'version': '1'})
        client.kv.default_kv_version = "1"

    @property
    def client(self):
        return self._client
    
    def delete(self, path):
        self._client.kv.delete_secret(mount_point=self._path_prefix, path=path)

    def write(self, path, **kargs):
        self._client.kv.v1.create_or_update_secret(mount_point=self._path_prefix, path=path, secret=kargs)
        #self.client.write(self._path_prefix + path, **kargs)
        
    def read(self, path):
        data = None
        try:
            data = self._client.kv.read_secret(mount_point=self._path_prefix, path=path)
        except InvalidPath:
            pass
        
        return data

    def wrap(self, data):
        response = self._client.adapter.post('/v1/sys/wrapping/wrap', json=data, headers={'X-Vault-Wrap-TTL': '30m'})
        return response.json()

    def unwrap(self, token):
        response = self._client.adapter.post('/v1/sys/wrapping/unwrap', json={'token': token})
        return response.json()