from .models import *
from django import forms

class StaffRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Staff
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(StaffRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['staff_id'].widget.attrs.update({'class': 'px-4 py-3 rounded-full border'})


