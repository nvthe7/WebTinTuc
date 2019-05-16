
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='homepage'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('category/<int:category_id>/', views.category, name='category'),

]
