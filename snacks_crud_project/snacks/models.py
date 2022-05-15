from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

class Snack  (models.Model):
    title = models.CharField(max_length=64)
    purchaser =models.ForeignKey(get_user_model() ,on_delete=models.CASCADE)
    description =models.CharField(max_length=255)



    def __str__(self):
        return self.title
        

