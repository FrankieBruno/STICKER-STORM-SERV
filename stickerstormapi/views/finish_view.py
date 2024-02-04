"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from stickerstormapi.models import Finish


class FinishTypeView(ViewSet):
    """sticker storm finish view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single finish

        Returns:
            Response -- JSON serialized finish
        """
        finish_type = Finish.objects.get(pk=pk)
        serializer = FinishTypeSerializer(finish_type)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all finishes

        Returns:
            Response -- JSON serialized list of finishes
        """
        finish_types = Finish.objects.all()
        serializer = FinishTypeSerializer(finish_types, many=True)
        return Response(serializer.data)


class FinishTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for finishes
    """
    class Meta:
        model = Finish
        fields = ('id', 'finish_type')

