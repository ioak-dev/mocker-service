from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from app.endpointDomain import service


@api_view(['GET'])
def get_endpoint_domain(request, space_id, projectId):
    if request.method == 'GET':
        response = service.find_by_project_id(request, space_id, projectId)
        return JsonResponse(response[1], status=response[0])


@api_view(['PUT'])
def update_endpoint_domain(request, space_id):
    if request.method == 'PUT':
        response = service.update(request, space_id, request.body)
        return JsonResponse(response[1], status=response[0])


@api_view(['DELETE'])
def delete_endpoint_domain(request, space_id, id):
    if request.method == 'DELETE':
        response = service.delete(request, space_id, id)
        return JsonResponse(response[1], status=response[0])
