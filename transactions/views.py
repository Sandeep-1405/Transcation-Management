# transactions/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    #permission_classes = [IsAuthenticated]

    # Custom create method
    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id  
        serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            transaction = serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    # Custom PUT method to update transaction status
    @action(detail=True, methods=['put'])
    def update_status(self, request, pk=None):
        transaction = self.get_object()
        status = request.data.get('status')
        
        if status not in ['PENDING', 'COMPLETED', 'FAILED']:
            return Response({'error': 'Invalid status'}, status=400)
        
        transaction.status = status
        transaction.save()
        return Response(TransactionSerializer(transaction).data)
