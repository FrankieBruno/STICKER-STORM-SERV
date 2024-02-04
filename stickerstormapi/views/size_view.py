from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from stickerstormapi.models import Size


class SizeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single size

        Returns:
            Response -- JSON serialized size
        """
        size = Size.objects.get(pk=pk)
        serializer = SizeSerializer(size)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all sizes

        Returns:
            Response -- JSON serialized list of sizes
        """
        size = Size.objects.all()
        serializer = SizeSerializer(size, many=True)
        return Response(serializer.data)


class SizeSerializer(serializers.ModelSerializer):
    """JSON serializer for size model
    """
    class Meta:
        model = Size
        fields = ('id', 'sticker_size')