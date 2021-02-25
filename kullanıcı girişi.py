print("-"*30,"\nkullanıcı girişine hoşgelsiniz\n","-"*30,sep="")

username = "userr"
userpasword = "123456"

hak = 3


while True:
    if hak > 0:
        sysUserName = input("lütfen kullanıcı adınızı girin:")
        sysUserPasword = input("lütfen şifrenizi girin (only number):")
        
        if sysUserName != username and sysUserPasword == userpasword:
            print("kullanıcı adınız yanlış.")
            hak -=1
            continue
    
        elif sysUserName == username and sysUserPasword != userpasword:
            print("lütfen şifrenizi doğru yazın")
            hak -=1
            continue

        elif sysUserName != username and sysUserPasword != userpasword:
            print("kullanıcı adı ve şifre hatalı")
            hak -=1
            continue
    
        else:
            print("sisteme hoşgeldiniz....")
            break

    elif hak == 0:
        print("girişiniz geçici bi süreliğine engellendi!!!")
        break
