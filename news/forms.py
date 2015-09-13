from django  import forms
from .models import Articles
from django.forms import ModelForm
class UpdateArticle(ModelForm):
    email=forms.EmailField()
    heading=forms.CharField(Articles._meta.get_field('heading').max_length)
    article=forms.Textarea()
    author=forms.CharField(Articles._meta.get_field('author').max_length)
    def save(self,commit=True):
        instence=super(UpdateArticle,self).save(commit=False)
        if commit:
            instence.save(update_fields=['email','article','heading','heading'])
        return instence

    class Meta:
        model=Articles
        fields=('heading','email','author','article')
class CreateArticle(ModelForm):
    email=forms.EmailField()
    heading=forms.CharField(Articles._meta.get_field('heading').max_length)
    article=forms.Textarea()
    author=forms.CharField(Articles._meta.get_field('author').max_length)
    class Meta:
        model=Articles
        fields=('heading','email','author','article')
