from django.conf.urls import url
from . import views

app_name = 'notes'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login_user/$', views.loginUser, name='loginUser'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout_user/$', views.logoutUser, name='logoutUser'),
    url(r'^create_note/$', views.createNote, name='createNote'),
    url(r'^edit_note/(?P<pk>[0-9]+)/$', views.editNote, name='editNote'),
    url(r'^delete_note/(?P<pk>[0-9]+)/$', views.deleteNote, name='deleteNote'),



]