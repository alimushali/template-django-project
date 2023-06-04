from rest_framework import serializers
from coreapp.models import AbstractUnit1

class AbstractUnit1Serializer(serializers.ModelSerializer):
    class Meta:
        model=AbstractUnit1
        fields = (
            'name',
            'description',
            'integer_property',
        )