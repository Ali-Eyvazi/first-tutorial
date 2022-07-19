from django import forms
import datetime
from .models import ToDo

class Item_Creation_Form(forms.Form):


    # Modelform  mofrl=artivcle  Fields=[]
    title=forms.CharField(max_length=100)
    date_time=forms.DateTimeField(initial=datetime.datetime.now)
    Details=forms.CharField(max_length=1000,widget=forms.Textarea)



class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=ToDo   
        fields=['title','Details','date_time']    #=__all__
    
    
    
    