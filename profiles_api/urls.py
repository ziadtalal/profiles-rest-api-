from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewsets', views.HelloViewsets, base_name='hello-viewsets')
router.register('profile',views.UserProfileViewSet)


urlpatterns=[
    path('Hello-View/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
