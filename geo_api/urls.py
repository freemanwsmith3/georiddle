from django.urls import path
from .views import CountryList, AnswerList, RiddleRetrieve, Results

app_name = 'geo_api'

urlpatterns = [
    # path('countries/<int:pk>/', CountryDetail.as_view(), name='detailcreate'),
    path('answers/', AnswerList.as_view(), name='answerlist'),
    path('countries/', CountryList.as_view(), name='listcreate'),
    path('riddles/<int:day>/', RiddleRetrieve.as_view(), name='riddleretrieve'),
    # path('guesses/<int:pk>/', GuessList.as_view(), name='guesslist'),
    path('results/<str:month>/<str:user>/', Results.as_view(), name='results'),
]
