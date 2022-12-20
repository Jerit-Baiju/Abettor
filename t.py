import requests

arr_1 = requests.get('https://raw.githubusercontent.com/Jerit-Bajiu/dictionary/master/popular.txt').text.split()
arr_2 = requests.get('https://raw.githubusercontent.com/Jerit-Baiju/dictionary/master/popular.txt').text.split()

print(arr_1)
