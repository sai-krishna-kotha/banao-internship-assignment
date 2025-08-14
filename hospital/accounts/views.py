from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from .forms import SignupForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:dashboard_redirect')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

class SignupView(CreateView):
    model = CustomUser
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('accounts:login')

@login_required
def dashboard_redirect(request):
    if request.user.user_type == 'doctor':
        return redirect('accounts:doctor_dashboard')
    else:
        return redirect('accounts:patient_dashboard')

@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')