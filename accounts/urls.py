from django.urls import path
from .views import signup_view,CustomLoginView , password_reset_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view,name='signup'),
    path('login/', CustomLoginView.as_view(next_page='base'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='base'), name='logout'),
    path('password_reset/', password_reset_view, name='password_reset'),  # AJAX فقط این مرحله
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),]