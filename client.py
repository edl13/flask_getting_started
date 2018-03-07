import requests

url = 'http://vcm-3582.vm.duke.edu'

r = requests.get(url + '/name')
print(r.json())

r = requests.get(url + '/hello/Grayson_Allen')
print(r.json())

dis_dict = {'a': [13, 23], 'b': [12, -44]}
r = requests.post(url + '/distance', json=dis_dict)
print(r.json())
