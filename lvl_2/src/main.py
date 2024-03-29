import urllib3

# Creating a PoolManager instance for sending requests.
http = urllib3.PoolManager()

resp = http.request("GET", "https://httpbin.org/robots.txt")

print("hey!")
print(resp.status)
print(resp.data)