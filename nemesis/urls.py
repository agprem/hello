from . import views
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('usersview',views.users_view,basename="usersview")


urlpatterns = [
     path('register/',views.register_view.as_view() ,name="register"),
     path('',include(router.urls) ,name="usersview"),
     path('login/',TokenObtainPairView.as_view(),name="Login_View"),
     path('refreshtoken/',TokenRefreshView.as_view() ,name="refreshtoken"),
     path('verifytoken/',TokenVerifyView.as_view(),name="verifytoken")
     
     
]
