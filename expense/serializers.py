from rest_framework import serializers
from .models import User, Expense, ExpenseShare

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_number']

    

class ExpenseShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseShare
        fields = ['user', 'amount', 'share_type', 'percentage']


class ExpenseSerializer(serializers.ModelSerializer):
    shares = ExpenseShareSerializer(many=True)

    class Meta:
        model = Expense
        fields = ['user', 'title', 'description', 'amount', 'date', 'shares']

    def validate_shares(self, value):
        total_share_amount = 0
        total_percentage = 0
        share_type = None

        for share in value:
            share_type = share['share_type']
            if share_type == 'exact':
                if share['amount'] is None:
                    raise serializers.ValidationError("Amount is required for exact shares.")
                total_share_amount += share['amount']
            elif share_type == 'percentage':
                if share['percentage'] is None:
                    raise serializers.ValidationError("Percentage is required for percentage shares.")
                total_percentage += share['percentage']

        if share_type == 'exact' and total_share_amount != self.initial_data.get('amount'):
            raise serializers.ValidationError("The sum of share amounts does not match the total expense amount.")
        if share_type == 'percentage' and total_percentage != 100:
            raise serializers.ValidationError("The sum of percentages must be 100%.")
        
        return value

    def create(self, validated_data):
        shares_data = validated_data.pop('shares')
        expense = Expense.objects.create(**validated_data)

        for share_data in shares_data:
            if share_data['share_type'] == 'equal':
                equal_share_amount = expense.amount / len(shares_data)
                share_data['amount'] = equal_share_amount
            elif share_data['share_type'] == 'percentage':
                share_data['amount'] = (share_data['percentage'] / 100) * expense.amount

            ExpenseShare.objects.create(expense=expense, **share_data)
        
        return expense