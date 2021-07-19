import os, datetime, time, requests, json
import library.db_utils as db_utils
from bson.objectid import ObjectId

domain = 'user'
domain_role_permissions = 'role_permissions'

ONEAUTH_API_URL = os.environ.get('ONEAUTH_API_URL')
if ONEAUTH_API_URL is None:
    ONEAUTH_API_URL = 'http://localhost:4010/api'

def find(request, space_id):
    data = find_by_user_id(space_id, request.user_id)
    return (200, {'data': data})

def find_all(request, space_id):
    data = db_utils.find(space_id, domain, {})
    return (200, {'data': data})

def authorize_user(request, space_id):
    access_token = request.body['accessToken']
    refresh_token = request.body['refreshToken']
    access_token_response = _decode_access_token(access_token)
    if access_token_response != 'expired':
        return (200, {'accessToken': None, 'claims': access_token_response})
    get_new_access_token_response = _get_new_access_token(space_id, refresh_token)
    if get_new_access_token_response == None:
        return (200, {})
    new_access_token_response = _decode_access_token(get_new_access_token_response['access_token'])
    return (200, {'access_token': get_new_access_token_response['access_token'], 'claims': new_access_token_response})

def _decode_access_token(access_token):
    response = requests.get(ONEAUTH_API_URL + '/auth/token/decode', headers={'authorization': access_token})
    if response.status_code == 401:
        return "expired"
    if response.status_code == 200:
        return response.json()
    return None

def _get_new_access_token(space_id, refresh_token):
    response = requests.post(ONEAUTH_API_URL + '/auth/token', json={'grant_type': "refresh_token", 'realm': space_id, 'refresh_token': refresh_token})
    if response.status_code == 200:
        return response.json()
    return None

def expand_authors(space_id, data):
    for item in data:
        last_modified_by = db_utils.find(space_id, domain, {'_id': item.get('lastModifiedBy')})
        created_by = db_utils.find(space_id, domain, {'_id': item.get('createdBy')})
        item['lastModifiedByEmail'] = last_modified_by[0].get('email')
        item['createdByEmail'] = created_by[0].get('email')
    return data

def do_update_user(request, space_id):
    updated_record = update_user(space_id, request.body, request.user_id)
    return (200, {'data': updated_record})

def find_permitted_actions(space_id, user_id):
    roles = db_utils.find(space_id, domain, {'_id': user_id})[0].get('roles')
    roles.append('open')
    return db_utils.find(space_id, domain_role_permissions, {'role': {'$in': roles}})

def find_by_user_id(space_id, user_id):
    return db_utils.find(space_id, domain, {'_id': user_id})

def update_user(space_id, data, user_id=None):
    return db_utils.upsert(space_id, domain, data, user_id)

def insert_user(space_id, data, user_id=None):
    data['_id'] = ObjectId(data['_id'])
    return db_utils.insert(space_id, domain, data, user_id)

def is_first_user(space_id):
    data = db_utils.find(space_id, domain, {})
    if len(data) == 0:
        return True
    else:
        return False
