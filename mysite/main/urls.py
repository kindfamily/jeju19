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
from main.views import index, about, new, cafelist, cafedetails, cafeindex, cafe_update, cafe_delete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cafeindex),
    path('new/', new),
    path('cafelist/', cafelist),
    path('about/', about), # name을 안넣으면 <a href="/cafe/cafelist/{{i.pk}}" 요렇게 넣어야함
    path('cafelist/<int:pk>', cafedetails, name='cafe_list'),   # name을 넣으면 a 테그에 넣을때 <a href="{% url 'cafe_list' i.id %}"> 처럼 넣을수 있음
    path('edit/<int:pk>', cafe_update, name='cafe_edit'),
    path('delete/<int:pk>', cafe_delete, name='cafe_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)