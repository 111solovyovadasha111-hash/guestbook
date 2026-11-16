from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["author", "text"]

    def clean_author(self):
        author = self.cleaned_data.get("author", "").strip()
        if not author:
            raise forms.ValidationError("имя автора не должно быть пустым")
        return author

    def clean_text(self):
        text = self.cleaned_data.get("text", "").strip()
        if not text:
            raise forms.ValidationError("текст не должен быть пустым")
        return text