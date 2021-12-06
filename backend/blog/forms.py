from django import forms
from blog.models import Author, Category, Comment, Post
from ckeditor.widgets import CKEditorWidget

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content', 'email', )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Blog post title'}))
    content = forms.CharField(widget=CKEditorWidget())

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['thumbnail'].label = "Upload image (formats .png, .jpeg, jpg)"
        self.fields['categories'].label = "Select blog post categories"

    class Meta:
        model = Post
        fields = '__all__' 
        exclude = ['author', 'slug', 'status'] 


# class BookingForm(forms.ModelForm):
#     arrival_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select')
#     # title = forms.CharField(initial = "Method 2 ")

#     # caption = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Caption uploaded image'}))

#     def __init__(self, *args, **kwargs):
#         super(BookingForm, self).__init__(*args, **kwargs)
#         # self.fields['picture'].label = "Upload image (formats .png, .jpeg, jpg)"
#     class Meta:
#         model = Booking
#         fields = '__all__'
#         exclude = ('time_booked',)


    