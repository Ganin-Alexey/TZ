import uuid
from django.contrib.auth import login
from django.contrib.auth.middleware import get_user
from django.views import View
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import filters
from .serializers import *
import datetime

# -------Имитируем Fronted часть (Запросы)---------
class InterrogationDetail(View):
    def get(self, request, id):
        return render(request, 'interrogation_detail.html', context={'id': id})


class InterrogationList(View):
    def get(self, request):
        if get_user(request).id == None:
            uu = str(uuid.uuid4())
            mail = '' + uu + '@mail.ru'
            pas = uu
            cur_user = get_user_model().objects.create_user(email=mail, password=uu, full_name='Anonim')
            login(request, cur_user)
            user_id = cur_user.id
        else:
            user_id = get_user(request).id
        return render(request, 'interrogations.html', context={'user_id': user_id})


class InterrogationAnsweredDetail(View):
    def get(self, request, user_id):
        return render(request, 'answered.html', context={'user_id': user_id})
# -------Имитируем Fronted часть(Запросы)---------


class InterrogationAPIList(ListAPIView):
    queryset = Interrogation.objects.filter(is_active=True, stop__gte=datetime.datetime.today(), start__lte=datetime.datetime.today())
    serializer_class = InterrogationSerializer


class InterrogationAPIDetail(APIView):
    def get(self, request, id):
        interrogation = get_object_or_404(Interrogation, id=id)
        serializer = InterrogationSerializer(interrogation)
        return Response(serializer.data)


class InterrogationAnsweredAPIDetail(APIView):
    def get(self, request, user_id):
        strings = Answer.objects.filter(user=user_id).values('interrogation__title').distinct()
        sp_interrogation = CharFieldSerializer(strings, many=True)
        answers = Answer.objects.filter(user=user_id)
        serializer = InterrogationAnsweredSerializer(answers, many=True)
        return Response((serializer.data)+([sp_interrogation.data]))


class QuestionAnswer(GenericAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get(self, request, format=None):
        answers = Answer.objects.all()
        serializer_class = AnswerGetSerializer(answers, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        answer = AnswerSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            if get_user(request).is_authenticated:
                cur_user = get_user(request)
            else:
                uu = str(uuid.uuid4())
                mail = '' + uu + '@mail.ru'
                pas = uu
                cur_user = get_user_model().objects.create_user(email=mail, password=uu, full_name='Anonim')
                login(request, cur_user)
            sp = answer.save()
            Answer(user=cur_user, question=sp[1], choice=sp[0], interrogation=sp[2]).save()
            return Response({'result': 'OK'})