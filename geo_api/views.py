from rest_framework import generics, status
from geo.models import Country, Riddle, Guess
from .serializers import CountrySerializer, RiddleSerializer, GuessSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class CountryList(generics.ListAPIView):
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
    queryset = Riddle.objects.all()
    serializer_class = RiddleSerializer

    

class GuessList(generics.ListCreateAPIView):
    serializer_class = GuessSerializer


    def get_queryset(self):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        user = self.request.session.session_key

        #############
        # temporary user issue
        ############

        user = 'hix5mm5xfmx0wp4lz3go5peohamu8xhb'
        return Guess.objects.filter(riddle = self.kwargs['pk'], user = user)

    def post(self, request, pk):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        user = self.request.session.session_key

        #############
        # temporary user issue
        ############
        user = 'hix5mm5xfmx0wp4lz3go5peohamu8xhb'
        try: 
            guess = Guess(user = user, country = Country.objects.get(id = request.data['country']), riddle = Riddle.objects.get(id = pk) )
            guess.save()
        except Exception as e:
            print('exception: ', e)
            return Response({'Bad Request':'Invalid Guess'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(GuessSerializer(guess).data, status=status.HTTP_201_CREATED)



    
    

# class GuessRetrieve(generics.ListAPIView):
#     serializer_class = GuessSerializer
    
#     def get(self, request, pk):
        
#         ###############
#         ##  SESSION KEY HERE
#         ##############
#         if not self.request.session.exists(self.request.session.session_key):
            
#             self.request.session.create()
            
#         user = self.request.session.session_key
#         #####################
#         ### testing before getting sessions keys functioning
#         ##############

#         user = 'iig7q3mn197kz2cfjkocpowfjbj4n8l3'
#         data=request.data
#         guess = Guess.objects.filter(riddle = pk, user = user)[0]
#         # data['user'] = self.request.session.session_key 
#         # user = data['user']
#         print("D: ", guess)

#         data['id'] = guess.pk
#         data['country'] = guess.country.id
#         data['riddle'] = guess.riddle.id
#         data['user'] = user

#         print("data: ", data)
#         serializer = self.serializer_class(data=data)
#         print(serializer)
#         if serializer.is_valid() and user:
#             print('pk', pk)
#             # guess = Guess.objects.filter(riddle = pk, user = user)
#             # print("G", guess)
#             # data['country']=Guess.country
#             # data['riddle']=Guess.riddle
#             # print(data)

#             return Response(GuessSerializer(data).data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'Bad Request':'Invalid User or Week'}, status=status.HTTP_400_BAD_REQUEST)
