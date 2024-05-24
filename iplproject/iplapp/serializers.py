from rest_framework import serializers
from .models import Teams


class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = "__all__"