from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import login as auth_login
from authentication.forms import SignUpForm


class UserSignup(View):
    ''' Returns an html template containing user settings '''
    template_name = 'registration/signup.html'

    def get(self, request):
        form = SignUpForm()
        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            auth_login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')

            return redirect('home')

        context = {
            'form': form
        }

        return render(request, self.template_name, context)
