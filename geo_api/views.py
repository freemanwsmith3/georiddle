from rest_framework import generics, status
from geo.models import Country2, Riddle, Result
from .serializers import CountrySerializer, RiddleSerializer, ResultSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.db.models import F, Sum, DecimalField, Sum

class CountryList(generics.ListCreateAPIView):
    queryset = Country2.objects.all()
    serializer_class = CountrySerializer


class AnswerList(generics.ListAPIView):
    queryset = Country2.objects.all()
    serializer_class = CountrySerializer
    
class Results(generics.ListCreateAPIView):
    
    #idk why this matters
    queryset = Result.objects.all()
    
    
    serializer_class = ResultSerializer

    def get(self, request, month, user, **kwargs):
        try: 
            #gets the individuals average

            indUserSum = Result.objects.filter(user=user, month=month).aggregate(sum= Sum('points'))['sum']
            
            #gets the users that rank above them
            userAveragesAbove = Result.objects.filter(month=month).values('user').annotate(sum= Sum('points')).filter(sum__gt=indUserSum).values_list('user', flat=True).count()
            #kinda inefficient to get the total this way, but just feels Sum
            userAveragesBelow= Result.objects.filter(month=month).values('user').annotate(sum= Sum('points')).values_list('user', flat=True).count()
            percentile = int(round((100*userAveragesAbove/userAveragesBelow), 0))

            data = {user:percentile}
            return Response( data = data, status=status.HTTP_200_OK)
        except Exception as e:
            print("Failed:", e)
            return Response(request.data, status=status.HTTP_404_NOT_FOUND)
        

    def post(self, request, month, user, **kwargs):
        try: 
            print(request.data)
            if 'won' not in request.data:
                won = False
            else:
                won = True
            result = Result( won = won, points = request.data['points'], user = user, day=request.data['day'], month=month)
            result.save()
            return Response(ResultSerializer(result).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Failed:", e)
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        
# Guess data no longer user


class RiddleRetrieve(generics.RetrieveAPIView):
    #permission_classes = [IsAdminUser]
    # serializer_class = RiddleSerializer
    # lookup_field = 'day'

    def get(self, *args, **kwargs):
        day = self.kwargs['day']
        #intitializeGuessData(self, riddleId)
        #print(Country2.objects.select_related().values())
        riddleObj = Riddle.objects.get(day=day)
        if riddleObj.sort:
            sort_method = riddleObj.sort
        else:
            sort_method = 'name'

        answers = []
        for ans in riddleObj.answers.all().order_by('population').values('name').order_by(sort_method):

            answers.append(ans)
        riddle_answers = {}
        riddle_answers['answers'] = answers
        riddle_answers['day'] = day
        riddle_answers['question'] = riddleObj.question
        return Response(riddle_answers, status=status.HTTP_200_OK)
    



def intitializeGuessData(self, riddleId):
    print("initialize: ", self.request.session.session_key)
    #### below i am checking to see if there is any guess dicitonary in the session for the user
    # then checking if there is a riddle specific guess array
    #this will be passed into the riddle to displayed already used guesses
    # if not i am creating empty ones
    #then saving them to the session with the modified command

    if not self.request.session.exists(self.request.session.session_key):
        self.request.session.create()
        self.request.session.modified = True
        print("SK", self.request.session.session_key)

    if self.request.session.get('guess_data'):
        guess_data_dict = self.request.session.get('guess_data')
    else:
        guess_data_dict = {}

    if str(riddleId) not in guess_data_dict:
        riddle_guess = []
        guess_data_dict[str(riddleId)] = riddle_guess
        print(guess_data_dict)
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
        
    
    
