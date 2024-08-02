from django import  forms
from .models import ClientInfo


class ClientInfoForm(forms.ModelForm):
    class Meta:
        model = ClientInfo
        fields = "__all__"