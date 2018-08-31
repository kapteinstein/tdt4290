from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import View
from database.models import MembershipModel, GroupModel
from database.forms import GroupInvitationForm
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

    # Use the group invitation form for creating new invitations in the view
    form_class = GroupInvitationForm

    def get(self, request, slug):
        ''' Retrieve the required group and member information'''
        group_info = group_utils.get_group_info(request, slug)
        group_member_info = group_utils.get_group_member_info(
            group_info['group'])

        form = self.form_class(group=group_info['group'])

        context = {
            **group_info,
            **group_member_info,
            'form': form,
        }

        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        ''' Retrieve the group and member information (again) TODO: Find a smarter way to CACHE this perhaps '''
        group_info = group_utils.get_group_info(request, slug)
        group_member_info = group_utils.get_group_member_info(
            group_info['group'])

        form = self.form_class(request.POST, group=group_info['group'])

        context = {
            **group_info,
            **group_member_info,
            'form': form,
        }

        if form.is_valid():
            # Re-initialize the form if successfull
            context['form'] = self.form_class(
                initial={'group': group_info['group']})
            messages.add_message(
                request, messages.SUCCESS, "Invitation Sent!")

            return render(request, self.template_name, context)

        messages.add_message(
            request, messages.ERROR, "Invitation Not Sent!")
        return render(request, self.template_name, context)
