This repo is a toy django app to reproduce a problem with POSTing to create a
new resource with a related resource.

Successful request with tastypie 0.14.1
```
>>> h = {'content-type': 'application/json', 'accept': 'application/json'}
>>> d = {'name': 'some book', 'author': 1}
>>> r = requests.post('http://127.0.0.1:8000/api/v1/books/', data=json.dumps(d), headers=h)
>>> r.status_code
201
>>> r.headers
{'Date': 'Thu, 04 Aug 2022 20:18:12 GMT', 'Server': 'WSGIServer/0.2 CPython/3.6.9', 'Content-Type': 'text/html; charset=utf-8', 'Location': '/api/v1/books/2/', 'Vary': 'Accept', 'X-Frame-Options': 'SAMEORIGIN', 'Content-Length': '0'}
```

Failed request with tastypie 0.14.4
```
>>> d = {'name': 'another book', 'author': 1}
>>> r = requests.post('http://127.0.0.1:8000/api/v1/books/', data=json.dumps(d), headers=h)
>>> r.content
b'{"books": {"author": ["This field is required."]}}'
>>>
```
