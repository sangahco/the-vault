from django.db import models
from django.contrib.auth.models import User

class Secret(models.Model):
    GENERAL='GENERAL'
    DBINFO='DB'
    SERVERINFO='SERVER'
    CATEGORIES = (('DB', 'DB'), ('SERVER', 'Server'), ('GENERAL', 'General'))
    
    label = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    project = models.CharField(max_length=200, null=True, blank=True)
    config = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True, choices=CATEGORIES, default=GENERAL)
    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
