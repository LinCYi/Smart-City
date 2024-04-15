import requests
import datetime
import matplotlib.pyplot as plt

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
    
    # 初始化地震強度列表
    intensity_values = []
    
    # 解析地震資料，並將近一個月內的地震強度加入列表中
    for earthquake in data['records']['Earthquake']:
        origin_time = datetime.datetime.strptime(earthquake['EarthquakeInfo']['OriginTime'], '%Y-%m-%d %H:%M:%S')
        if origin_time > one_month_ago:
            intensity_values.append(earthquake['Intensity']['ShakingArea'][0]['AreaIntensity'])
    
    # 計算各強度級別的次數
    intensity_count = {}
    for intensity in intensity_values:
        if intensity in intensity_count:
            intensity_count[intensity] += 1
        else:
            intensity_count[intensity] = 1
    
    # 將強度級別和次數分離成兩個列表
    intensity_levels = list(intensity_count.keys())
    intensity_frequencies = list(intensity_count.values())
    
    # 繪製長條圖
    plt.figure(figsize=(10, 6))
    plt.bar(intensity_levels, intensity_frequencies, color='skyblue')
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.title('Earthquake Intensity in the Past Month')
    plt.show()
    
else:
    print("Failed to retrieve earthquake data from the API")
