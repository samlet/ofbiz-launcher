#!/usr/bin/env python
import requests
with requests.Session() as s:
    r=s.get('https://localhost:8443/ofbizDemo/control/main/ajaxCheckLogin?USERNAME=admin&PASSWORD=ofbiz', verify=False)
    print(r.headers)

    # visitUrl='https://localhost:8443/partymgr/control/FindCommunicationEvents'
    visitUrl='https://localhost:8443/ofbizDemo/control/AddOfbizDemoXml'
    r=s.get(visitUrl, verify=False)
    print("response code is "+str(r.status_code))
    print(r.text)


