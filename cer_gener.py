from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import qrcode
import yagmail
import os




path="./participants.csv"
dataframe=pd.read_csv(path)
font_name=ImageFont.truetype('/home/chitreshnarra/.local/share/fonts/NimbusMono-Regular.otf',40,encoding="unic")
font_event=ImageFont.truetype('/home/chitreshnarra/.local/share/fonts/NimbusMono-Regular.otf',40,encoding="unic")

directory="./all_certificates"




for index,item in dataframe.iterrows():
    img=Image.open('cer.jpg')
    draw=ImageDraw.Draw(img)
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=7,
    border=2
    )
    t = f"{item['name']}"
    x = len(t)
    text1 = " "*(27//2-x//2)+f"{item['name']}"+" "*(27//2-x//2)
    qr.add_data("https://ipk33jtfxtnruirt9j5e7g.on.drv.tw/website/{}.html".format(item['email']))
    qr.make()
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("./qrs/{}.png".format(item['email']))
    draw.text(xy=(580 , 600 ),text=text1,fill=(0,0,0),font=font_name)
    offset = 740,820
    img.paste(qr_img,offset)
    img.save('./all_certificates/{}.jpg'.format(item['email']))


    f = open(f"./website/{item['email']}.html",'w')
    message = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Petrichor</title>
        <style>
            body
            {{
                background-image: url("./bg.png");
                background-repeat: no-repeat;
                background-size: cover;
                padding: 0;
                margin: 0;
                min-height: 100vh;
            }}
            #heading
            {{
                display: flex;
                padding-left: 37vw;
                align-self: flex-start;
            
            }}
            h1
            {{
                color: rgb(0,0,0);
                font-size: 50px;
                letter-spacing: 4px;
                font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif; 
                text-align: center;
                
                
            }}
            #logo
            {{
                
                width: 50px;
                display: flex;
                justify-self: left;
                align-self: top;
                padding-left: 30px;
                margin-top: -95px;
                padding-bottom: 15px;
            }}#cer
            {{
                width: 21vw;
                outline: 1px solid whitesmoke;
                display: flex;
                align-self: center;
                margin: 20px;
                padding: 5px;
            }}
            #content
            {{
                display: flex;
                justify-content: center;
                justify-self: center;
                align-self: center;
                margin-left:10vw;
                width: 80vw;
                height: auto;
                outline: 1px solid whitesmoke;
                
            
                
            }}
            p
            {{
                color: rgb(0,0,0);
                font-size: 30px;
                letter-spacing: 3px;
                word-spacing: 7px;
                font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif; 
                padding-left: 5vw;
                display: flex;
                align-self: center;
                z-index: 5;
            }}
            @media screen and (max-width:950px)
            {{
                #heading
                {{
                    padding-left: 32vw;

                }}
            
                #cer
                {{
                    width: 27vw;
                }}      
            }}
            @media screen and (max-width:770px)
            {{
                #heading
                {{
                    padding-left: 27vw;

                }}
                
                #content
                {{
                    display: grid;
                    justify-items: center;  
                    margin-bottom: 10vh;         
                }}
                #cer
                {{
                    width: 70vw;
                }}
                            
            }}
            @media screen and (max-width:500px)
            {{
                #heading
                {{
                    padding-left: 20vw;

                }}
                h1 
                {{
                    font-size: 30px;
                }}
                #content
                {{
                    width: 96vw;
                    margin-left: 2vw;
                }}   
                
                p
                {{
                    font-size: 20px;
                    letter-spacing: 1px;
                    word-spacing: 3px;

                }}
                #logo
                {{
                    width: 40px;
                    padding-left: 15px;
                    margin-top: -80px;
                    padding-top: 20px;
                    padding-bottom: 10px;
                }}  
            }}
            @media screen and (max-width:290px)
            {{
                #heading
                {{
                    padding-left: 10vw;
                    font-size: 40px;

                }}
                #logo
                {{
                    opacity: 0;
                }}  
            }}
            
        </style>
    </head>
    <body>
        <div id="heading">
            <h1>Petrichor '22</h1>
        </div>
        <div id="im">
            <img src="Logo.png" alt="" id="logo" >
        </div>
            
        <div id="content">
            <p>This certificate is awarded to Mr/Ms {item['name']} for enthusiastically participating in Artificial Intelligence Workshop conducted by Petrichor, IIT Palakkad from 17th , 18th September 2022.</p>
            <a href="./all_certificates/{item['email']}.jpg" target="_blank"><img src="./all_certificates/{item['email']}.jpg" alt="" id="cer"></a>
        </div>
            
    </body>
    </html>"""

    f.write(message)
    f.close()






# yag = yagmail.SMTP('UR MAIL', 'UR PASSWORD')

# for index,item in dataframe.iterrows():
#     email=item['email']

#     contents = [
#         '''Dear Participant, 

#                 Thanks for participating in the Workshop conducted by Petrichor 22. Please find the attached certificate. 

#         Regards,
#         Petrichor Technical Team.
#         ''', f'/home/chitreshnarra/stuff/workshop/Certificate_generator-main/all_certificates/{email}.jpg'
#     ]
#     yag.send(f'{email}', 'Petrichor Workshop Certificate', contents)


