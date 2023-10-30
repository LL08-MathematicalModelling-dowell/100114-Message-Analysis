from django.urls import path
from .views import SentenceAnalysisView

urlpatterns=[
    path('noun_&_verb/v1/API', SentenceAnalysisView.as_view(), name='noun_&_verb'),
]

