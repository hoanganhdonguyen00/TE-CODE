x = 1

while x <= 5:
    user = input("tài khoản: ")
    pwd = input("mật khẩu: ")
    
    if user == "1245" and pwd == "qaas":
        print("chúc mừng")
        break
    else:
        x += 1

if x > 5:
    print("đã qá lần đăng nhập")