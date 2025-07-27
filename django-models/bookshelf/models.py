# from django.db import models

# # Create your models here.
# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     publication_year = models.IntegerField(default=2000)

#     def __str__(self):
#         return self.title



from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomeUserManager

# Create your models here.
class CustomUser(AbstractUser): #Addition to Django default 
    date_of_birth = models.DateField(null = True, blank = True)
    profile_photo = models.ImageField(upload_to= "profile_photo/", null = True, blank = True)


    def __str__(self):
        return self.username
    


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=2000)

    def __str__(self):
        return self.title



