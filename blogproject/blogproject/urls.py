"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jurnal.views import MusicListView, MusicDetailView, MusicCreateView, MusicUpdateView, register, login

# from django.contrib.auth import views as auth_views
# from django.urls import path
# from . import views
# from . import views_api


# app_name = 'account'

# urlpatterns = [

#     # Patterns using views

    
#     path('login/', views.login, name="login"),

#     path('register/', views.register, name='register'),
# white_check_mark
# eyes
# raised_hands



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('register/', register, name = "register"),
    # path('login/', login, name = "login"),
    path('account/',include('apps.accounts.urls',  namespace='accounts')),

    
    path("allmusic/", MusicListView.as_view(),name="list_view"),
    path("allmusic/<int:pk>/", MusicDetailView.as_view(),name="detail_view"),
    path("allmusic/newmusic/", MusicCreateView.as_view(),name="create_view"),
    path("allmusic/updatemusic<int:pk>/", MusicUpdateView.as_view(), name="update_view"),        
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
