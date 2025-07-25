# 取得使用者輸入
n = int(input("請輸入一個正整數："))

# 初始化結果
factorial = 1

# 使用 for 迴圈計算階乘
for i in range(1, n + 1):
    
    # factorial = factorial * i
    factorial *= i

# 輸出結果
print(f"{n} 的階乘是 {factorial}")
