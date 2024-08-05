from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="uploads/%Y/%m", null=True)
    company = models.CharField(max_length=255, null=True)


class ItemBase(models.Model):
    class Meta:
        abstract = True

    Created_Date = models.DateTimeField(auto_now_add=True, null=True)
    Updated_Date = models.DateTimeField(auto_now=True, null=True)


class CLIENT(ItemBase):
    ClientIdSubId = models.CharField(
        max_length=100, null=False, unique=True, db_index=True, primary_key=True
    )
    ClientSortName = models.CharField(max_length=255, null=False)

    ClientStatus = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.ClientIdSubId


class STAFF(ItemBase):
    StaffId = models.CharField(
        max_length=100, null=False, unique=True, db_index=True, primary_key=True
    )
    StaffName = models.CharField(max_length=255, null=False)
    StaffStatus = models.CharField(max_length=20, null=True)
    StaffEmail = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.StaffId


class CLIENTCRS(ItemBase):
    class Meta:
        unique_together = ("ClientIdSubId", "StaffId", "FirmClientStaffAssignmentName")

    ClientIdSubId = models.ForeignKey(CLIENT, on_delete=models.CASCADE)
    StaffId = models.ForeignKey(STAFF, on_delete=models.CASCADE)
    FirmClientStaffAssignmentName = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.ClientIdSubId} - {self.StaffId} ({self.FirmClientStaffAssignmentName})"
