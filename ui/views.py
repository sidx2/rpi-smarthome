from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "index.html")

def api(request, pin):
    print(f"pin {pin} has been turned on/off")
    return JsonResponse({
        "status" : "success"
    })
    
