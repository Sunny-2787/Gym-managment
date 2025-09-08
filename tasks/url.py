from django.urls import path
from django.contrib.auth import views as auth_views
from tasks.views import  home,home2,home3,home4,home5,M_update,M_Delet,Planform,UpdatePlanform,DeletPlanform,TrainerForms,TrainerUpdate,Delettrainerform,reset_admin_password,create_admin_user,payment_create,member_details

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    path('', home,name="home"),
    path('home/', home,name="home"),
    path('Member/', home2,name="member_list"),
    path('Member/from/', home3,name="MemberForm"),
    path('Plans/from/', Planform,name="planForm"),
    path('plan_list/', home4,name="plan_list"),
    path('Trainer_list/', home5,name="Trainer_list"),
    path('Trainer/form/', TrainerForms,name="TrainerForm"),

    path('Member/update/<int:id>/', M_update,name="update"),
    path('Member/Delet/<int:id>/', M_Delet,name="delet"),
 
    path('Plans/update/<int:id>/',UpdatePlanform,name="update1"),
    path('Plans/delet/<int:id>/',DeletPlanform,name="delet2"),

    path('Trainer/update/<int:id>/',TrainerUpdate,name="update2"),
    path('Trainer/delet/<int:id>/',Delettrainerform,name="delet3"),

    path('reset-admin/', reset_admin_password, name="reset_admin"),
    path("create-admin/", create_admin_user, name="create_admin"),


    path("payment/<int:member_id>/", payment_create, name="payment_create"),

    path("member_details/<int:id>/", member_details, name="member_details"),




    









    
]
