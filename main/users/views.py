from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm

def create_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render (request , 'users/register.html' , context)

