from django.http import JsonResponse
from django.views.generic import TemplateView


class JSONResponseMixin:
    ''' Mixin used to render a JSON Response (from the DJANGO Docs) '''

    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context),
            **response_kwargs,
            safe=False
        )

    def get_data(self, context):
        return {'error': {'problem': 'NotImplementedError', 'solution': 'You need to overwrite the get_data method in order to return data from the JSONView'}}


class JSONView(JSONResponseMixin, TemplateView):
    ''' Custom JSON View from the DJANGO docs '''

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
