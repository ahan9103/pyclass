while True:
    # 使用者輸入
    number = input("請輸入一個數字：")

    # 轉換為數字型別（整數）
    number = int(number)

    # 判斷並輸出結果
    if number > 10:
        print("這個數字大於 10")
    elif number < 10:
        print("這個數字小於 10")
    else:
        print("這個數字等於 10")
