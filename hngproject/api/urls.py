from django.urls import path
from .views import SlackUserDetail, #SlackUserList

urlpatterns = [
    path('slackuser/<int:pk>', SlackUserDetail.as_view()),
    #path('slackuser/', SlackUserList.as_view()),
]
