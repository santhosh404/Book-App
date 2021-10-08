from django.urls import path, include
from . import views


urlpatterns = [
    path('home/',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login, name='login'),
    path('addbooks/', views.add_books, name='addbooks'),
    path('update_event/<update_id>', views.update_event, name='update_event'),
    path('delete_event/<book_id>', views.delete_event, name='delete_event'),
    path('', views.logout, name='logout')
]