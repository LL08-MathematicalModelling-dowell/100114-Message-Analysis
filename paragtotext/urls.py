from django.urls import path
from .views import Collect_noun_and_verb_from_article



urlpatterns=[
    path('Collect/noun_and_verb/article', Collect_noun_and_verb_from_article, name='Collect_noun_and_verb_from_article'),
]