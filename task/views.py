from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

db = {
    "slackUsername":"ahmaad",
    "age":25,
    "bio":"web developer",
    "backend":True
}


def home(request):
    return JsonResponse(db)