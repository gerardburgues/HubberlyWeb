from django.conf.urls import url
from first_app import views
app_name = 'first_app'
urlpatterns = [
    url(r'^faqs/$', views.faqs, name='faqs'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^$', views.index, name='index'),

    url(r'^Contact_question/$', views.Contact_question, name='Contact_question'),
    url(r'^spanish_home/$', views.spanish_home, name='spanish_home'),
    url(r'^spanish_faqs/$', views.spanish_faqs, name='spanish_faqs'),
]