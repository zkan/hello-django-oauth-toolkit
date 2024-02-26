import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class CourseView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        response_data = {
            "status": "success",
            "courses": [
                {
                    "name": "Airflow",
                },
                {
                    "name": "dbt"
                },
            ],
        }
        return JsonResponse(response_data)

    def post(self, request):
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        print(body)

        response_data = {
            "status": "success",
        }
        return JsonResponse(response_data)
