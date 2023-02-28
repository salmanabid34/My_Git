import requests
#payload={'page':2,'count':25}
#r=requests.get('https://httpbin.org/get',params=payload)
#print(r.url)
payload={'username':'corey','password':'hi.apk'}
r=requests.post('https://httpbin.org/post',data=payload)
print(r.json())