from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        return {'section': 'home'}


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        return {'section': 'about'}