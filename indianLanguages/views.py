from django.shortcuts import render
from language.models import Language

def homeView(request):
    languages = Language.objects.all()
    return render(request, "home.html", {"languages":languages})