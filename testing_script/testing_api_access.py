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
url = f'http://localhost:8000/api/status/'

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

def req_img(method='get', data={}, id=1, is_json=True, image_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)

    if image_path:
        print(image_path)
        with open(image_path, mode='rb') as image:
            files = {'image': image}
            r = requests.request(method=method, url=url, data=data, files=files)
    else:
        r = requests.request(method=method, url=url, data=data, headers=headers)
    print(headers)
    print(r.text)
    print(r.status_code)
    print('----------------')


# req(method='put', data={'id':14, 'user': 1, 'content':'testing form script'})
# req(method='post', data={'user': 1, 'content':'testing form script post data'})
# req(data={'id':14})
# req(method='delete', data={'id':10})
req_img(method='put', data={'id': 20, 'user': 1, 'content': ''}, is_json=False, image_path=image_path)