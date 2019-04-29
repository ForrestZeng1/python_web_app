from django.db import models

# Create your models here.


class user(models.Model):
    genders = [('male', 'Male'), ('female', 'Female')]
    yeename = models.CharField(max_length=255)
    yeepassword = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=genders)

    def __str__(self):
        return self.yeename


class loginCredential(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        show_password = ''
        for each in self.password:
            show_password = show_password + '*'
        return 'Username: ' + self.username + ' | Password: ' + show_password
