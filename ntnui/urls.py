from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# from accounts import views as accounts_views
# from groups import views as groups_views


''' Include URL Patterns '''
urlpatterns = [
    path('admin/', include('database.urls')),
    path('nested_admin/', include('nested_admin.urls')),
    path('api/', include('api.urls')),

    # Application routes
    path('a/', include('authentication.urls')),
    path('m/', include('management.urls')),

    # url(r'^ajax/', include('forms.ajax')),
    # url(r'^$', groups_views.list_groups, name='home'),
    # url(r'^forms/', include('forms.urls')),
    # url(r'^groups/', include('groups.urls')),
    # url(r'^hs/', include('hs.urls')),
    # # url(r'^signup/$', accounts_views.signup, name='signup'),
    # url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(
    #     template_name='accounts/password_change.html'),
    #     name='password_change'),
    # url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='accounts/password_change_done.html'),
    #     name='password_change_done'),
    # url(r'^cron/accounts/all$', accounts_views.add_all_users_from_exeline,
    #     name='add_all_users_from_exeline'),
    # url(r'^cron/accounts/lastday$', accounts_views.add_last_week_users_from_exeline,
    #     name='add_last_week_users_from_exeline'),

    # Load static files
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
