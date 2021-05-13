from django.db import models

# Create your models here.


class Client(models.Model):
    fName = models.CharField(max_length=199)
    lName = models.CharField(max_length=199)
    email = models.EmailField()
    phone = models.CharField(max_length=199)
    company = models.CharField(max_length=199)
    requirements = models.CharField(max_length=199)
    message = models.TextField()

    def __str__(self):
        return "{}||{}||{}||{}".format(self.fName, self.email, self.phone, self.message)


class DropYourEmail(models.Model):
    droppedEmail = models.EmailField()

    def __str__(self):
        return "{}".format(self.droppedEmail)