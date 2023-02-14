from rest_framework import generics, status
from geo.models import Country, Riddle
from .serializers import CountrySerializer, RiddleSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

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
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        riddleId = self.kwargs['pk']

        user = self.request.session.session_key

        #### below i am checking to see if there is any guess dicitonary in the session for the user
        # then checking if there is a riddle specific guess array
        #this will be passed into the riddle to displayed already used guesses
        # if not i am creating empty ones
        #then saving them to the session with the modified command
        print(user)
        if str(riddleId) not in self.request.session.get('guess_data'):
            riddle_guess = []
            print("ok")
            if self.request.session.get('guess_data'):
                guess_data_dict = {}
            else:
                guess_data_dict = self.request.session.get('guess_data')

            guess_data_dict[str(riddleId)] = riddle_guess
            self.request.session['guess_data'][str(riddleId)] = guess_data_dict
            
        self.request.session.modified = True
        print(self.request.session.get('guess_data')[str(riddleId)])

        return   Riddle.objects.all()

