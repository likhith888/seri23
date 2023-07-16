import requests

url = "http://your-api-endpoint"

response = requests.get(url)

if response.status_code == 307:
    new_url = response.headers["Location"]
    response = requests.get(new_url)
    
# Process the response as needed
print(response.status_code)
print(response.text)
