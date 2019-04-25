from django.db import models

# class Player(models.Model):
#     user_name = models.CharField(max_length=255, primary_key=True)
#     first_name = models.CharField(max_length=255, blank=False)
#     last_name = models.CharField(max_length=255, blank=False)
#     class Meta:
#         db_table = 'player'   

class Point(models.Model):
    # user_name= models.ForeignKey('User', on_delete=models.CASCADE, related_name='scores')
    user_name = models.CharField(max_length=255, default="XXX")
    score= models.IntegerField(blank=False, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'point'