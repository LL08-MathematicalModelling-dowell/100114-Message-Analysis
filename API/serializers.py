from rest_framework import serializers
from .models import Sentences

class SentencesDataserializer(serializers.ModelSerializer):
    class Meta:
        model = Sentences
        fields = '__all__'