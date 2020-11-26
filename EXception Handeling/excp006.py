def atm():
    total=10000
    pin = input("Enter you debit card pin")

    assert (pin =="1234"),"Login Failed"
    print("Login Successfull")
    

    amount = int(input("Enter amount to withdraw"))

    assert(amount < total),"Insufficient Balance"
    total-=amount
    print(f"Remaining Balance is : {total}")


try:
    atm()
    

except AssertionError as err:
    print("Assertion Error : ",err)
    atm()


