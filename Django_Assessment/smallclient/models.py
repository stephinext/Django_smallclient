from typing_extensions import Required
from django.db import models
import datetime


# Create your models here.
class SmallClient(models.Model):
    """Instructions for SmallClient model"""
    
    name = models.CharField(max_length = 250, blank=False)
    website = models.CharField(max_length=250)
    point_of_contact = models.EmailField(max_length=250,unique=True, blank=False)
    profile_pic  = models.ImageField(upload_to ='uploads/%Y/%m/%d/')
    
    class Goals(models.TextChoices):
        CPA = "CPA", "CPA"
        IMPRESSIONS = "Impressions", "Impressions"
        DOWNLOADS = "Downloads", "Downloads"
        INSTALLS = "Installs", "Installs"
        PURCHASE = "Purchase", "Purchase"

    goal_choices= models.CharField(
        max_length=50,
        choices=Goals.choices,
        default=Goals.CPA,
        blank = False
    )

    due_date = models.DateField(blank=False)
    date_joined =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def check_due(self):
        if self.due_date > datetime.date.today():
            return False
        else:
            return True

