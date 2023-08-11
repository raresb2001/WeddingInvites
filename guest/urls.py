from django.urls import path

from guest import views

urlpatterns = [
    path('create_guest/', views.GuestCreateView.as_view(), name='create-guest'),
    path('list_guest/', views.GuestListView.as_view(), name='list-guest'),
    path('update_guest/<int:pk>/', views.GuestUpdateView.as_view(), name='update-guest'),
    path('delete_guest/<int:pk>/', views.GuestDeleteView.as_view(), name='delete-guest'),

]