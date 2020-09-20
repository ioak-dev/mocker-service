from django.http import JsonResponse
from rest_framework.decorators import api_view
import app.endpoint_domain_field.service as service


@api_view(['GET'])
def get_fields_domain_id(request, space_id, domain_id):
    if request.method == 'GET':
        response = service.find_fields_domain_id(request, space_id, domain_id)
        return JsonResponse(response[1], status=response[0])
