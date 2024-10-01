from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('set_language/', views.set_language, name='set_language'),
    path('success/', views.success_view, name='success'),
    path('what-do-i-do/', views.what_do_i_do, name='what_do_i_do'),
    path('404/', views.page_not_found, name='page_not_found'),
    path('', views.main, name='main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


