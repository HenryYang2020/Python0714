import requests
import json
path = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
data = requests.get(path).text  # 取得網路原始字串資料
list = json.loads(data)  # 將json字串轉成python可用的物件


for rice in list:
    name = str(rice.get('品名'))
    if name.__contains__('壽司'):
        print(name, rice.get('不合格原因'))