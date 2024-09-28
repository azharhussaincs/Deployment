from django.shortcuts import render

def home(request):
    print("Home view called")
    return render(request, 'users/home.html')  
