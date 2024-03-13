from PIL import Image
import binascii


class LSB_Stenograph:

    def __init__(self) -> None:
        pass

    # def get_user_input_string(self):
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
        
    #     return inputstring_user
        
    #     # length_of_string = len(inputstring_user)

#     minimal_length_of_picture_needed = length_of_string*8 + 8 # + 8 for end of string character

#     print("XXXXXXXXXXXXXXXXXXX")
#     print(binascii.a2b_uu("a"))
#     print("OOOOOOOOOOOOOOOOOOOOOOO")
    
  
# # Python3 code to demonstrate working of
# # Converting String to binary
# # Using join() + ord() + format()
    # https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
    
    def decimalToBinary(self, n): 
        str = bin(n).replace("0b", "")
        return str.zfill(8)
    
 
    def convert_str_to_binary(self, input_string):
        # https://www.geeksforgeeks.org/python-convert-string-to-binary/
        
        # printing original string 
       # print("The original string is : " + str(input_string))
        
        # using join() + ord() + format()
        # Converting String to binary
        inputStringInBinary = ''.join(format(ord(i), '08b') for i in input_string)
        
        return inputStringInBinary

    
    def open_pic_and_read_pixel_data(self,image_path):
        # Open the image file
        with Image.open(image_path) as img:
            # Convert the image to RGB mode if it's not already in RGB
            img = img.convert("RGB")

            # Get pixel data as a list of tuples (R, G, B)
            pixel_array = list(img.getdata())

        # print(pixel_array)
                
            # Convert pixel array to a list of bits
        bit_array = []
        for pixel in pixel_array:
            
            for value in pixel:
                bit_array.append(self.decimalToBinary(value))  # Add each bit of the byte

        # print(bit_array)
        # print("Leng of bitarray  : ",len(bit_array))

        return bit_array, img.size

 



    
    def extract_hidden_message(self,bit_array):
        
        # bit array is an array that holds the bytes stored as bits
        messagebits = []
        zero_counter=0
        null_terminator_found=False

        for i in range(0,len(bit_array)):
           
            if(bit_array[i][-1]== "0"):
                zero_counter+= 1
            else:
                zero_counter=0        
        
            if i+1 % 8 ==0:
                zero_counter=0
            if zero_counter==8:
                #print("Null terminator found. End of encrypted message")
                null_terminator_found = True
                break

            messagebits.append(bit_array[i][-1])
        print(messagebits)
        message_bits_string = ''.join(messagebits)


        # Convert the binary string to a string of ascii chars
        ascii_string = ""
        # interpret every 8 bits
        for i in range(0, len(message_bits_string), 8):
            byte = message_bits_string[i:i+8]
            int_of_byte = int(byte, 2)
            ascii_character = chr(int_of_byte)
            ascii_string += ascii_character

        return ascii_string, null_terminator_found
    
    def truncate(self, s, l):
        if (l >= len(s)):
            return (s)
        else:
            return (s[:l])
    
    def embedd_hidden_message_in_picture_pixel_array(self, hidden_message, picture_bit_array):
        # printing original string 
        
        # using join() + ord() + format()
        # Converting String to binary
        #https://www.geeksforgeeks.org/python-convert-string-to-binary/
        hidden_message_binary = ''.join(format(ord(i), '08b') for i in hidden_message)
        print("length of bit picture array: ", len(picture_bit_array))
    

        # check if there is enough space to hide message.
        
        if len(picture_bit_array) < 16:
            print("The destination image does not have enough space to store any text. No output image will be generated")
            return
        
        elif len(picture_bit_array) < len(hidden_message_binary) + 8:
            print("Not enough space to store the whole string, it will be trunkated")

            # trunkate string:
            a=8
            trunkated_hidden_message_binary= hidden_message_binary[0:a]
            while len(picture_bit_array) > len(trunkated_hidden_message_binary) + 8:
                trunkated_hidden_message_binary= hidden_message_binary[0:a]
                a+=8
                
            hidden_message_binary = trunkated_hidden_message_binary
            print("Hidden message: ", hidden_message_binary)
#            picture_bit_array[i] = picture_bit_array[i][:-1] + hidden_message_binary[hidden_index]


        counter_hidden_message_placed=0
        print("OLd string: ", picture_bit_array)
        for i in range(len(picture_bit_array)):
            if counter_hidden_message_placed < len(hidden_message_binary):
                picture_bit_array[i] = picture_bit_array[i][:-1] + hidden_message_binary[counter_hidden_message_placed]
                counter_hidden_message_placed += 1
            else:
                if counter_hidden_message_placed < len(hidden_message_binary) + 8:
                    picture_bit_array[i] = picture_bit_array[i][:-1] + '0'
                    counter_hidden_message_placed += 1
                else:
                    break
        
        return picture_bit_array



    
    def get_user_input_embed_or_extract(self):
        flag = True
        print("Choose an option: \n1. Embed string in bitmap. \n2. Extract string from bitmap. \n \n")
        while flag:
            user_input=input("Enter the number corresponding to your desired option: ")
            if user_input =="1" or user_input=="2":
                flag=False
            else:
                print("Your input was invalid. Try again.")


        return user_input


    def get_string_to_hide(self):
        flag = True
        userInputString=""
        while flag:
            userInputString = input("Enter the string to embed: ")
            for char in userInputString:
                if ord(char) >=32 and ord(char) <=127:
                    flag = False
                
            
            if flag:
                print("\nYour input is either empty or not a valid ASCII string. Try again.")

        return userInputString


    def create_bitmap_image(self, bit_array, image_size):
        # Convert each binary string in bit_array back to its decimal representation
        decimal_values = [int(binary, 2) for binary in bit_array]

        # Reconstruct the pixel array using the decimal values for each color channel (R, G, B)
        pixel_array = [(decimal_values[i], decimal_values[i+1], decimal_values[i+2]) for i in range(0, len(decimal_values), 3)]

        # Create a new image from the reconstructed pixel array
        new_image = Image.new("RGB", image_size)
        new_image.putdata(pixel_array)
        
        return new_image

    
    
    
    def main(self): 
        
        Adds one too much chars and does not add the null character!!!!!!!!!
        #a = './test-images/test-images/original-test-images/duq_logo.bmp'
        
        a = "newwuhu.bmp"
        lsb_instance = LSB_Stenograph()


        user_input_embed_or_extract = lsb_instance.get_user_input_embed_or_extract()

        if user_input_embed_or_extract == "1":
            # embed a string in a picture
            string_to_hide = lsb_instance.get_string_to_hide()
            pixel_bit_array, img_size = lsb_instance.open_pic_and_read_pixel_data(a)
            pixel_bit_array_with_embedded_message = lsb_instance.embedd_hidden_message_in_picture_pixel_array(hidden_message=string_to_hide, picture_bit_array=pixel_bit_array)
            new_image = lsb_instance.create_bitmap_image(pixel_bit_array_with_embedded_message,img_size)
            
            new_image.save("newwuhu.bmp")
            

        else:
            # extract string from bitmap:
            pixel_bit_array, img_size = lsb_instance.open_pic_and_read_pixel_data(a)
            hidden_message, null_terminator_found = lsb_instance.extract_hidden_message(pixel_bit_array)

            if not null_terminator_found:
                print("WARNING: No null terminator was found when extracting text from the image. This means that steganography was likely not applied to the input image, and thus, the output string is likely arbitrary nonsense.")
            print("The output string created from the image is: ")
            print(hidden_message)




if __name__ == "__main__":
    lsb_instance = LSB_Stenograph()
    lsb_instance.main()