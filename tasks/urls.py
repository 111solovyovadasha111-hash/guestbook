from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.review_list, name="review_list"),
    # path("tasks/<int:task_id>/toggle/", views.task_toggle, name="task_toggle"),
    # path("api/tasks/", views.task_api, name="task_api"),
    # path("<int:task_id>/", views.task_id_details, name="task_id_details"),
    # path("<int:task_id>/delete/", views.delete_task, name="delete_task")
]
