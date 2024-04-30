from django import forms
from .models import Teams
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class TeamModelForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = "__all__"
        # fields = ('f_name','f_nickname')
        # exclude = ('f_logo',)

class TeamsForm(forms.Form):
    f_name = forms.CharField(max_length=30)
    f_nickname = forms.CharField(max_length=6)
    f_started_year = forms.IntegerField()
    f_trophies = forms.IntegerField()
    f_logo = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('f_name', css_class='form-group col-md-6 mb-0'),
                Column('f_nickname', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('f_started_year', css_class='form-group col-md-6 mb-0'),
                Column('f_trophies', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('f_logo', css_class='form-group col-md- mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Register')
        )