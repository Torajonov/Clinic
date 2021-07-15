from django.urls import path
from .import views



app_name = 'medic'

urlpatterns = [
	path('',views.HomeView.as_view(), name='index'),
	path('search_index/', views.search, name='search'),

]	