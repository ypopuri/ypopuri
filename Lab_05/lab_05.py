import re
import requests
import json
url = "https://michaelgathara.com/api/python-challenge"
response = requests.get(url)
challenges = response.json()
print(challenges)
newstr = challenges
str = newstr 
str = '[{"id":1,"problem":"3 + 5?"},{"id":2,"problem":"7 * 6?"},{"id":3,"problem":"20 / 5?"},{"id":4,"problem":"20 / 4?"},{"id":5,"problem":"15 - 7?"},{"id":6,"problem":"9 * 9?"},{"id":7,"problem":"27 / 9?"},{"id":8,"problem":"100 - 56?"},{"id":9,"problem":"14 + 26?"},{"id":10,"problem":"64 / 8?"}]'
arr = str.split('},{')
size = len(arr)
to_array = []
op_array = []
for x in range(10):
    for y in arr[x]:
        to_array.extend(y)
num = re.findall(r'\d+', str)
ope = 0
num1 = []
num2 = []
num1 = 1
num2 = 2
size1 = len(to_array)
for x in range(size1):
        if to_array[x]=='+' or to_array[x]=='-' or to_array[x]=='/' or to_array[x]=='*':
            if to_array[x]=='+':
                print(num[num1],to_array[x],num[num2])
                print(int(num[num1])+int(num[num2]))
            if to_array[x]=='-':
                print(num[num1],to_array[x],num[num2])
                print(int(num[num1])-int(num[num2]))
            if to_array[x]=='*':
                print(num[num1],to_array[x],num[num2])
                print(int(num[num1])*int(num[num2]))
            if to_array[x]=='/':
                print(num[num1],to_array[x],num[num2])
                print(int(num[num1])/int(num[num2]))
            print()
            num1 += 3
            num2 += 3