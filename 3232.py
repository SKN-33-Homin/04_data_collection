import requests
import xmltodict
import json

url = "http://ws.bus.go.kr/api/rest/busRouteInfo/getRoutePath"

params = {
    "serviceKey": ".",
    "busRouteId": "100100112"
}

try:
    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    # XML → dict 변환
    data = xmltodict.parse(response.text)

    # JSON 파일 저장
    with open("bus_route.json", "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )

    print("JSON 저장 완료")

except requests.exceptions.Timeout:
    print("요청 시간 초과")

except requests.exceptions.HTTPError as e:
    print("HTTP 오류:", e)

except Exception as e:
    print("오류 발생:", e)


