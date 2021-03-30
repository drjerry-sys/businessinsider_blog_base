from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)

class SearchForm(forms.Form):
    search_inpt = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder':'Search for post'}))