from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('all_games/', views.all_games, name='all_games'),
    path('all_guides/', views.all_guides, name='all_guides'),
    path('my_guides/', views.my_guides, name='my_guides'),
    path('my_guides/create/', views.create, name='create'),
    path('all_games/guides_by_category/<slug:slug>/', views.guides_by_cat, name='guides_by_cat'),
    path('all_games/guides_by_category/guide_description/<int:pk>', views.guide_desc, name='guide_desc'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login_view'),
    path('logout_action/', views.logout_action, name='logout_action'),
    path('sorry/', views.sorry, name='sorry'),
    path('my_guides/delete/<int:pk>/', views.delete_guide, name='delete_guide')
]