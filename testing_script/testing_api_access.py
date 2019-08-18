import requests
import json
import os

BASE_URL = 'http://localhost:8000/'
API_ENDPOINT = 'api/status/'
image_path = os.path.join(os.getcwd(), 'resized_flyer.png')

def get_data():
    data = requests.get(url=(BASE_URL + API_ENDPOINT))
    print(data)
    print('json----', data.json())
    # data = data.json()
    # print(data)
    # for obj in data:
    #     print(obj)
    #
    # for obj in data:
    #     print(obj['id'])

def post_data():
    new_data = {
        'content': ''
    }
    r = requests.delete(url=(BASE_URL+API_ENDPOINT + str(5) + '/'))
    # r = requests.post(url=(BASE_URL + API_ENDPOINT), data=new_data)
    print(r)
    print(r.status_code)
    print(r.json())


# url = f'http://localhost:8000/api/status/?id={7}'
# url = f'http://localhost:8000/api/status/'

# ?id={str(1)}
def req(method='get', data={}, id=1, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
        print(type(data))
    print(headers)
    r = requests.request(method=method, url=url, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    print('----------------')




# req(method='put', data={'id':14, 'user': 1, 'content':'testing form script'})

# req(data={'id':14})
# req(method='delete', data={'id':10})
# req_img(method='put', id=21, data={'user': 1, 'content': ''}, is_json=False, image_path=image_path)

REFRESH_ENDPOINT = BASE_URL + API_ENDPOINT + 'token-refresh/'

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNSwidXNlcm5hbWUiOiJraGtveWFuaTE1IiwiZXhwIjoxNTY2MTEwNzY0LCJlbWFpbCI6Imtoa295YW5pMTVAZ21haWwuY29tIiwib3JpZ19pYXQiOjE1NjYxMTA0NjR9.OwKU-nu-Pv7I2OIpNXrd_yTpCLbt2pffp77O-1IXYTA'
def get_token(username='khkoyani15', password='Shreeji323', refresh=False, token=None):
    data = {'username': username, 'password': password, 'password2': password,
            'email': 'khkoyani15@gmail.com'}

    AUTH_ENDPOINT = BASE_URL + 'api/auth/'
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = 'JWT ' + str(token)
        data = {'token': str(token)}
        r = requests.request(method='post', url=AUTH_ENDPOINT,
                             data=json.dumps(data), headers=headers)
    else:
        r = requests.request(method='post', url=AUTH_ENDPOINT,
                             data=json.dumps(data), headers=headers)
    # print(r.json())
    print('------------------------------')
    # print(r.json()['token_response']['token'])

    return r.json()['token']

# token = get_token()
# get_token()

# refresh = get_token(refresh=True, token=token)

def req_img(method='get', data={}, id=None, is_json=True, image_path=None):
    headers = {'Authorization': 'JWT ' + str(get_token())}
    endpoint = 'http://localhost:8000/api/status/'
    url = endpoint if id is None else f'{endpoint}{str(id)}/'

    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)

    if image_path:
        with open(image_path, mode='rb') as image:
            files = {'image': image}
            r = requests.request(method=method, url=url, data=data, files=files, headers=headers)
    else:
        r = requests.request(method=method, url=url, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    print('----------------')
#
# req_img(method='put', id=1, data={'content':'permissions testing tokens put data'},
#         is_json=False)

# req_img(method='post', data={'user': '4', 'content':'permissions testing tokens POST data'},
#         image_path=image_path, is_json=False)

req_img(method='get', id=1, is_json=False)