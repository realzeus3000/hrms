from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #Log in user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()

    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def register_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            # log user init
            return redirect('home')
    else:
        form = UserCreationForm
    context = {'form':form}
    return render(request, 'accounts/register.html',context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')
