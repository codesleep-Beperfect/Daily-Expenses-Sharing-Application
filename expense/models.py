from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Using custom model inherited Base Model
class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return self.username
    
class Expense(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"user is {self.user} and title is {self.title}"

class ExpenseShare(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='shares')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='shares')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    share_type = models.CharField(max_length=20, choices=(('equal', 'Equal'), ('exact', 'Exact'), ('percentage', 'Percentage')))
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user} owes {self.amount}"
