from rest_framework import generics, status
from geo.models import Country, Riddle
from .serializers import CountrySerializer, RiddleSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

class CountryList(generics.ListCreateAPIView):
    #permission_classes = [IsAdminUser]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
     
class AnswerList(generics.ListAPIView):
    #permission_classes = [IsAdminUser]
    queryset = Country.objects.filter(status= 'correct')
    serializer_class = CountrySerializer
    
    

class RiddleRetrieve(generics.RetrieveAPIView):
    #permission_classes = [IsAdminUser]
    serializer_class = RiddleSerializer
    

    def get_queryset(self, *args, **kwargs):

        riddleId = self.kwargs['pk']
        intitializeGuessData(self, riddleId)


        return   Riddle.objects.all()
    
    def post(self, request, *args, **kwargs):
        print(self.request.session.session_key)
        riddleId = self.kwargs['pk']
        intitializeGuessData(self, riddleId)
        
        guess_data_dict = self.request.session.get('guess_data')
        this_weeks_guesses = guess_data_dict[str(riddleId)]
        print("data in cookie: ", guess_data_dict[str(riddleId)])
        try: 
            guessed_country = request.data['country']

        except Exception as e:
            guessed_country ='placeholder' 
            print(e)
        this_weeks_guesses.append(guessed_country)
        guess_data_dict[str(riddleId)] = this_weeks_guesses
        print('request data: ', guessed_country)
        print("g: ", guess_data_dict)
        self.request.session['guess_data'] = guess_data_dict
        self.request.session.modified = True
        return Response(status=status.HTTP_201_CREATED)    



def intitializeGuessData(self, riddleId):
    print("initialize: ", self.request.session.session_key)
    #### below i am checking to see if there is any guess dicitonary in the session for the user
    # then checking if there is a riddle specific guess array
    #this will be passed into the riddle to displayed already used guesses
    # if not i am creating empty ones
    #then saving them to the session with the modified command

    if not self.request.session.exists(self.request.session.session_key):
        print("one")
        self.request.session.create()
        self.request.session.modified = True
    

    if self.request.session.get('guess_data'):
        print("two")
        guess_data_dict = self.request.session.get('guess_data')
    else:
        guess_data_dict = {}

    if str(riddleId) not in guess_data_dict:
        print('three')
        riddle_guess = []
        guess_data_dict[str(riddleId)] = riddle_guess
        self.request.session['guess_data'] = guess_data_dict
        self.request.session.modified = True
        
    ### use this later
    # if self.request.session.get('guess_data'):
    #     guess_data_dict = self.request.session.get('guess_data')
    # else:
    #     guess_data_dict = {}

    # if str(riddleId) in self.request.session.get('guess_data'):
    #     riddle_guess =  guess_data_dict[str(riddleId)]
    # else: 
    #     riddle_guess = []
    #     guess_data_dict[str(riddleId)] = riddle_guess
    #     self.request.session['guess_data'][str(riddleId)] = guess_data_dict
        
    
    
    
