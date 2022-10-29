from rest_framework import generics
from .models import SlackUser
from .serializers import SlackUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



#Create your views here.
class SlackUserList(generics.ListCreateAPIView):
    queryset = SlackUser.objects.all()
    serializer_class = SlackUserSerializer

class SlackUserDetail(generics.RetrieveAPIView):
	queryset = SlackUser.objects.all()
	serializer_class = SlackUserSerializer 

class JsonView(APIView):
    def get(self, request):
        return Response({'some': 'data'})