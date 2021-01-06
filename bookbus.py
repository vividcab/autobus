import requests as rq
import json
import datetime
import sys
import decrypt as Crypt
username = "xxxx"
password = "xxxxxx"
url = 'http://159.226.95.123/dataForward'
key = '0102030405060708'

def Login(user, pwd):
    data = {"idserial":user,"password":pwd,"method":"/mobile/login/userLoginCheck"}
    cipher_data = Crypt.aes_encode(key, json.dumps(data).replace(' ', '')).upper()
    data = {"item":cipher_data}
    r = rq.post(url, json=data)
    #print(r.text)
    if r.status_code == 200:
        if r.json()["code"] == 200:
            return r.json()['data']['token']
        else:
            print(r.json()['msg'])
    else:
        print("登录失败")
        return None

def Logout(token):
    cipher_token = Crypt.aes_encode(key, token).upper()
    header = {"X-Token":cipher_token}
    data = {"method":"/mobile/login/mobileLogout"}
    cipher_data = Crypt.aes_encode(key, json.dumps(data).replace(' ', '')).upper()
    data = {"item":cipher_data}
    r = rq.post(url, headers=header, json=data)
    #print(r.text)
    if r.status_code == 200:
        print(r.json()['data'])
        return None
    else:
        print("查询错误")
        return None

def QueryBus(token, date):
    cipher_token = Crypt.aes_encode(key, token).upper()
    header = {"X-Token":cipher_token}
    data = {"selldate":date,"enddate":date,"method":"/mobile/home/queryHomeGoods"}
    cipher_data = Crypt.aes_encode(key, json.dumps(data).replace(' ', '')).upper()
    data = {"item":cipher_data}
    r = rq.post(url, headers=header, json=data)
    #print(r.text)
    if r.status_code == 200:
        if r.json()["code"] == 200:
            return r.json()['data']
        else:
            print(r.json()['msg'])
            return None
    else:
        print("查询错误")
        return None

def FindBusId(buslist, busname): # busname: 时间发站-到站，例如 20:30益园-张仪村
    for bus in buslist:
        if bus["goodsname"] == busname:
            return bus["id"]
    return None

def Book(token, date, busid, busname):
    cipher_token = Crypt.aes_encode(key, token).upper()
    header = {"X-Token":cipher_token}
    data = {"selldate":date,"id":busid,"method":"/mobile/pay/toPaySelf"}
    cipher_data = Crypt.aes_encode(key, json.dumps(data).replace(' ', '')).upper()
    data = {"item":cipher_data}
    r = rq.post(url, headers=header, json=data)
    #print(r.text)
    if r.status_code == 200:
        if r.json()['code'] == 200:
            print("预定【%s %s】成功，订单号：%s" %(date, busname, r.json()["data"]))
            return r.json()['data']
        else:
            print("预定【%s %s】失败，msg：%s" %(date, busname, r.json()["msg"]))
    else:
        print("预订错误")
        return None

if __name__ == "__main__":
    date1 = datetime.datetime.now()
    print(date1)
    delta = datetime.timedelta(days=2)
    date = str(date1.date()+delta)
    print(date)
    busnames = ["8:00张仪村-益园", "20:30益园-张仪村"]
    token = Login(username, password)
    print("token: ", token)

    if not token:
        sys.exit()

    buslist = QueryBus(token, date)
    if not buslist:
        Logout(token)
        sys.exit()

    for busname in busnames:
        busid = FindBusId(buslist, busname)
        Book(token, date, busid, busname)
    
    Logout(token)