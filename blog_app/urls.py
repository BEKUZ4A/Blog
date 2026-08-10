from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('signup/', views.SignUpView.as_view(), name='signup_page'),
    path('account/', views.account_settings, name='account_settings'),
    path('change-password/', views.change_password, name='change_password'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.post_detail,
        name='post_detail',
    ),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]
