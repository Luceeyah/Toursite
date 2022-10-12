from django.urls import path
from .views import CustomUserCreate, CustomUserLogin,BlacklistTokenView



app_name ='user'

urlpatterns =[
    path('register/',CustomUserCreate.as_view(),name= 'create_user'),
    path('login/',CustomUserLogin.as_view(), name ='login'),
    path('logout/blacklist', BlacklistTokenView.as_view(), name= 'logout')
]