from rest_framework import serializers

from .models import SlackModel

class SlackModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlackModel
        fields = ("slackUsername","age","backend","bio")