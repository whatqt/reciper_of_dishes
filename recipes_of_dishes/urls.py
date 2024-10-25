from rest_framework import routers
from django.urls import path, include



router = routers.DefaultRouter()


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]