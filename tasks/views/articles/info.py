from django.views.generic import TemplateView


# Articles
class Productivity(TemplateView):
    template_name = "article/productivity.html"


class UseIt(TemplateView):
    template_name = "article/useit.html"


class GoodTask(TemplateView):
    template_name = "article/task.html"


# Legal Information
class ContactUs(TemplateView):
    template_name = "article/information/contact_us.html"


class Gdpr(TemplateView):
    template_name = "article/information/gdpr.html"


class PrivacyPolicy(TemplateView):
    template_name = "article/information/privacy_policy.html"


class TermsService(TemplateView):
    template_name = "article/information/terms_service.html"
