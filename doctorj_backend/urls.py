from django.contrib import admin
from django.urls import path, include
from doctorj_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('doctorj_app.urls')),  # 包含应用的URL
    path('', views.index, name='index'),
    path('intro/', views.intro, name='intro'),
]
