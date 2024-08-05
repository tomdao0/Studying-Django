from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # avatar = models.ImageField(upload_to="uploads/%Y/%m")
    company = models.CharField(max_length=255, null=True)


class CLIENT(models.Model):
    ClientSortName = models.CharField(max_length=255, null=False)
    ClientIdSubId = models.CharField(
        max_length=100, null=False, unique=True, db_index=True, primary_key=True
    )
    ClientStatus = models.CharField(max_length=20, null=True)
    Created_Date = models.DateTimeField(auto_now_add=True)
    Updated_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ClientIdSubId


class STAFF(models.Model):
    StaffId = models.CharField(
        max_length=100, null=False, unique=True, db_index=True, primary_key=True
    )
    StaffName = models.CharField(max_length=255, null=False)
    StaffStatus = models.CharField(max_length=20, null=True)
    StaffEmail = models.CharField(max_length=200, null=True)
    Created_Date = models.DateTimeField(auto_now_add=True)
    Updated_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.StaffId


class CLIENTCRS(models.Model):
    ClientIdSubId = models.ForeignKey(CLIENT, on_delete=models.CASCADE)
    StaffId = models.ForeignKey(STAFF, on_delete=models.CASCADE)
    FirmClientStaffAssignmentName = models.CharField(max_length=100, null=True)
