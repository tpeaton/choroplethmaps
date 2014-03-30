from django.views.generic.base import TemplateView


class ViewMaps(TemplateView):

    template_name = 'maps.html'

    def get_context_data(self, **kwargs):
        """Call methods and send metrics to context variable."""

        context = super(ViewMaps, self).get_context_data(**kwargs)

        extra_context = {
            'foo': 'bar',

        }

        context.update(extra_context)

        return context
