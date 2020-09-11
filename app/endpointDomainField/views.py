from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
import app.endpointDomainField.service as service
import library.db_utils as db_utils


@api_view(['GET'])
def get_fields_domainId(request, space_id, domainId):
    if request.method == 'GET':
        response = service.find_fields_domainId(request, space_id, domainId)
        return JsonResponse(response[1], status=response[0])
