from avi.sdk.avi_api import ApiSession
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# input
cip = input("Enter controller ip: ")
cname = input("Enter username: ")
cpass = input("Enter password: ")
pname = input("Input pool name: ")
sip = input("Input pool server ip: ")
vsname = input("Input virtual service name: ")
vip = input("Input VIP for VS: ")
vport = input("Input VIP port: ")

#api session
api = ApiSession.get_session(cip, cname, cpass, tenant="admin")

# Create Pool
pool_frame = {u'lb_algorithm': u'LB_ALGORITHM_LEAST_CONNECTIONS', u'default_server_port': 80, u'name': pname,
              u'servers': [{u'ip': {u'type': u'V4', u'addr': sip}}]}
resp = api.post('pool', data=pool_frame)

pool_obj = api.get_object_by_name('pool', pname)
pool_ref = api.get_obj_ref(pool_obj)

services_obj = [{'port': vport, 'enable_ssl': False}]
vs_obj = {'name': vsname, 'ip_address': {'addr': vip, 'type': 'V4'}, 'services': services_obj, 'pool_ref': pool_ref}

resp = api.post('virtualservice', data=vs_obj)

if resp.ok:
    print('VS Creation Success')
else:
    print('VS Creation Failure')


#Enter controller ip: 10.91.89.10
#Enter username: admin
#Enter password: !!avi123
#Input pool name: testp
#Input pool server ip: 10.10.24.205
#Input virtual service name: testvs
#Input VIP for VS: 10.91.89.143
#Input VIP port: 80