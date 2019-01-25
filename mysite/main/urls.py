"""tutorialdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from main.views import index, about, write, cafelist, cafedetails, memberlist, faqlist, cafeindex
from main.views import index, about, write, cafelist, cafedetails, cafeindex
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cafeindex),
    path('write/', write),
    path('cafelist/', cafelist),    
    path('about/', about),
    path('cafelist/<int:pk>', cafedetails),   
    # path('faq/', faqlist),
    # path('memberlist/', memberlist),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)