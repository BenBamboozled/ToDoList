from django.urls import path
from . import views
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView 

urlpatterns = [
    path('', ItemListView.as_view(), name='list-home'),
    path('task/<int:pk>/', ItemDetailView.as_view(), name='task-detail'),
    path('task/new/', ItemCreateView.as_view(), name='task-create'),
    path('task/create/', views.create, name='task-new'),
    path('task/<int:pk>/update/', ItemUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', ItemDeleteView.as_view(), name='task-delete'),
    path('task/delete/', views.deleteTask, name='task-delete2'),
    path('about/', views.about, name='about'),
    path('complete/<int:pk>/', views.complete, name='complete'),
    path('clear/', views.clearList, name='clear-list'),
    path('text-file/', views.getTextFile, name='get-txt'),

]

