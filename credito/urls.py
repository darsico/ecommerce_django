from django.urls import path
from . import views

urlpatterns = [
	path('credito/create/', views.PostPagosView.as_view()),
	path('credito/list/', views.GetPagosView.as_view()),
]