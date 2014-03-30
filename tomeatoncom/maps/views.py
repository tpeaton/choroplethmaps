from django.views.generic.base import TemplateView


class ViewMaps(TemplateView):

    template_name = 'maps.html'

    def get_context_data(self, **kwargs):

        context = super(ViewMaps, self).get_context_data(**kwargs)

        extra_context = {
            'foo': 'bar',

        }
        context.update(extra_context)

        return context


class ViewHome(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super(ViewHome, self).get_context_data(**kwargs)

        extra_context = {
            'foo': 'bar',

        }
        context.update(extra_context)

        return context
