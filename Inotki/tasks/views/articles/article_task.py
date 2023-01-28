from django.views.generic import TemplateView


class GoodTask(TemplateView):
    template_name = "article/task.html"
