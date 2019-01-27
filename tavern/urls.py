from django.urls import path

from . import views

app_name = 'tavern'

urlpatterns = [
    # This is the route for the home page
    path('', views.Home.as_view(), name='home'),

    # This route includes value capturing to grab the contest id as the pk variable
    # Example: localhost:8000/5/ <-- The # 5 is saved to a variable pk that we
    # can use in the view.
    path('<int:pk>/', views.Details.as_view(), name='detail'),

    # This route includes value capturing to grab the contest id as the pk variable
    path('<int:pk>/results/', views.Results.as_view(), name='results'),

    # This route includes value capturing to grab the contest id as the pk variable
    path('<int:pk>/vote/', views.Vote.as_view(), name='vote'),
]
