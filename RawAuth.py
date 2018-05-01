import requests


requests.packages.urllib3.disable_warnings()

login = requests.post('https://10.1.10.144/login', verify=False,data={'username': 'admin', 'password': 'avi@@123'})
login.raise_for_status()
#print(login.json())
#print(login.cookies['csrftoken'])
head = {'X-CSRFToken': login.cookies['csrftoken'], 'Referer': 'https://10.1.10.144', 'X-Avi-Version': '17.2.9'}


#Pool Create Data
data = {u'lb_algorithm': u'LB_ALGORITHM_LEAST_CONNECTIONS', "health_monitor_refs" : ["https://10.1.10.144/api/healthmonitor/healthmonitor-02b993d9-fd9f-4166-9381-10953841947b#System-TCP"], u'default_server_port': 80, u'name': 'Py-Pool', u'servers': [{u'ip': {u'type': u'V4', u'addr': '10.1.10.100'}}]}

#here u do the request u want
resp = requests.post('https://10.1.10.144/api/pool', verify=False, json=data, headers=head, cookies=login.cookies)
print(resp.text)
print(resp.json)