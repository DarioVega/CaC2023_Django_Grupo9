from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def lista(request):
    return render(request,'lista/lista.html')