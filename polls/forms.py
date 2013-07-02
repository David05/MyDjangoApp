from django import forms

class ClienteForm(forms.Form):
    Email   = forms.EmailField(widget=forms.TextInput())
    Titulo  = forms.CharField(widget=forms.TextInput())
    Texto   = forms.CharField(widget=forms.Textarea())

class addProductos(forms.Form):
    nombre  = forms.CharField(widget=forms.TextInput)
    descripcion = forms.CharField(widget=forms.Textarea)

    def clean (self):
        return self.cleaned_data
