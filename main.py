print("Hello! Use this program to ENCRYPT OR DECRYPT a message using RSA.")

while True:
    while True:
        try:
            print("Would you like to 1)Encrypt or 2)Decrypt.")
            choice = int(input("Enter 1 or 2:"))
        except ValueError:
            print("Please enter a 1 for Encrypt or 2 for Decrypt")
        else:
            break

    #ENCRYPT...
    if (choice == 1):
        while True:
            try:
                pt = int(
                    input(
                        "What is the PLAINTEXT message you want to encrypt? "))
            except ValueError:
                print("ERROR: Sorry, your message needs to be a number")
            else:
                break
        message = pt
        publicKey = int(input("What is your FRIEND'S Public Key?"))
        publicMod = int(input("What is your FRIEND'S Public Modulus?"))
        ct = (message**publicKey) % publicMod
        print("Calculating (" + str(message) + "^" + str(publicKey) +
              ") mod " + str(publicMod) + "  =...")
        print("")
        print("CIPHERTEXT: " + str(ct))
        print("")

    #DECRYPT...
    if (choice == 2):
        while True:
            try:
                ct = int(
                    input(
                        "What is the CIPHERTEXT message you want to decrypt? ")
                )
            except ValueError:
                print("ERROR: Sorry, your message needs to be a number")
            else:
                break
        cipherText = ct
        privateKey = int(input("What is YOUR Private Key?"))
        publicMod = int(input("What is YOUR Public Modulus?"))
        plainText = (cipherText**privateKey) % publicMod
        print("Calculating (" + str(cipherText) + "^" + str(privateKey) +
              ") mod " + str(publicMod) + " =...")
        print("")
        print("PLAINTEXT: " + str(plainText))
        print("")
