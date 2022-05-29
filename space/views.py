from . import forms
import account.forms
import account.views
from django.http import HttpResponseRedirect
from django.shortcuts import render

class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm

class SignupView(account.views.SignupView):

    form_class =  forms.SignupForm
    

    def generate_username(self, form):
        username = form.cleaned_data["email"]
        return username
    def after_signup(self, form):
        HttpResponseRedirect('/')
        super(SignupView, self).after_signup(form)

def home(request):
	return render(request, 'home/index.html')