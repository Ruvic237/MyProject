
from django.urls import  path
from .views import *


urlpatterns = [

    path('', home, name='home'),
    path('about', about, name='about'),
    path('courseA', SubjectListView.as_view(), name='courseA'),
    path('CourseA/<slug:slug>', LessonDetailView.as_view(), name='less'),
    path('CourseA/<str:subject>/<slug:slug>', PerLessonDetailView.as_view(), name='per'),
    path('contact', contact, name='contact'),

]








