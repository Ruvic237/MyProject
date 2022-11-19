from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .form import *


# Home page View
def home(request):
    return render(request, 'home.html', {})


# About page View
def about(request):
    return render(request, 'about.html', {})


# Course page View
class SubjectListView(ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'GCE_A.html'


# Lesson page View
class LessonDetailView(DetailView):
    model = Subject
    context_object_name = 'lessons'
    template_name = 'lessons.html'


# Lesson Summary page View
class PerLessonDetailView(DetailView, FormView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'lesson.html'
    form_class = CommentForm
    second_form_class = ResponseForm

    # method to insert an object in the context dictionary
    def get_context_data(self, **kwargs):
        context = super(PerLessonDetailView, self).get_context_data(**kwargs)

        # check if comment form is in context dictionary if not store it
        if 'form' not in context:
            context['form'] = self.form_class

        # check if response form is in context dictionary  if not store it
        if 'form2' not in context:
            context['form2'] = self.second_form_class

        # returning context dictionary
        return context

    # method to check comment form validity
    def form_valid(self, form):
        self.object = self.get_object()

        # collect the form but do not yet store in database
        fd = form.save(commit=False)

        fd.author = self.request.user
        fd.lesson_id = self.object.id
        fd.save()
        return HttpResponseRedirect(self.get_success_url())

    # method to check comment form validity
    def form_valid2(self, form):
        self.object = self.get_object()

        # collect the form but do not yet store in database
        fd = form.save(commit=False)
        fd.author = self.request.user
        fd.comment_name_id = self.request.POST.get('comment.id')
        fd.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        self.object = self.get_object()
        subject = self.object.subject_name.slug
        return reverse_lazy('per', kwargs={'subject': subject, 'slug': self.object.slug})

    # method to determine which form was submitted
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        # checking if it is comment submitted
        if 'form' in request.POST:
            form_class = self.form_class
            form_name = 'form'

        # checking if it is response submitted
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        # collecting submitted form and storing in (form)
        form = self.get_form(form_class)

        # checking if form submitted is comment and if it is valid
        if form_name == 'form' and form.is_valid():
            return self.form_valid(form)

        # checking if form submitted is response and if it is valid
        if form_name == 'form2' and form.is_valid():
            return self.form_valid2(form)


# Contact page View
def contact(request):

    # checking if the form is submitted
    if request.method == 'POST':
         forms = ContactsForm(request.POST)

         if forms.is_valid:
            subject = "website inquiry"
            body = {
                'name': request.POST['Name'],
                'message': request.POST['Comment'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, body['message'], ['bambavarnes@gmail.com'])

            except BadHeaderError:
                return HttpResponse('Invalid header')

            return redirect(home)
    forms = ContactsForm()
    context = {'forms': forms}
    return render(request, 'contact.html', context)

