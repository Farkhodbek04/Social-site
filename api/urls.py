from django.urls import path, include
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register(r'my-model', views.MyModelView, basename='MyModel')


# urlpatterns = [
#     path('router/', include(router.urls)),
#     path('auth/', include('rest_framework.urls')),
#     # path('', views.list_data)
# ]

urlpatterns = [
    # User
    path('register/', views.UserRegistrationAPIview.as_view()),
    path('login/', views.LoginUserAPIview.as_view()),
    path('update-profile/', views.UpdateUserAPIview.as_view()),
    path('search-users/', views.SearchUsersAPIview.as_view()),
    path('delete-profile/', views.DeleteUserAPIview.as_view()),
]