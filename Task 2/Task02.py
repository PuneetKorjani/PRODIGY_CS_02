from PIL import Image

def encrypt_image(input_image , output_path):
    img = Image.open(input_image)
    pixels = img.load()
    
    width, height = img.size
    
    for x in range(width):
        for y in range(height):
            r,g,b = pixels[x,y]
           
            encryption = (b,g,r)
            pixels[x,y] = encryption

    img.save(output_path)
    img.show(output_path)
    print("Image encrypted successfully")
    
    



def decrypt_image(encrypt_image , output_path):
    img = Image.open(encrypt_image)
    pixels = img.load()

    width , height = img.size
    for x in range(width):
        for y in range(height):
            b,g,r = pixels[x ,y]
            decryption = (r,g,b)
            pixels[x,y] = decryption
    
    img.save(output_path)
    img.show(output_path)
    print("image decrypted successfully")







# encryption
input = 'studs.jpeg'
output_encryption = 'encrypted_image.jpeg'

encrypt_image(input,output_encryption)


# decryption
encrypt_image_path = 'encrypted_image.jpeg'
output_decryption = 'decrypted_image.jpeg'



decrypt_image(encrypt_image_path, output_decryption)








