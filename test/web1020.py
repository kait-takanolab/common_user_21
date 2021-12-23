from urllib import request

response = request.urlopen('https://www.pasonatech.co.jp/')
content = response.read()
response.close()
html = content.decode()

title = html.split('<h1>')[1].split('</h1>')[0]
print(title)