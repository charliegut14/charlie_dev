from avi.sdk.avi_api import ApiSession
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import webbrowser

# Avi Session
api = ApiSession.get_session("10.10.24.145", "admin", "@@avi123")
csrf_token = api.cookies["csrftoken"]
session_id = api.cookies["sessionid"]
tenant = input("Enter Tenant: ")
url = "https://10.10.24.145/#!/login?csrf_token=%s&session_id=%s&tenant_name=%s" %(csrf_token,session_id,tenant)
print(url)
webbrowser.open_new(url)