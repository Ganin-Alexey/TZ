from .views import *
from django.urls import path

urlpatterns = [
    path('interrogations/', InterrogationList.as_view(), name='interrogations-list'),
    path('interrogations/detail/<int:id>/', InterrogationDetail.as_view(), name='interrogation-detail'),
    path('interrogations/answered/<int:user_id>/', InterrogationAnsweredDetail.as_view(), name='interrogation-answered'),
    path('api-interrogations/', InterrogationAPIList.as_view()),
    path('api-interrogations/detail/<int:id>/', InterrogationAPIDetail.as_view()),
    path('api-interrogations/answered/<int:user_id>/', InterrogationAnsweredAPIDetail.as_view()),
    path('answer/', QuestionAnswer.as_view()),
]