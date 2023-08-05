def encrypt(rec_ID,Message):
    L_enc = list(rec_ID.split("-"))
    for i in L_enc:
        if i == "0":
            Message= "$%^&*(^$~`" + Message
        elif i == "1":
            Message=Message*2
        elif i == "2":
            Message=Message[:1]+"#%🐱‍🏍"+Message[1:]
        elif i == "3":
            Message=Message[:5]+"😁#!🤑"+Message[5:]
        elif i == "4":
            Message=Message + "😋%^~"
        elif i == "5":
            Message=Message[:8]+"*$!🥱~`"+Message[8:]
        elif i == "6":
            for j in range(0,len(Message),15):
                Message=Message[:15] + "+=_👨‍💻" +Message[15:]
        elif i == "7":
            for j in range(0,len(Message),2):
                Message=Message[:2] + "$@`1~😂" +Message[2:]
        elif i == "8":
            d=int(len(Message)/6)
            Message=Message[:d]+"10021"+Message[d:]
        elif i == "9":
            q=int(len(Message)-4)
            Message=Message[:q] + "🍨"+Message[q:]
        else:
            print('Please Enter a Valid Receiver ID')
    print("\n\n           ****Receiver's Console***\n")
    print("Encrypted message: ",Message)
    return(Message)
    
def decrypt(rec_ID,mess_dec):
    L_dec = list(reversed(rec_ID))
    for i in range(0,len(L_dec),2):
        if L_dec[i] == '0':
            mess_dec=mess_dec.replace("$%^&*(^$~`",'')   
        elif L_dec[i] == '1':
            mess_dec=mess_dec[slice(0,len(mess_dec)//2)]
        elif L_dec[i] == '2':
            mess_dec=mess_dec.replace("#%🐱‍🏍",'')
        elif L_dec[i] == '3':
            mess_dec=mess_dec.replace("😁#!🤑",'')
        elif L_dec[i] == '4':
            mess_dec=mess_dec.replace("😋%^~",'')
        elif L_dec[i] == '5':
            mess_dec=mess_dec.replace("*$!🥱~`",'')
        elif L_dec[i] == '6':
            mess_dec=mess_dec.replace("+=_👨‍💻",'')
        elif L_dec[i] == '7':
            mess_dec=mess_dec.replace("$@`1~😂",'')
        elif L_dec[i] == '8':
            mess_dec=mess_dec.replace("10021",'')
        elif L_dec[i] == '9':
            mess_dec=mess_dec.replace("🍨",'')   
        else:
            break
    print("Decrypted message:",mess_dec)

while(True):
    l=int(input("Please enter your option\n1 -> Encrypt\n2 -> Decrypt\n3 -> Exit \n"))
    if(l==1):
        print("  ******* The Receiver's ID should be 10 DIGITS of the form 1-2-3-4.... *******")
        print("  ******* Format of Receiver's ID:0-1-2-3-4-5-6-7-8-9 *******\n\n")
        rec_ID = input("Enter the Receiver's ID: ")
        Message = input("Enter the message to be sent: ")
        mess_enc = encrypt(rec_ID,Message)
    elif(l==2):
        mess_dec = mess_enc
        decrypt(rec_ID,mess_dec)
    
    elif(l==3):
        break
    else:
        print("Please Enter a valid option")