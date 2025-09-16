from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=100)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    CustomUser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    saving_goal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=10, default='USD')
    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.CustomUser.username}'s Profile"
    
class PieChart(models.Model):
    label = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.label}, {self.amount}"