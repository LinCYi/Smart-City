import requests
import datetime
import folium

# 發送請求並獲取地震資料，忽略SSL憑證的驗證
url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=rdec-key-123-45678-011121314"
response = requests.get(url, verify=False)

# 檢查請求是否成功
if response.status_code == 200:
    data = response.json()
    
    # 取得目前時間
    now = datetime.datetime.now()
    
    # 計算一個月前的日期
    one_month_ago = now - datetime.timedelta(days=30)
    
    # 初始化地震震央的經緯度列表
    earthquake_coordinates = []
    
    # 解析地震資料，並將近一個月內的地震震央的經緯度加入列表中
    for earthquake in data['records']['Earthquake']:
        origin_time = datetime.datetime.strptime(earthquake['EarthquakeInfo']['OriginTime'], '%Y-%m-%d %H:%M:%S')
        if origin_time > one_month_ago:
            epicenter_latitude = earthquake['EarthquakeInfo']['Epicenter']['EpicenterLatitude']
            epicenter_longitude = earthquake['EarthquakeInfo']['Epicenter']['EpicenterLongitude']
            earthquake_coordinates.append((epicenter_latitude, epicenter_longitude))
    
    # 初始化地圖中心點
    map_center = earthquake_coordinates[0] if earthquake_coordinates else (23.973875, 120.982024)  # 台灣的中心點
    
    # 初始化地圖
    m = folium.Map(location=map_center, zoom_start=7)

    # 在地圖上標記地震震央
    for coordinate in earthquake_coordinates:
        folium.Marker(location=coordinate, popup='Earthquake').add_to(m)

    # 顯示地圖
    display(m)
    
else:
    print("Failed to retrieve earthquake data from the API")
