from rest_framework import serializers
from .models import Sentences

class SentencesDataserializer(serializers.ModelSerializer):

    class Meta:
        model = Sentences
        fields = '__all__'
        api_key = serializers.CharField(max_length=510, required=True)
