import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 讀取 CSV 檔案
df = pd.read_csv('PM2.5.csv')

# 以 county 群組化，計算平均 PM2.5 值
county_pm25_mean = df.groupby('county')['PM25'].mean()

# 繪製群組直條圖
fig, ax = plt.subplots()
county_pm25_mean.plot(kind='bar', color='skyblue', ax=ax)

# 設置中文字型
font_path = 'kaiu.ttf'  # 將 'your_chinese_font.ttf' 換成你的中文字型檔案路徑
font_prop = FontProperties(fname=font_path)
plt.xlabel('縣市', fontproperties=font_prop)
plt.ylabel('平均 PM2.5', fontproperties=font_prop)
plt.title('各縣市平均 PM2.5', fontproperties=font_prop)
plt.xticks(rotation=45)

plt.show()
