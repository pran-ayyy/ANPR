from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

# class User(AbstractUser):
#     fname = models.CharField(max_length=200, null=True)
#     lname = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=False)
#     loc = models.CharField(max_length=50, null=True)
#     mobile = models.CharField(max_length=15)
#     desg = models.CharField(max_length=20)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     user_permissions = ['related_name']
#     groups = ['onduty_user']
#     def __str__(self) -> str:
#         return self.name


class Vehicle(models.Model):
    plate = models.CharField(max_length=15)
    type = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.plate


class Log(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    onduty = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='onduty_user', null=True)
    entry = models.DateTimeField(auto_now=True, blank=False)
    exit = models.DateTimeField(blank=True)
    loc = models.CharField(max_length=40, blank=True)

    # def __str__(self) -> str:
    #     return self.vehicle.plate +" "+ self.entry +" "+ self.exit

    class Meta:
        ordering = ('-exit', '-entry')

    def update_exit_time(self):
        self.exit = models.DateTimeField(auto_now=True)


class Image(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')
    vehicle = models.OneToOneField(Vehicle, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name
