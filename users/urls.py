"""User views"""

# Django
from django.urls import path

# Views
from users import views


urlpatterns = [
    # Esta sera la primera class-based view, el perfil de usuario
    
    # Management
    path(
        route='login/', 
        view=views.LoginView.as_view(), 
        name='login'
    ),
    
    path(
        route='logout/', 
        view=views.LogoutView.as_view(), 
        name='logout'
    ),
    
    path(
        route='signup/', 
        view=views.SignupView.as_view(), 
        name='signup'
    ),
 
    path(
        route='me/update_profile/', 
        view=views.UpdateProfileView.as_view(), 
        name='update_profile'
    ),

    # Posts
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]