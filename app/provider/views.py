from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
import app.provider.service as service

@api_view(['GET'])
def domain_endpoint(request, space_id, project_reference, domain_name):
    if request.method == 'GET':
        response = service.domain_endpoint_get(request, space_id, project_reference, domain_name)
        return JsonResponse(response[1], status=response[0])
