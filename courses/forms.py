from django import forms
from django.forms import TextInput,Textarea

from courses.models import Course

# class CourseCreateForm(forms.Form):
#     title=forms.CharField(label="Kurs basligi",required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
#     description=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields =('title','description','imageUrl','slug')
        labels={
            'title':"kurs basligi",
            'description': 'açıklama'
        }
        widgets={
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "imageUrl": TextInput(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),


        }
        error_messages = {
            "title": { 
                "required":"kurs başlığı girmelisiniz",
                "max_length":"maksimum 50 karakter girmelisiniz"
            },
            "description":{
                "required":"kurs açıklaması gereklidir."
            }
        }

