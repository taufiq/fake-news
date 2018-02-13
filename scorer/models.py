from django.db import models
from newspaper import Article
#import scraper
import csv
from pathlib import Path
import os
# Create your models here.


class User(models.Model):
    username = models.CharField(
        max_length=20, help_text="Username of User", primary_key=True)

    def __str__(self):
        return self.username


class Paper(models.Model):
    url = models.TextField(help_text="Url of the Article", primary_key=True)
    title = models.TextField(help_text="Title of Article", default="NULL")
    body = models.TextField(help_text="Body of Article", default="NULL")
    stance = models.CharField(
        max_length=20, help_text="Stance of Title in relation to Body", default="NULL")
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'URL: ' + self.url + 'Stance:' + self.stance


class PaperUser(models.Model):
    url = models.TextField(default="NULL")
    # Person who first invoked the article
    referrer = models.CharField(max_length=20, default="NULL")
    # Person who requested such an article
    referree = models.CharField(max_length=20, default="NULL")
