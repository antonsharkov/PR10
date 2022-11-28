from django.http import HttpResponse
import massivs
import scipy

# Create your views here.

def index(request, array, s1, s2):
    return HttpResponse(f"Начальный массив: {array}  Измененный массив: {massivs.Zamena(array, s1, s2)}")