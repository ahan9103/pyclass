try:
    number = int(input("請輸入一個數字："))
    if number > 10:
        print("這個數字大於 10")
    elif number < 10:
        print("這個數字小於 10")
    else:
        print("這個數字等於 10")
except ValueError:
    print("請輸入正確的數字格式")
