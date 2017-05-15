import http.client, urllib.request, urllib.parse, urllib.error, base64, sys

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9ea940a34ebd408ca9465115a94e9f39',
}

params = urllib.parse.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Bae_Suzy_at_%22Uncontrollably_Fond%22_press_conference%2C_4_July_2016_05.jpg/250px-Bae_Suzy_at_%22Uncontrollably_Fond%22_press_conference%2C_4_July_2016_05.jpg' }"

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e.args)
