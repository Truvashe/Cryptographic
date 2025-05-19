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

    #a is the image by it self
    #b are the pixels of said img converted into values of RGB

    #Code to annalyse image resolution, if ever we need to code the text into the next line of pixels.
        
    width, height = img.size
    if width<15 or height <15:
        print("Image too short, please choose a bigger image.")
        return False
            
    for i in user_name:
        val=int(text_encode[k])
        b[i,0]=(val,b[i,j][1],b[i,j][2])

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

def open_image_decrypt(img,user_name,white_listed):
    a=Image.open(img)
    a=a.convert("RGB")
    b=a.load()

    width, height = img.size

    text=[]

    for j in height:
        for i in width:
            text.append(b[i,j][0])

    for i in text:
        if (text[i]!="\n"):
            text[i]=chr(text[i])

    j=0
    for i in text:
        first_line+=str(i)
        j+=1
        if j>10:
            break
    
    white_listed=user_int.get_wlist(user_name)

    #check if the username have is
    if any(word in text for word in white_listed):
        file=open("Output.txt","w")
        file.write(''.join(text))
        file.close
        return True
    else:
        print("User is not in your white list")
        return False