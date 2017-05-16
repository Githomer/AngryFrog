import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, requests

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.

    #select proper type!!!!!!!!!!!!!!!!!!!

    #'Content-Type': 'application/octet-stream',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9ea940a34ebd408ca9465115a94e9f39',
}

params = urllib.parse.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
#body = open('c:\ex.jpg', 'rb')
body = "{ 'url': 'http://cfile9.uf.tistory.com/image/233F604857F3ACD6208420' }"


try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e.args)

    
    
#refer from https://github.com/Microsoft/Cognitive-Emotion-Python/blob/master/Jupyter%20Notebook/Emotion%20Analysis%20Example.ipynb
