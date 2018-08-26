from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from database.models import MembershipModel, GroupModel


@login_required
def group_list(request):
    user_groups = GroupModel.objects.filter(members=request.user)
    other_groups = GroupModel.objects.all().exclude(members=request.user)

    print(other_groups[0].group_media)

    return render(request, 'group_list.html', {
        'user_groups': user_groups,
        'other_groups': other_groups
    })


@login_required
def group_home(request, slug):
    ''' Returns the html template for the group homepage '''
    return HttpResponse('<html><body>' + slug + '</body></html >')
