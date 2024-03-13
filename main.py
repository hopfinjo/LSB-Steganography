from PIL import Image
import binascii


class LSB_Stenograph:


#     flag = True
#     while flag:
#         flag = False
#         # get input from user:
#         inputstring_user = input("PLease enter your string")
#         print(inputstring_user)
#         if(len(inputstring_user)>0):
#             flag=False
        
#         # verify input:
#         # ASCII printable characters (character code 32-127)
            
#         # not included in my check ??!!
#         # The extended ASCII codes (character code 128-255)

#         for char in inputstring_user:
#             if ord(char) >=32 and ord(char) <=127:
#                 flag=False
    
#     length_of_string = len(inputstring_user)
#     minimal_length_of_picture_needed = length_of_string*8 + 8 # + 8 for end of string character

#     print("XXXXXXXXXXXXXXXXXXX")
#     print(binascii.a2b_uu("a"))
#     print("OOOOOOOOOOOOOOOOOOOOOOO")
    
  
# # Python3 code to demonstrate working of
# # Converting String to binary
# # Using join() + ord() + format()
 

#     # https://www.geeksforgeeks.org/python-convert-string-to-binary/
    
#     # printing original string 
#     print("The original string is : " + str(inputstring_user))
    
#     # using join() + ord() + format()
#     # Converting String to binary
#     inputStringInBinary = ''.join(format(ord(i), '08b') for i in inputstring_user)
    
#     # printing result 
#     print("The string after binary conversion : " + str(inputStringInBinary))


    # # Open the image file
    # with Image.open('./test-images/test-images/original-test-images/1by6.bmp') as img:

        
    #     # Get the pixel data
    #     pixel_data_inhex = img.tobytes("rgb")
    #     print("pixel data in hex: ",pixel_data_inhex)
    

    #     bits_from_image=""

    #     for byte in pixel_data_inhex:
    #         # Convert byte from hexadecimal to bits
    #         bits_from_image += format(byte, 'b')


    #     #print("\n")
    #     print(" Bits from image are: ",bits_from_image)
    #     print("\n")
    #     print("And the picture has ",len(bits_from_image) , " length in bits")
    #     print("pic in bytes: ",len(bits_from_image)/8 , " length in bits")
    #     print(" MEANS YOU CAN STORE ",len(bits_from_image)/8 )

    #     # check if any ascii can be stored in it.
    #     # must be able to hold at least 2 asciis.  1 Ascii = 8 bits 
    #     if len(bits_from_image) > 16:
    #         print("YOU CAN STORE at least ONE INTEGER IN THIS PICTURE")
    #     else:
    #         print("YOU CAN NOT NOT NOT IT HAS LESS THAN 16 BITS")


# https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
    def decimalToBinary(n): 
        str = bin(n).replace("0b", "")
        return str.zfill(8)
    
    print(decimalToBinary(2))

# Open the BMP image
    with Image.open('./test-images/test-images/steg-test-images/6by1.bmp') as img:
        # Convert the image to RGB mode if it's not already in RGB
        img = img.convert("RGB")

        # Get pixel data as a list of tuples (R, G, B)
        pixel_array = list(img.getdata())

    print(pixel_array)
            
        # Convert pixel array to a list of bits
    bit_array = []
    for pixel in pixel_array:
        
        for value in pixel:
            bit_array.append(decimalToBinary(value))  # Add each bit of the byte

    print(bit_array)
    print("Leng of bitarray  : ",len(bit_array))

    


# def main(): 

# if __name__ == "__main__":
#     main()
