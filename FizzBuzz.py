for num in range(1, 101):
    string = ''

    # ここから記述
    # 出力に利用する変数
    string ='FizzBuzz'

    # 15の倍数である場合
    if (num % 3 == 0 and num % 5 == 0):
        pass

    # 3の倍数である場合
    elif (num % 3 == 0):
        string = string[:4]

    # 5の倍数場合
    elif (num % 5 == 0):
        string = string[4:]
        
    # 3,5,15の倍数以外の場合
    else:
        string = num

    # ここまで記述

    print(string)