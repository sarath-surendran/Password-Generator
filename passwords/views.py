from django.shortcuts import render, redirect
from .models import SavePassword

# Create your views here.
def savepassword(request):
    print('function called')
    if request.method == "POST":
        password = request.POST.get('save_password')
        print(password)
        SavePassword.objects.create(
            user = request.user,
            password = password
        )
        return redirect('view_saved_passwords')
    
def viewsavedpasswords(request):
    user = request.user
    passwords = SavePassword.objects.filter(user=user)
    context = {
        'passwords': passwords,
    }
    return render(request, 'saved_passwords.html', context)