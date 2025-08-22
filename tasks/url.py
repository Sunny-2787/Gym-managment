from django.urls import path,include
from tasks.views import  home,home2,home3,home4,home5,M_update,M_Delet,Planform,UpdatePlanform,DeletPlanform,TrainerForms,TrainerUpdate,Delettrainerform
urlpatterns = [
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









    
]
