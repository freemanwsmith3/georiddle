from rest_framework import serializers
from geo.models import Country, Riddle, Guess

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

class GuessSerializer(serializers.ModelSerializer):
    
    # country = CountrySerializer(read_only=True)
    # riddle = RiddleSerializer(read_only=True)

    class Meta:
        model = Guess
        fields = ('id', 'country', 'riddle', 'user')


