from flask import Flask,request
import requests
import json
app = Flask(__name__)
@app.route('/newCasesPeak',methods=['GET'])
def newCasesPeak():
    Country=request.args.get('country')
    data = requests.get("https://disease.sh/v3/covid-19/historical/{}?lastdays=31".format(Country)).json()
    cases = data["timeline"]["cases"]
    flag=0
    dif=0
    prev=0
    for key,value in cases.items():
        if flag==0:
            flag=1
            prev=value
            date=key
        elif(value-prev > dif):
            dif=value-prev
            date=key 
            prev=value
    #print(date, "," ,dif )
    result="{“country”:”%s”,“method”:“newCasesPeak”,”%s”:“date”,“value”:%d}"%(Country,date,dif)

    return result

@app.route('/newDeathsPeak',methods=['GET'])
def newDeathsPeak():
    Country=request.args.get('country')
    data = requests.get("https://disease.sh/v3/covid-19/historical/{}?lastdays=31".format(Country)).json()
    cases = data["timeline"]["deaths"]
    flag=0
    dif=0
    prev=0
    for key,value in cases.items():
        if flag==0:
            flag=1
            prev=value
            date=key
        elif(value-prev > dif):
            dif=value-prev
            date=key 
            prev=value
    #print(date, "," ,dif )
    result="{“country”:”%s”,“method”:“newDeathsPeak”,”%s”:“date”,“value”:%d}"%(Country,date,dif)
    return result

@app.route('/newRecoveredPeak',methods=['GET'])
def newRecoveredPeak():
    Country=request.args.get('country')
    data = requests.get("https://disease.sh/v3/covid-19/historical/{}?lastdays=31".format(Country)).json()
    cases = data["timeline"]["recovered"]
    flag=0
    dif=0
    prev=0
    for key,value in cases.items():
        if flag==0:
            flag=1
            prev=value
            date=key
        elif(value-prev > dif):
            dif=value-prev
            date=key 
            prev=value
    #print(date, "," ,dif )
    result="{“country”:”%s”,“method”:“newRecoveredPeak”,”%s”:“date”,“value”:%d}"%(Country,date,dif)
    return result


if __name__ == '__main__':
    app.run(host="localhost", port=8080)