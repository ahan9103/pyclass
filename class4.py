# 取得使用者輸入的總分鐘數
total_minutes = int(input("請輸入總分鐘數："))

# 計算小時與分鐘
hours = total_minutes // 60
minutes = total_minutes % 60

# 顯示結果
print(f"{total_minutes} 分鐘等於 {hours} 小時 {minutes} 分鐘")
