from django import forms
from django.forms import ModelForm, Textarea,TextInput,ChoiceField
from jobs.models  import Job

class JobForm(ModelForm):
		class Meta:
			model = Job
			fields = ['title','industry','location','availability','description','requirements', 'benefits']
			widgets = {
			'title': TextInput(attrs={'class': 'form-control','placeholder':"Job Title"}),
			'industry': forms.Select(attrs={'class': 'form-control'}),
			'location': TextInput(attrs={'class': 'form-control','placeholder':"Region, city or zip code"}),
			'availability': forms.Select(attrs={'class': 'form-control'}),
			'description': Textarea(attrs={'class': 'form-control','cols': 3, 'rows': 5,'placeholder':"Enter the job description here; include key areas of responsibility and what the candidate might do on a typical day"}),
			'requirements': Textarea(attrs={'class': 'form-control','cols': 3, 'rows': 5,'placeholder':"job requirements"}),
			'benefits': Textarea(attrs={'class': 'form-control','cols': 4, 'rows': 5,'placeholder':"benefits"}),
			}