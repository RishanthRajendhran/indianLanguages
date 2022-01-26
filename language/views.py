from django.shortcuts import render, redirect
from .models import Language
from . import forms

# Create your views here.
def languageDetail(request, slug):
    language =  Language.objects.get(slug=slug)
    return render(request, "language/languageDetail.html",{"language":language})

def languageCreate(request):
    if request.method == "POST":
        form = forms.CreateLanguage(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save()
            return redirect("home")
    else:
        form = forms.CreateLanguage()
    return render(request, "language/languageCreate.html", {"form":form})
