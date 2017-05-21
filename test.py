import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, requests, json, os, time

while(True): 
    success_flag = False

    print("Cheese")

    #cmd = "raspistill -w 400 -h 500 -t 1000  -o " + "image.jpg"

    #os.system(cmd)


    fp = open("emotion.txt", "w")

    headers = {
       'Content-Type': 'application/octet-stream',
       'Ocp-Apim-Subscription-Key': '9ea940a34ebd408ca9465115a94e9f39',
    }

    params = urllib.parse.urlencode({
    })


    body = open('/home/pi/image.jpg', 'rb')

    print("try")

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()

        data = response.read()

        print(data)

        data = str(data).split("[")[1]
        data = data.split("]")[0]

        dict_data = json.loads(data)

        emotion_sum = 0

        for k, v in dict_data["scores"].items():
            print("%-15s : %10f" %(k, v))
            if k != 'neutral' and k != 'happiness' and k != 'surprise':
                emotion_sum += v

        print("\nEmotion Sum = %f" %emotion_sum)
        success_flag = True

        conn.close()

        print("analysis done")

    except Exception as e:
        print("error\n", e.args)


    if(success_flag == True):
        if(emotion_sum > 0.3):
            print("1")
            print("1", file=fp)
        else:
            print("0")
            print("0", file=fp)


    print("End")

    fp.close()
    time.sleep(15)
