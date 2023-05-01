from rest_framework import serializers
from geo.models import Country, Riddle, Result

# class CountrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = ('name',)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)
        
class RiddleSerializer(serializers.ModelSerializer):
    
    answers = CountrySerializer(read_only=True, many=True)
    class Meta:
        model = Riddle
        fields = ('id', 'question', 'answers', 'day', 'sort')

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('won', 'points','day', 'month')
