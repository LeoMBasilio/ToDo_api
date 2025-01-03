from taskList.views import Task_View_Set
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

routers = routers.DefaultRouter()
routers.register('task', Task_View_Set, basename='task')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(routers.urls)),
]
