s_PIN = '0805'
i_PIN = int(s_PIN)

i=0
while i<3:
    print('Enter the PIN code: ')
    attempt = int(input())
    if attempt == i_PIN:
        print('Correct')
        exit()
    else:
        print('Incorrect...')
    i += 1
if i==3:
    print('Sorry, your payment card has been blocked.')