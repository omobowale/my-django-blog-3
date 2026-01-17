from django import forms
from .models import Post


# Create, Read, Update, Delete (CRUD) forms for Post model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        
    # Add some more validations for title and content
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
        
# class ProductForm(forms.Form):
#     class Meta:
#         model = Product
#         fields = ['name', 'price', 'description', 'stock', 'category', 'image', 'sku', 'weight', 'dimensions', 'brand', 'rating', 'reviews', 'discount', 'availability', 'tags']
        

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['author', 'text']
        
        
        
