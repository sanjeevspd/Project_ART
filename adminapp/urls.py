from django.urls import path
from. import views

urlpatterns = [
    path("adminhome/",views.adminhome,name="adminhome"),
    path('uploadopt/', views.upload_photo, name='uploadopt'),
    path("adminlogout",views.logout,name="adminlogout"),
    path("feedbacks",views.feedbackpage,name="feedbacks")
    #path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
]
