from django.db import models

class Member(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    photo = models.ImageField(upload_to="Member/",blank=True,null=True,default="Member/default.png")
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(blank=True,null=True)
    join_date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add = True,blank=True,null=True)
    plan = models.ForeignKey("MembershipPlan", on_delete=models.SET_NULL,null=True,blank=True,related_name="members")
    trainers = models.ManyToManyField(
        "Trainer", blank=True,null=True, related_name="members"
    )
    
    def __str__(self):
        return self.name
    
class MembershipPlan(models.Model):
    plan_name = models.CharField(max_length=50)
    duration = models.IntegerField(help_text="Duration in days")
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.plan_name} ({self.duration} days ) (${self.fees}) "
    
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name



