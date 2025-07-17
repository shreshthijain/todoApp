from django import forms

class TodoItemForm(forms.Form):
    text = forms.CharField(max_length=200,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Add a new todo item...', 'aria-label':'Todo', 'aria-describedby':'add-btn'}
            )
        )
    # exclude = ['time']