# import requests
#
# url = 'https://t-data.seoul.go.kr/apig/apiman-gateway/tapi/BisTbisMsSttn/1.0?apikey=5a6b778c-d42a-4f65-a553-0cfeb90d5bfe'
#
# response = requests.get(url)
#
# print(response.text)

import requests
# import json

url = "https://apis.data.go.kr/1613000/BusRoutespecificStopInformation/getBusRoutespecificStopInformation"

params = {
    'serviceKey ' : '5a6b778c-d42a-4f65-a553-0cfeb90d5bfe'

}

response = requests.get(url, params=params)

response.raise_for_status()

# JSON 파싱
data = response.json()

print(data)

# =========================
# 1. JSON 파일로 저장
# =========================
# with open("bus_route.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
#
# print("✔ JSON 파일 저장 완료 (bus_route.json)")

