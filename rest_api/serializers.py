from rest_framework import serializers
# from .models import Player, Point
from .models import Point

# class PlayerSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'user_name',
#             'first_name',
#             'last_name',
#         )
#         model = Player

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user_name',
            'score',
            'date_created'
        )
        model = Point