from django.forms import ModelForm
from .models import semestersModel

class semForm(ModelForm):
    class Meta:
        model = semestersModel
        fields = '__all__'

    def clean(self):
        super(semForm,self).clean()

        subject_title = self.cleaned_data.get('subject_title')
        subject_code = self.cleaned_data.get('subject_code')
        document = self.cleaned_data.get('document')
        subject_credits = self.cleaned_data.get('subject_credits')
        if(subject_credits) > 10:
            self._errors['subject_credits'] = self.error_class([
                'Maximum 10 allowed for a subject'
            ])
        if (len(subject_title)) < 5:
            self._errors['subject_title'] = self.error_class([
                'Minimum 5 characters required'
            ])
        return self.cleaned_data
