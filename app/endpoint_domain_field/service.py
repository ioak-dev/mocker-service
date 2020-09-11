import library.db_utils as db_utils

domain = 'endpoint.domain.field'


def find_fields_domain_id(request, space_id, domain_id):
    data = db_utils.find(space_id, domain, {'domain_id': domain_id})
    return 200, {'data': data}


def find_fields_by_domain_id(space_id, domain_id):
    data = db_utils.find(space_id, domain, {'domain_id': domain_id})
    return data


def find(request, space_id):
    fields = db_utils.find(space_id, domain, {})
    return 200, {'data': fields}


def update(space_id, data, domain_id, user_id):
    field_list = []
    for item in data:
        item['domain_id'] = domain_id
        field_list.append(db_utils.upsert(space_id, domain, item, user_id))
    return field_list


def delete(request, space_id, id):
    result = db_utils.delete(space_id, domain, {'_id': id}, request.user_id)
    return 200, {'deleted_count': result.deleted_count}


def delete_by_domain_id(space_id, domain_id, user_id):
    result = db_utils.delete(space_id, domain, {'domain_id': domain_id}, user_id)
    return 200, {'deleted_count': result.deleted_count}


def find_by_id(request, space_id, id):
    data = db_utils.find(space_id, domain, {'_id': id})
    return 200, {'data': data}
