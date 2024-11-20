# transactions/serializers.py
from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'user', 'timestamp', 'status']
        read_only_fields = ['id', 'timestamp']
