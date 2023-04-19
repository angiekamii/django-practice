from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)

    class Meta:
        db_table = "Student"

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Employee(models.Model):
    name = models.CharField(max_length=50)
    Position = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    Age = models.IntegerField()
    Start_date = models.DateField()
    Salary = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.Position


class venue(models.Model):
    VenueName = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    ZipPostCode = models.IntegerField()
    ContactPhone = models.IntegerField()
    WebAddress = models.CharField(max_length=50)
    EmailAddress = models.EmailField()

    def __str__(self):
        return self.VenueName


class post(models.Model):
    Author = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField()
    PublishedDate = models.DateTimeField()
