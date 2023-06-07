from django.contrib import admin
from django.urls import path
from .  import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve 
urlpatterns = [
    path('',views.home,name="home"),
    path('features',views.features,name="features"),
    path('use_cases_strategy',views.use_cases_strategy,name="use_cases_strategy"),
    path('use_cases_invester',views.use_cases_invester,name="use_cases_invester"),
    path('Open_interest_analysis', views.Open_interest_analysis, name='Open_interest_analysis'),
    path('Strategy_builder_straddle', views.Strategy_builder_straddle, name='Strategy_builder_straddle'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('help_support', views.help_support, name='help_support'),
    path('learning_center', views.learning_center, name='learning_center'),
    path('blog', views.blog, name='blog'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('signUp', views.signUp, name='signUp'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('change_pass/<token>/',views.change_pass,name='change_pass'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)