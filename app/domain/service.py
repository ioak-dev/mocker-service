import library.db_utils as db_utils
import app.project.service as project_service

domain = 'domain'


def find(request, space_id):
    find_all_domains(space_id)
    domains = db_utils.find(space_id, domain, {})

    return 200, {'data': domains}


def update(request, space_id, data):

    if '_id' not in data:
        if 'projectId' not in data:
            return 406, {'data': 'Please provide Project ID'}  #send error message
        else:
            result_project = project_service.find_by_id(request, space_id, data['projectId'])
            if result_project is None:
                return 406, {'data': 'Please provide a valid project ID'}  # send error message
            else:
                updated_record = db_utils.upsert(space_id, domain, data, '')
                return 200, {'data': updated_record}

    return 200, {'data': 'updated_record'}


def delete(request, space_id, id):
    result = db_utils.delete(space_id, domain, {'_id': id}, request.user_id)
    return 200, {'deleted_count': result.deleted_count}


def find_by_id(request, space_id, id):
    data = db_utils.find(space_id, domain, {'_id': id})
    return 200, {'data': data}


# TBD deprecated should be removed
def find_all_domains(space_id):
    return db_utils.find(space_id, domain, {})