"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms_home, name='rooms_home'),  # Страница со всеми палатами
    path('<int:pk>', views.RoomsDetailView.as_view(), name='rooms-detail'),  # Страница с подробной информацией о палате
    path('<int:pk>/delete', views.RoomsDeleteView.as_view(), name='rooms-delete'),  # Удаление палаты
    path('<int:pk>/update', views.RoomsUpdateView.as_view(), name='rooms-update'), # Изменение палаты
    path('add', views.add, name='add')  # Добавление палаты

]
