from django.urls import path
from .views import SlackUserDetail

urlpatterns = [
    path('slackuser/<int:pk>', SlackUserDetail.as_view()),
]