from django.urls import path
from.views import add_show
from.views import delete_data
from.views import update_data



urlpatterns = [
    path('',add_show,name="addandshow"),
    path('delete/<int:id>',delete_data, name="deletedata"),
    path('<int:id>',update_data, name="updatedata")
]