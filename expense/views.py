from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserModel, Expense, ExpenseShare
from .serializers import UserSerializer, ExpenseSerializer
from django.db.models import Sum
from .utils import generate_balance_sheet_all_users

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def custom_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials or user does not exist.'}, status=status.HTTP_401_UNAUTHORIZED)
    
@csrf_exempt
@api_view(["POST"])
def custom_logout(request):
    if not request.user.is_authenticated:
        return Response({'error': 'User is not logged in.'}, status=status.HTTP_400_BAD_REQUEST)

    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'You have already Created your account'})
    

@api_view(['GET'])
def retrieve(request, user_id):
    if request.user.is_authenticated:
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response({'error':'You are not Authorized to retrieve data'})

@api_view(['GET'])
def retrieve_all(request):
    if request.user.is_authenticated:
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    else:
        return Response({"error":"You are not authorized to retrieve data"})


@api_view(['POST'])
def add_expense(request):
    if request.user.is_authenticated:
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error':'you are not authorized to add expenses'})


@api_view(['GET'])
def get_user_expenses(request, user_id):
    if request.user.is_authenticated:
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        expenses = Expense.objects.filter(user=user)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error':'you are not authorized to get user expenses'})



@api_view(['GET'])
def get_overall_expenses(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.all()
        total_expense_amount = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
        serializer = ExpenseSerializer(expenses, many=True)
        return Response({
            'total_expense_amount': total_expense_amount,
            'expenses': serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error':'you are not authorized to get overall user expenses'})

@api_view(['GET'])
def download_all_users_balance_sheet(request):
    if request.user.is_authenticated:
        return generate_balance_sheet_all_users()
    else:
        return Response({'error':'you are not authorized to download all user balance sheet'})