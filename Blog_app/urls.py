from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import index, blog, post, search, post_delete, post_update, post_create, profile
from . import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('search/', search, name='search'),
    path('blog/', blog, name='post-list'),
    path('post/<id>/', post, name='post-detail'),
    path('create/', post_create, name='post-create'),
    path('accounts/profile/', profile, name='profile-create'),
    #path('accounts/signup/', signup, name='signup'),
    #path('accounts/signup/', signup, name='logout'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('about',about.about,name='about'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
