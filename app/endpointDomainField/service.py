import library.db_utils as db_utils

domain = 'endpoint.domain.field'


def find_fields_domainId(request, space_id, domainId):
    data = db_utils.find(space_id, domain, {'domainId': domainId})
    return (200, {'data': data})


def find_fields_by_domainId(space_id, domainId):
    data = db_utils.find(space_id, domain, {'domainId': domainId})
    return data


def find(request, space_id):
    fields = db_utils.find(space_id, domain, {})
    return (200, {'data': fields})


def update(space_id, data, domainId, user_id):
    field_list = []
    for item in data:
        item['domainId'] = domainId
        field_list.append(db_utils.upsert(space_id, domain, item, user_id))
    return field_list


def delete(request, space_id, id):
    result = db_utils.delete(space_id, domain, {'_id': id}, request.user_id)
    return (200, {'deleted_count': result.deleted_count})


def find_by_id(request, space_id, id):
    data = db_utils.find(space_id, domain, {'_id': id})
    return (200, {'data': data})
