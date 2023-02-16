from django.urls import path
from .views import CountryList, CountryDetail, AnswerList, RiddleRetrieve, GuessList

app_name = 'geo_api'

urlpatterns = [
    path('countries/<int:pk>/', CountryDetail.as_view(), name='detailcreate'),
    path('answers/', AnswerList.as_view(), name='answerlist'),
    path('countries/', CountryList.as_view(), name='listcreate'),
    path('riddles/<int:pk>/', RiddleRetrieve.as_view(), name='riddleretrieve'),
    path('guesses/<int:pk>/', GuessList.as_view(), name='guesslist'),
]
