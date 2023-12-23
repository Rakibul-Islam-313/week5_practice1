from django.urls import path
from . import views
urlpatterns = [
    path('profile/',views.profile, name='profile_page'),
    path('signup/',views.sign_up, name='sign_up_page'),
    path('login/', views.log_in,name='login_page'),
    path('logout/',views.log_out,name='logout_page'),

    path('pass_change/', views.password_change,name='pass_change_page'),

    path('pass_change_2/',views.password_change2,name='pass_change_2_page'),
]