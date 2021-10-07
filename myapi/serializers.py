from re import I
from django.db.models import fields
from rest_framework import serializers
from .models import TODO


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = "__all__"
