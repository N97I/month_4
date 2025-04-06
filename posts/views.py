from django.shortcuts import render, HttpResponse
import random 



def test_view(request):
    return HttpResponse(f"Hello world {random.randint(1, 100)}")

def html_view(request):
    return render(request, "base.html")
