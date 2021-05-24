from django.urls import path
from . import views


app_name = "main"

urlpatterns=[

    
    path('/create',views.create,name="create"),
    path('detail/<int:write_id>',views.detail,name="detail"),
    path('update/<int:write_id>',views.update,name="update"),
    path('delete/<int:write_id>',views.delete, name="delete"),
    path('create_comment/<int:write_id>',views.create_comment,name="create_comment"),
    path('delete_comment/<int:write_id>/<int:comment_id>',views.delete_comment,name="delete_comment"),

]