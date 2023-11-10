from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from imgtotext.noun_verb import For_noun_verb_adj
from .helpers import check_api_key
from .serializers import SentencesDataserializer

class SentenceAnalysisView(APIView):
    def post(self, request):

        try:
            json_data = request.data
            serializer = SentencesDataserializer(data=json_data)

            if serializer.is_valid():

                res = check_api_key(json_data['api_key'])

                if res != "success":
                    return Response(
                        {"success": False, "message": res,
                         "data": []},
                        status=status.HTTP_404_NOT_FOUND)

                nouns, adjectives, verbs = For_noun_verb_adj(json_data['paragraph'])
                analysis = {
                    "sentence": json_data['paragraph'],
                    "nouns": nouns,
                    "adjectives": adjectives,
                    "verbs": verbs,
                }
                serializer.save()
                return Response({"success": True,"message":'We successfully analyzed the data', "data" : analysis},status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message" : serializer.errors
                },status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Exception as e:
            return Response({
                'message' : str(e),
                "success": False,
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)