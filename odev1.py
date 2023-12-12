import requests
url="https://api.waifu.im/search?included_tags=maid&height=>=2000"
response=requests.get(url)
data=response.json()
print(data)
