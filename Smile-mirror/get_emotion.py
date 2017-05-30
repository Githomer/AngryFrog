import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, requests, json, os, time, random

while(True): 
    success_flag = False
    path = "/home/pi/smart-mirror/picture/"
    cmd = ""

    print("Cheese")

    cmd = "raspistill -w 400 -h 500 -t 1000  -n -o " + path + "face.jpg"
    os.system(cmd)

    headers = {
       'Content-Type': 'application/octet-stream',
       'Ocp-Apim-Subscription-Key': '9ea940a34ebd408ca9465115a94e9f39',
    }

    params = urllib.parse.urlencode({
    })

    body = open('/home/pi/smart-mirror/picture/face.jpg', 'rb')

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
            if k != 'happiness' and k != 'surprise': # and k != 'neutral':
                emotion_sum += v

        print("\nEmotion Sum = %f" %emotion_sum)
        success_flag = True

        conn.close()

        print("analysis done")

    except Exception as e:
        cmd = "cp " + path + "black.jpg " + path + "show.jpg"
        os.system(cmd)

        print("analysis fail")

    if(success_flag == True):
        if(emotion_sum > 0.1):
            rand_num = random.randrange(1, 6)
            print(rand_num)
            cmd = "cp " + path + str(rand_num) + ".jpg " + path + "show.jpg"
            os.system(cmd)
        else:
            cmd = "cp " + path + "black.jpg " + path + "show.jpg"
            os.system(cmd)

    print("End")

    time.sleep(15)
