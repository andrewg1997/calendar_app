from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name ='hello'),
    path('<month>/display/', views.display, name= 'display'),
    path('<month>/<int:year>', views.calendar_view, name= 'calendar_view'),
    path('add_new/<month>/<year>', views.add_new_view, name= 'add_new_view'),
    path('delete_old/<month>/<year>', views.delete_old_view, name= 'delete_old_view')
]