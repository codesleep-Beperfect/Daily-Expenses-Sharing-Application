from rest_framework import status
import uuid
import csv
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Expense, ExpenseShare
from .serializers import UserSerializer, ExpenseSerializer
from django.db.models import Sum
from .utils import generate_balance_sheet_all_users


# Create your views here.
@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def retrieve_all(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_expense(request):
    serializer = ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user_expenses(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    expenses = Expense.objects.filter(user=user)
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_overall_expenses(request):
    expenses = Expense.objects.all()
    total_expense_amount = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    serializer = ExpenseSerializer(expenses, many=True)
    return Response({
        'total_expense_amount': total_expense_amount,
        'expenses': serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def download_all_users_balance_sheet(request):
    return generate_balance_sheet_all_users()