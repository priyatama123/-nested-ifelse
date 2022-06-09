atm_card=input("insert atm_card")
if atm_card=="right side" or atm_card=="Right side":
 language=input("enter any language")
 if language=="english" or language=="hindi":
     pin=int(input("enter 4 digit number"))
     if pin>=1000 and pin<=9999:
         t_type=input("enter trasaction")
         if t_type=="Withdraw" or t_type=="withdraw":
             account_type=input("enter account_type")
             amount=int(input("enter amount"))
             key_name=input("enter ok")
             if amount>=500 and amount<=2000 and amount%500==0:
                 a=amount//2000
                 b=amount%2000
                 c=b//500
                 d=b%500
                 print("note of 2000=","a","note of 500=","c")
                 m_receipt=input("enter m_receipt")
                 if m_receipt=="y" or m_receipt=="n":
                     print("m_receipt")
                 else:
                     print("thanks for money transaction")
             else:
                print("limited amount")
         elif t_type=="Balance enquiry" or t_type=="balance enquiry": 
                amount_type=input("enter amount_type")
                key_name=input("enter ok")
                print("total amount")
                if key_name=="ok" or key_name=="Ok":
                    print("thanks for enquiry")
                else:
                    print("invalid key")

         elif t_type=="Deposit money" or t_type=="deposit money":
             account_no=int(input("enter account"))
             if account_no>=1000000000 and account_no<=9999999999:
                 bill_amount=int(input("enter bill_amount"))
                 key_name=input("enter ok")
                 print("succesful")
             else:
                 print("unsuccesful")
         elif t_type=="bill_payment" or t_type=="Bill_payment":
             account_no=int(input("enter account _no"))
             if account_no>=1000000000 and account_no<=9999999999:
              bill_id=int(input("enter bill_id"))
             amount=int(input("enter amount"))
             key_name=input("enter ok")
             if key_name=="ok" and key_name=="Ok":
                print("succesful")
             else:
                print("unseccesful")
         else:
             print("no transaction")       
     else:
         print("no pin number") 
 else:
     print("no language")                           
else:
    print("invalid card")






                                      


