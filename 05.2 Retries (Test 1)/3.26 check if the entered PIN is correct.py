def check_pin():
    correct_pin = "0805"
    for i in range (0,3):
        pin = input("Enter the PIN code: ")
        if pin == correct_pin:
            print("Correct PIN!")
            i=0
        else:
            print("Incorrect...")
    if i==2:
        print("Sorry, your payment card has been blocked.")
    
    
check_pin()