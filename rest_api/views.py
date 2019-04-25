from rest_framework import generics, permissions
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
# from .serializers import PointSerializer, PlayerSerializer
from .serializers import PointSerializer
# from .models import Player, Point
from .models import Point
from django.db.models import Sum

class AddScore(generics.CreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
        
    def perform_create(self, serializer):
        Point.objects.create(user_name=self.kwargs['player'], score=self.kwargs['score'])
        
def GetScore(request, player):
    scores = Point.objects.filter(user_name=player)
    response = {}

    if(scores.count() == 0):
        response = JsonResponse({'status':'false','message':'No player registered with this name'}, status=500)
    else:
        total = scores.aggregate(Sum('score'))['score__sum']
        response = JsonResponse({
            'player' : player,
            'total_score' : total,
        })

    return response