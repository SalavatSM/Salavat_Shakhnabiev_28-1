"""
URL configuration for study_djangoProject_4month project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static


#from posts.views import hello_view, redirect_to_youtube_view, redirect_to_google, redirect_to_github, helloview, goodby, now_date, now_date_v2
from posts.views import main_page_view, posts_view, products_view, post_detail_view
from study_djangoProject_4month import settings

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('hello_v/', hello_view),
#     path('youtube/', redirect_to_youtube_view),
#     path('google/', redirect_to_google),
#     path('github/', redirect_to_github),
#     path('hello/', helloview),
#     path('goodby/', goodby),
#     path('now_date/', now_date),
#     path('now_date_2/', now_date_v2)
# ]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_page_view),
    path('posts/', posts_view),
    path('products/', products_view),
    path('posts/<int:id>/', post_detail_view),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)