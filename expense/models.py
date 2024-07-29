from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.name
    
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"user is {self.user} and title is {self.title}"

class ExpenseShare(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='shares')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shares')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    share_type = models.CharField(max_length=20, choices=(('equal', 'Equal'), ('exact', 'Exact'), ('percentage', 'Percentage')))
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user} owes {self.amount}"
