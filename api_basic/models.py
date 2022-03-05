from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField('Name', max_length=100)
    age = models.PositiveIntegerField('Age')

    def __str__(self):
        return self.name

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()
#
#     def create(self, validate_data):
#         return Article.objects.create(validate_data)
#
#     def update(self, instance, validate_data):
#         instance.title = validate_data.get('title', instance.title)
#         instance.author = validate_data.get('author', instance.author)
#         instance.email = validate_data.get('email', instance.email)
#         instance.date = validate_data.get('date', instance.date)
#         instance.save()
#         return instance