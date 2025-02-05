from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('issue/<int:issue_id>/', views.issue_detail, name='issue_detail'),
    path('create_issue/', views.create_issue, name='create_issue'),
    path('issue/<int:issue_id>/add_reply/', views.add_reply, name='add_reply'),
    path('reply/<int:reply_id>/vote/<str:vote_type>/', views.vote, name='vote'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('issue/<int:issue_id>/close/', views.close_issue, name='close_issue'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]