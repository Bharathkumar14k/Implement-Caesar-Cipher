import socket
name= socket.gethostname()
alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def run_the_show(eord, text, shift_key):
    if eord == 'encrypt':
        cipher_text=""
        for char in text:
            if char in alphabets:
                postion= alphabets.index(char)
                new_position=(postion+shift_key)%26
                cipher_text+=alphabets[new_position]
            else:
                cipher_text+=char
        return f"Here is the text after encryption:{cipher_text}"
    elif eord == 'decrypt':
        plain_text=""
        for char in text:
            if char in alphabets:
                postion= alphabets.index(char)
                new_position=(postion - shift_key)%26
                plain_text+=alphabets[new_position]
            else:
                plain_text+=char
        return f"Here is the text after decryption:{plain_text}"
    else:
        return "Given wrong input please try again"
    
print("WELCOME! "+name)
again=True
while again:
    eord= input("Type 'encrypt' for encryption or type 'decrypt' for decryption: \n")
    text = input("Enter the text: \n").lower()
    shift_key= int(input("Enter the shift key: \n"))
    a= run_the_show(eord, text, shift_key)
    print(a)
    try_again= input("type 'y' to try again or type 'n' to quit")
    if try_again == 'n':
        again= False
        print("Thank you!")
    else:
        again= True
        