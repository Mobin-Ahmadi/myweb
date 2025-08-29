from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.base_view,name='base'),
    path('about/',views.about_view,name='about'),
    path('post/<int:pk>/',views.detail_view,name='post_detail'),
    path('resume/certificate/',views.certificate_view,name='certificates'),
    path('contact/',views.contact_view,name='contactme'),
    path('resume/',views.resume_view,name='resume'),
    path('comments/edit/<int:comment_id>/', views.edit_comment_ajax, name='edit_comment_ajax'),
    path('comments/delete/<int:comment_id>/', views.delete_comment_ajax, name='delete_comment_ajax'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)