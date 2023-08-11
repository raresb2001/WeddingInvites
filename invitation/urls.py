from django.urls import path

from invitation import views

urlpatterns = [
    path('create_invitation/', views.InvitationCreateView.as_view(), name='create_invitation'),
    path('list_invitation/', views.InvitationListView.as_view(), name='list-invitation'),
    path('update_invitation/<int:pk>/', views.InvitationUpdateView.as_view(), name='update-invitation'),
    path('delete_invitation/<int:pk>/', views.InvitationDeleteView.as_view(), name='delete-invitation'),
    path('details_invitation/<int:pk>/', views.InvitationDetailView.as_view(), name='details-invitation'),
]