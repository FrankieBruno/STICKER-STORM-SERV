from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from stickerstormapi.models import Sticker, Finish, Size
from django.contrib.auth.models import User 




class StickerView(ViewSet):
    """sticker storm sticker view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single sticker

        Returns:
            Response -- JSON serialized sticker
        """
        sticker = Sticker.objects.get(pk=pk)
        serializer = StickerSerializer(sticker)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all stickers

        Returns:
            Response -- JSON serialized list of stickers
        """
        
        stickers = Sticker.objects.filter(user=request.auth.user)
            
        serializer = StickerSerializer(stickers, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized game instance
        """
        user=request.auth.user

        finish_type = Finish.objects.get(pk=request.data["finish_type"])
        sticker_size = Size.objects.get(pk=request.data["sticker_size"])

        sticker = Sticker.objects.create(
            user=user,
            name=request.data["name"],
            image=request.data["image"],
            finish_type=finish_type,
            sticker_size=sticker_size,
            price=request.data["price"]
        )

        serializer = StickerSerializer(sticker)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        
        
        sticker = Sticker.objects.get(pk=pk)
        sticker.name=request.data["name"]
        sticker.image=request.data["image"]
        sticker.price=request.data["price"]
        
        finish_type = Finish.objects.get(pk=request.data["finish_type"])
        sticker_size = Size.objects.get(pk=request.data["sticker_size"])
        sticker.finish_type=finish_type
        sticker.sticker_size=sticker_size
        sticker.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):

        sticker = Sticker.objects.get(pk=pk)
        sticker.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class SizeSerializer(serializers.ModelSerializer):
    """JSON serializer for size model
    """
    class Meta:
        model = Size
        fields = ('id', 'sticker_size')

class FinishSerializer(serializers.ModelSerializer):
    """JSON serializer for Finish model
    """
    class Meta:
        model = Finish
        fields = ('id', 'finish_type')
class StickerSerializer(serializers.ModelSerializer):
    """JSON serializer for sticker model
    """
    sticker_size = SizeSerializer(read_only=True)
    finish_type = FinishSerializer(read_only=True)

    class Meta:
        model = Sticker
        fields = ('id', 'user', 'name', 'image', 'finish_type', 'sticker_size', 'price')
        