from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from stickerstormapi.models import Order


class OrderView(ViewSet):
    """sticker storm order view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single order

        Returns:
            Response -- JSON serialized order
        """
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all orders

        Returns:
            Response -- JSON serialized list of orders
        """
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders
    """
    class Meta:
        model = Order
        fields = ('id', 'user', 'created_date', 'completed_date', 'order_sticker', 'quantity', 'total')