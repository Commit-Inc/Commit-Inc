from django.db import models

# Create your models here.


class Client(models.Model):
    fName = models.CharField(max_length=34)
    lName = models.CharField(max_length=35)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    company = models.CharField(max_length=50)
    requirements = models.CharField(max_length=199)
    message = models.TextField()

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.fName, self.email, self.phone, self.message, self.requirements)


class DropYourEmail(models.Model):
    droppedEmail = models.EmailField()

    def __str__(self):
        return "{}".format(self.droppedEmail)