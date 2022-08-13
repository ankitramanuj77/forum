from django.db import models

# Create your models here.
class Signup(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    
class userform(models.Model):
    title = models.CharField(max_length=100)
    option = models.CharField(max_length=100)
    select_file = models.FileField(upload_to="user_uploaded")
    dics = models.TextField()
    
    # def __str__(self):
    #     return self.fname
    