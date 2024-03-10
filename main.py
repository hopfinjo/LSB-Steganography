from PIL import Image


class LSB_Stenograph:

    flag = True
    while flag:
        flag = False
        # get input from user:
        input = input("PLease enter your string")
        print(input)
        if(len(input)>0):
            flag=True
        
        # verify input:
        # ASCII printable characters (character code 32-127)
        # The extended ASCII codes (character code 128-255)

        for char in input:
            if ord(char) >=32 and ord(char) <=127:
                flag=True;


    # Open the image file
    with Image.open('./test-images/test-images/original-test-images/1by5.bmp') as img:

        
        # Get the pixel data
        pixel_data_inhex = img.tobytes()

        bits=""

        for byte in pixel_data_inhex:
            # Convert byte from hexadecimal to bits
            bits += format(byte, 'b')

        # Print the binary data
        print(pixel_data_inhex)
        print("\n")
        print(bits)
        print("\n")
        print("And it has ",len(bits) , " length")

        if (len(bits)/8) > 8:
            print("YOU CAN STORE ONE INTEGER IN THIS PICTURES")
        else:
            print("YOU CAN NOT NOT NOT IT HAS LESS THAN 8 BYTES STORE AT LEAST ONE ASCI NR IN IT")

        print("that means there are bytes (packs of 8 bits)", len(bits)/8)
        print("\n")
        print() 


        







