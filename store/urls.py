from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login , logout

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),

]
