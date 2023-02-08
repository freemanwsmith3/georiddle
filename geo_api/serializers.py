from rest_framework import serializers
from geo.models import Country, Riddle

# class CountrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = ('name',)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'continent', 'capital', 'status')

class RiddleSerializer(serializers.ModelSerializer):
    
    answers = CountrySerializer(read_only=True, many=True)
    class Meta:
        model = Riddle
        fields = ('id', 'question', 'answers', 'date')

