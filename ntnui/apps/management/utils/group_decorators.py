from django.shortcuts import redirect
from database.models import GroupModel


def is_member(f):
    ''' Creates a python decorator for membership status '''
    def _wrapped(request, *args, **kwargs):
        # Redirect the user to the group list if the Group is not actually a group
        try:
            if request.user not in GroupModel.objects.get(slug=kwargs['slug']):
                # Redirect the user to the page they came from
                return redirect(request.META['HTTP_REFERER'])
        except GroupModel.DoesNotExist:
            return redirect(request.META['HTTP_REFERER'])

        return f(request, *args, **kwargs)
    return _wrapped
