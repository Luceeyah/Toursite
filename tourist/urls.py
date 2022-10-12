from django.urls import path
from tourist import views



urlpatterns =[ 
    path('tourist', views.getTourist_place),
    path('tourist',views.getTouristPlacesbyUser),

    path('tourist/create/', views.tourist_place_create),

    path('tourist/<int:id>/', views.getTourDetail),

    path ('tourist/update/<int:id>/',views.tourist_places_update),

    path('tourist/delete/<int:id>/', views.delete_tour)

]
