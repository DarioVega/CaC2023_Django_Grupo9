from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

context = {
    'form': UserCreationForm
}

def signup(request):
    return render(request, 'signup/signup.html',context)