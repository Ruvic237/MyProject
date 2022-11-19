from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.text import slugify


class Contact_Form(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Comment = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.Name}--Message'


class Subject(models.Model):
    subject_id = models.CharField(unique=True, max_length=100)
    subject_name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(null=True, blank=True)
    teacher_name = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date_creation = models.DateField(auto_now_add=True)
    subject_description = models.TextField(max_length=300, null=False)
    subject_image = models.ImageField(upload_to='base/subject_img', null=False)

    def __str__(self):
        return self.subject_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_name)
        super().save(*args, **kwargs)


class Lesson(models.Model):
    lesson_id = models.CharField(unique=True, max_length=100)
    lesson_name = models.CharField(max_length=100, null=False)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False, related_name='relate')
    slug = models.SlugField(null=True, blank=True)
    date_creation = models.DateField(auto_now_add=True)
    position = models.PositiveSmallIntegerField(verbose_name='lesson num')
    lesson_image = models.ImageField(upload_to='base/lesson_img', null=False)
    video = models.FileField(upload_to='base/videos', null=False)
    video_text = models.FileField(upload_to='base/PDF_course', null=False)

    def __str__(self):
        return self.lesson_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.lesson_name)
        super().save(*args, **kwargs)


class Comments(models.Model):
    lesson = models.ForeignKey(Lesson, null=True, on_delete=models.CASCADE, related_name='comm')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_name = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(max_length=500, blank=True, null=True)
    comment_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return 'The comment was written by {} at {}'.format(self.author, self.comment_date)


class Responses(models.Model):
    comment_name = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='resp')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500, blank=True, null=True)
    response_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'The response was written by {} at {} for {}'.format(self.author,self.response_date,self.comment_name)







