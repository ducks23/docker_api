from django.urls import path
from my_app.views import TodoView

urlpatterns = [
    path('todo', TodoView.as_view())
]