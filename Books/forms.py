from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields=['Photo','Book_Name','ISBN_NBR','PUB_NAME','Author_Name','Book_Desc','Status','Rating','Category']
        widgets = {
          'Rating':forms.Select,'Status':forms.Select
        }
    
    
