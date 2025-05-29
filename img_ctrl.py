from PIL import Image
import user_int

def encodage_de_texte(text):
    encodage= [ord(char) for char in text]
    return encodage

def open_image_crypt(img,text,user_name):
    a=Image.open(img)
    a=a.convert("RGB")
    b=a.load()
    text_encode=encodage_de_texte(text)

    stop_index=0

    #a is the image by it self
    #b are the pixels of said img converted into values of RGB

    #Code to annalyse image resolution, if ever we need to code the text into the next line of pixels.
        
    width, height = a.size

    if width<15 or height <15:
        print("Image too short, please choose a bigger image.")
        return False
            
    encoded_name=encodage_de_texte(str(user_name))
    for i in range(len(user_name)):
        val=int(encoded_name[i])
        b[i,0]=(val,b[i,0][1],b[i,0][2])

        stop_index=i

    #puting a stop to the fugazi
    b[stop_index,0]=(0,b[stop_index,0][1],b[stop_index,0][2])

    i=0
    j=1
    for k in range(len(text_encode)):
        if i>=width:
            j+=1
            i=0
        if j>=height:
            print("ERROR, Image too short. The Text couldn't be cripted all in. Please choose a bigger Image to put in all the text")
            return False
        val=int(text_encode[k])
        b[i,j]=(val,b[i,j][1],b[i,j][2])

        i+=1

    a.save("Output_image.png")

    print("Text crypté")

    return True

def open_image_decrypt(img,user_name):
    a=Image.open(img)
    a=a.convert("RGB")
    b=a.load()

    first_line=""

    width, height = a.size

    text=[]

    for j in range(height):
        for i in range(width):
            text.append(b[i,j][0])


    for i in range(len(text)):
        text[i]=chr(text[i])

    j=0
    for i in text:
        first_line+=str(i)
        j+=1
        if j>10:
            break
    
    #first_line=first_line.strip()
    
    #white_listed=user_int.get_wlist(first_line)
    text=''.join(text)
    text.strip()

    file=open("Output.txt","w")
    file.write(str(text))
    file.close()

    print("END SCRIPT")

    #check if the username have is
    #if any(word in first_line for word in white_listed):
        #file=open("Output.txt","w")
        #file.write(''.join(text))
        #file.close
    #    print("User is in your white list")
        #return True
    #else:
        #print("User is not in your white list")
        #return False