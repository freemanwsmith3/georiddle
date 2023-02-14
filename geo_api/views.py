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


        ######### for testing session data #
        ######
        ##############
        
        if not self.request.session.get('guess_data'):
            guess_data_dict = {}
            guess_data_dict['2'] = []
            self.request.session['guess_data'] = guess_data_dict
            print("DOesnt exist")
        else:
            guess_data_dict = self.request.session.get('guess_data')

        guess_data_this_week = guess_data_dict['2']

        guess_data_this_week.append('guessed cdddlder')
        print(user)
        print(guess_data_dict)
        #############
        # temporary user issue
        ############

        #user = 'hix5mm5xfmx0wp4lz3go5peohamu8xhb'
        return   Riddle.objects.all()

