from django.urls import path
from . import views

# import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("menu/", views.MenuItemView.as_view(), name="menuitem-list"),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view(), name="menuitem-detail"),
    # add following line in urlpatterns list
    path("api-token-auth/", obtain_auth_token),

]