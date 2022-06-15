from django import forms
from smallclient.models import SmallClient
from datetime import date
from django.core.exceptions import ValidationError
# from django.forms.utils import ErrorList

today = date.today()

"""Creating a modelform to handle the fields"""
class ClientForm(forms.ModelForm):
    class Meta:
        model = SmallClient
        fields = ['name', 'website', 'point_of_contact','goal_choices',
                 'due_date','profile_pic'] 
    due_date = forms.DateField(widget=forms.TextInput(attrs={'min': today, 'value': "Set Due Date", 'type': 'date'}), required=True)       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder':'Name'})
        self.fields['website'].widget.attrs.update({'class':'form-control','placeholder':'Website'})
        self.fields['profile_pic'].widget.attrs.update({'id':'file-search','onchange':'showPreview(event)'})
        self.fields['goal_choices'].widget.attrs.update({'class':'form-control','placeholder':'Goal Choices'})
        self.fields['due_date'].widget.attrs.update({'class':'form-control','id':'picker','placeholder':'Choose Due Date'})
        self.fields['point_of_contact'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
        self.fields['name'].label = ""
        self.fields['website'].label = ""
        self.fields['point_of_contact'].label = ""
        self.fields['goal_choices'].label = ""
        self.fields['due_date'].label = "Set Due Date"
        self.fields['profile_pic'].label = ""



    
    def clean(self):
        super(ClientForm, self).clean()
        username = self.cleaned_data.get('name')
        email = self.cleaned_data.get('point_of_contact')
        due_date = self.cleaned_data.get('due_date')
        goal = self.cleaned_data.get('goal_choices')
 
        # conditions to be met for the username length
        if len(username) < 3:
            self._errors['username'] = self.error_class([
                'Minimum 3 characters required'])
            self.fields['name'].widget.attrs.update({'class': 'form-control form_error'})

        ## check if email exists
        if SmallClient.objects.filter(point_of_contact = email):
            self._errors['point_of_contact'] = self.error_class([
                'Email is already registered'])
            self.fields['point_of_contact'].widget.attrs.update({'class': 'form-control form_error'})

        if due_date <= today:
            self._errors['due_date'] = self.error_class([
                'Pick a valid date in the future'])
            self.fields['due_date'].widget.attrs.update({'class': 'form-control form_error'})
        
        if not goal or len(goal) < 2:
            self._errors['goal_choices'] = self.error_class([
                'Pick a valid date in the future'])
            self.fields['goal_choices'].widget.attrs.update({'class': 'form-control form_error'})
