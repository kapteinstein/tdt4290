from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from database.models import MembershipModel, GroupModel
from management.utils import group_utils, group_decorators

membership_decorators = [login_required, group_decorators.is_member]


@method_decorator(login_required, name='dispatch')
class GroupList(View):
    ''' Returns an html template containing all groups based on membership of the active user'''
    template_name = 'group_list.html'

    def get(self, request):
        user_groups = GroupModel.objects.filter(members=request.user)
        other_groups = GroupModel.objects.all().exclude(members=request.user)

        context = {
            'user_groups': user_groups,
            'other_groups': other_groups
        }

        return render(request, self.template_name, context)


@method_decorator(membership_decorators, name='dispatch')
class GroupHome(View):
    template_name = 'group_home.html'

    def get(self, request, slug):
        group_info = group_utils.get_group_info(request, slug)

        # Flatten the group_info object before passing it on
        context = {**group_info}

        return render(request, self.template_name, context)


@method_decorator(membership_decorators, name='dispatch')
class GroupMembers(View):
    template_name = 'group_members.html'

    def get(self, request, slug):
        group_info = group_utils.get_group_info(request, slug)
