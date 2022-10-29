from rest_framework import generics
from .models import SlackUser
from .serializers import SlackUserSerializer


#Create your views here.
class SlackUserList(generics.ListCreateAPIView):
    queryset = SlackUser.objects.all()
    serializer_class = SlackUserSerializer

class SlackUserDetail(generics.RetrieveAPIView):
	queryset = SlackUser.objects.all()
	serializer_class = SlackUserSerializer 