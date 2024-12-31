import requests

url = "{{apiUrl}}/api/v1/auth"

payload={}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

import requests

url = "{{apiUrl}}/api/v1/auth"

payload={}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

import requests

url = "{{apiUrl}}/api/v1/webhook"

payload = "{\r\n    \"link_id\": 0,\r\n    \"url\": \"https://suaurl.com.br/callback\"\r\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


import requests

url = "{{apiUrl}}/api/v1/webhook"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import requests

url = "{{apiUrl}}/api/v1/webhook/[webhook_id]"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import requests

url = "{{apiUrl}}/api/v1/webhook/[webhook_id]"

payload={}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)


import requests

url = "{{apiUrl}}/api/v1/link"

payload = "{\r\n    \"slug\":\"o nome do seu link aqui\"\r\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


import requests

url = "{{apiUrl}}/api/v1/link/[link_id]"

payload={}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

import requests

url = "{{apiUrl}}/api/v1/link"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


import requests

url = "{{apiUrl}}/api/v1/link/[link_id]"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


import requests

url = "{{apiUrl}}/api/v1/link/slug/[slug]"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


{
    "amount": "3.03",
    "type":"pix",
    "link_id": 26,
    "message" : { //Não obrigatório
        "name" : "Angelo",
        "text" : "O corpo da mensagem",
        "email" : "email@test.cm"
    }
}


import requests

url = "{{apiUrl}}/api/v1/payment"

payload = "{\r\n    \"amount\": \"3.03\",\r\n    \"type\":\"pix\",\r\n    \"link_id\": 26,\r\n    \"message\" : { //Não obrigatório\r\n        \"name\" : \"Angelo\",\r\n        \"text\" : \"O corpo da mensagem\",\r\n        \"email\" : \"email@test.cm\"\r\n    }\r\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

import requests

url = "{{apiUrl}}/api/v1/payment/[uuid]"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


import requests

url = "{{apiUrl}}/api/v1/payment?limit=100&page=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import requests

url = "{{apiUrl}}/api/v1/config/pix"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

{
    "minimum_amount": "2",
    "pix_duration": "600"
}


import requests

url = "{{apiUrl}}/api/v1/config/pix"

payload = "{\r\n    \"minimum_amount\": \"2\",\r\n    \"pix_duration\": \"600\"\r\n}"
headers = {}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)


