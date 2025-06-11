from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def bmi_calculator(request):
    return render(request, 'bmi.html')

def glucose_evaluator(request):
    return render(request, 'glucose.html')

def nutrition(request):
    return render(request, 'nutrition.html')

def type1(request):
    return render(request, 'type1.html')

def type2(request):
    return render(request, 'type2.html')



# Create your views here.
