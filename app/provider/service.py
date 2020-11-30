import os, datetime, time, random
import library.db_utils as db_utils
import app.sequence.service as sequence_service
import app.role.service as role_service
import app.endpoint.service as endpoint_service
import app.project.service as project_service
from bson.objectid import ObjectId
import app.provider.data_generator as data_generator

def get_domain(request, space_id, project_reference, domain_name):
    project = project_service.get_by_reference(space_id, project_reference)
    if project is None:
        return (404, {"message": "Project not found"})
    endpoint_config = endpoint_service.get_by_project_and_endpoint_ref(space_id, project['_id'], domain_name)
    if endpoint_config is None:
        return (404, {"message": "No endpoint domains found"})
    out = [data_generator.traverse(endpoint_config["structure"], None, i) for i in range(0, random.randint(1,10))]
    return (200, out)

def get_domain_by_id(request, space_id, project_reference, domain_name, id):
    project = project_service.get_by_reference(space_id, project_reference)
    if project is None:
        return (404, {"message": "Project not found"})
    endpoint_config = endpoint_service.get_by_project_and_endpoint_ref(space_id, project['_id'], domain_name)
    if endpoint_config is None:
        return (404, {"message": "No endpoint domains found"})
    out = data_generator.traverse_with_known_primary_key(endpoint_config["structure"], None, 0, endpoint_config['key'], id)
    return (200, out)

def actions_for_custom_endpoint(request, space_id, project_reference, endpoint_name, method):
    project = project_service.get_by_reference(space_id, project_reference)
    if project is None:
        return (404, {"message": "Project not found"})
    endpoint_config = endpoint_service.get_by_project_and_endpoint_ref(space_id, project['_id'], endpoint_name)
    if endpoint_config is None:
        return (404, {"message": "No endpoint domains found"})
    if endpoint_config['method'] != method:
        return (405, {"message": "Method not supported"})
    if endpoint_config['responseType'] == 'Object':
        out = data_generator.traverse(endpoint_config["response"], None, 0)
    elif endpoint_config['responseType'] == 'Array':
        out = [data_generator.traverse(endpoint_config["response"], None, i) for i in range(0, random.randint(1,10))]
    else:
        out = None
    return (200, out)
