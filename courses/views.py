from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import CourseModel
from .forms import CourseCreateForm
# Create your views here.


class CourseView(View):
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(CourseModel, id=id)
            context['object'] = obj
            return render(request, 'courses/course_detail.html', context)

        context['object'] = CourseModel.objects.all()
        return render(request, 'courses/course_list.html', context)


class CourseCreateView(View):
    def get(self, request):
        form = CourseCreateForm()
        context = {'form': form}

        return render(request, 'courses/course_create.html', context)

    def post(self, request):
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseCreateForm()
        context = {'form': form}
        return render(request, 'courses/course_create.html', context)


class CourseDeleteView(View):
    template_name = "courses/course_delete.html"  # DetailView

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(CourseModel, id=id)
        return obj

    def get(self, request, id=None):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)


# def course_list_view(request):
#     obj = CourseModel.objects.all()
#
#     context = {'object': obj}
#     return render(request, 'courses/course_list.html', context)

