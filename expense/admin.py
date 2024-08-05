from django.contrib import admin
from .models import UserModel, Expense, ExpenseShare
# Register your models here.
class display_user(admin.ModelAdmin):
    list_display = ('username' , 'email' , 'phone_number')
admin.site.register(UserModel,display_user)

admin.site.register(Expense)
admin.site.register(ExpenseShare)