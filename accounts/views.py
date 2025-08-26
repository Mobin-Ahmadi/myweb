from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordResetForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context.get('form')
        
        if form.is_bound and (form.data.get('username') or form.data.get('password')):
            context['show_error'] = form.errors
        else:
            context['show_error'] = False
        return context


from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=False,
                email_template_name='accounts/password_reset_email.html',
                subject_template_name='accounts/password_reset_subject.txt',
            )
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'accounts/password_reset.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')
        
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
