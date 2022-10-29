from rest_framework import serializers
from .models import SlackUser

class SlackUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlackUser
        fields = 'slackUsername', 'backend', 'age', 'bio'
        extra_kwargs = {
            'id': {'read_only': True}
        }