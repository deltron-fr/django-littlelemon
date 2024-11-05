from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name ="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('users/',views.UsersListView.as_view()),
    path('register/', views.UserRegistrationView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]