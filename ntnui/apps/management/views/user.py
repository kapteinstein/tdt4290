from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required, name='dispatch')
class UserSettings(View):
    ''' Returns an html template containing user settings '''
    template_name = 'group_list.html'

    def get(self, request):
        return render(request, self.template_name)
