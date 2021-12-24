from django.urls import path

from . import views

app_name = 'single_page'
urlpatterns = [
    path('', views.single_page_view, name='single_page'),
    path('<search>/', views.single_page_view, name='single_page_search'),
    path('delete/<secret_token>/',
         views.delete_listing_view,
         name='delete_listing_page')

]
