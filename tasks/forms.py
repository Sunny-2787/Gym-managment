from django import forms
from tasks.models import Member, MembershipPlan, Trainer


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','age','gender', 'plan','trainers' ,'phone','email','address' ,'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Full Name'}),
            'age': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
            'plan': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
            'trainers': forms.CheckboxSelectMultiple(attrs={'class': 'border rounded p-2 w-full'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'border rounded p-2 w-full','accept': 'image/*','capture': 'camera'}),
            'phone': forms.TextInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Phone Number'}),
            'address': forms.Textarea(attrs={'class': 'border rounded p-2 w-full', 'rows': 3, 'placeholder': 'Address'}),
            

        }


class PlanForm(forms.ModelForm):
    class Meta:
        model = MembershipPlan
        fields = "__all__"  # Includes: plan_name, duration, fees
        widgets = {
            'plan_name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Plan Name'}),
            'duration': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Duration in Days'}),
            'fees': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Fees'}),
        }



class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"  # Includes: name, specialty, phone
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Trainer Name'}),
            'specialty': forms.TextInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Specialty'}),
            'phone': forms.TextInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Phone Number'}),
        }



