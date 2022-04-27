from unicodedata import name
from django.urls import path
from .views import dashBoard, homePageView, loginUnity, loginView, logout_user, private_page, dashBoard, signUpView, change, registerUnity, consultUnity, getInfo, updateInfo, deleteUser, createNewUser

urlpatterns = [
    path('', homePageView, name="home"),
    path('login/', loginView, name="login"),
    path('loginUnity/', loginUnity, name="loginUnity"),
    path('changeUnity/', change, name="changeUnity"),
    path('registerUnity/', registerUnity, name="registerUnity"),
    path('consultUnity/', consultUnity, name="consultUnity"),
    path('signup/', signUpView, name="signup"),
    path('dashBoard/', dashBoard, name="dashBoard"),
    path('logout/', logout_user, name="logout"),
    path('APIs/', private_page, name="APIs_pages"),
    path('getInfo/', getInfo, name="GET"),
    path('updateInfo/', updateInfo, name="UPDATE"),
    path('createUser/', createNewUser, name="CREATE"),
    path('deleteUser/', deleteUser, name="DELETE")
]