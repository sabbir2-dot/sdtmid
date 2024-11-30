from django.shortcuts import render, redirect
from .form import RegistrationForm, ChangeUserData
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
# Create your views here.
# function based view
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = RegistrationForm()
#     return render(request, 'register.html', {'form' : form, 'type' : 'Register'})

# class based view

class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = 'login'

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.save()
        return redirect(self.success_url)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context
# function based login view

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = name, password = userpass)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form' : form, 'type' : 'Login'})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ChangeUserData(instance = request.user)
    return render(request, 'update_profile.html', {'form' : form})

@login_required
def pass_Change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'pass_change.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     return redirect('user_login')