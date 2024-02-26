from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('all_recipes/', views.all_recipes, name='all_recipes'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
