from django.db import models

class Sentences(models.Model):
    id = models.AutoField(primary_key = True)
    data_sentence = models.TextField(null=False, blank=False)
