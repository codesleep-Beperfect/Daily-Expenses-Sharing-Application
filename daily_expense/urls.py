"""
URL configuration for daily_expense project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from expense import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create, name='create_user'),
    path('retrieve_all/', views.retrieve_all , name='retrieve_all'),
    path('retrieve/<uuid:user_id>/', views.retrieve, name='retrieve'),
    path('add-expenses/', views.add_expense, name='add_expense'),
    path('user/<uuid:user_id>/expenses/', views.get_user_expenses, name='get_user_expenses'),
    path('expenses/overall/', views.get_overall_expenses, name='get_overall_expenses'),
    path('balance-sheet/download/', views.download_all_users_balance_sheet, name='download_all_users_balance_sheet'),
]
