from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from imgtotext.noun_verb import For_noun_verb_adj
from .serializers import SentencesDataserializer

class SentenceAnalysisView(APIView):
    def post(self, request):

        try:

            json_data = request.data
            serializer = SentencesDataserializer(data=json_data)
            if serializer.is_valid():
                nouns, adjectives, verbs = For_noun_verb_adj(json_data['data_sentence'])
                analysis = {
                    "sentence": json_data['data_sentence'],
                    "nouns": nouns,
                    "adjectives": adjectives,
                    "verbs": verbs,
                }
                serializer.save()
                return Response(analysis, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message' : serializer.errors
                })
        except Exception as e:
            return Response({
                'message' : str(e)
            })