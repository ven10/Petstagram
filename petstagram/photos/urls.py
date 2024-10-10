from django.urls import path, include
from petstagram.photos import views

urlpatterns = [
    path('add/', views.photo_add_page, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.photo_details_page, name='details-photo'),
        path('edit/', views.photo_edit_page, name='edit-photo'),
        ]),
    )
]

