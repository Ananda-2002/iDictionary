from django.contrib import admin
from django.urls import path
from .views import translation, parts_of_speech, synonyms, all, languages

urlpatterns = [
    path('get-translation', translation),
    path('get-parts-of-speech', parts_of_speech),
    path('get-synonyms', synonyms),
    path('get-all', all),
    path('get-languages', languages)
]
