from PIL import Image,ImageDraw,ImageFont

image=Image.open('nobody/poster.jpg')
image=image.resize(1200,720)
image.save('nobody/poster.jpg','JPEG')
file1=open('nobody/actors.txt','r')
file2=open('nobody/actors0.txt','r')
realNames=[]
movieNames=[]
for i in file1:
    realNames.append(i.strip())
#print(realNames)
file1.close()
for i in file2:
    movieNames.append(i.strip())
file2.close()

#print(len(movieNames),len(realNames))
for i in range (0,13):
    image=Image.open('nobody/merged'+str(i)+'.jpg')

    draw=ImageDraw.Draw(image)

    text=realNames[i]+" as "+movieNames[i]
    #font=ImageFont.truetype('Roboto-Bold.ttf', size=45)
    font = ImageFont.truetype("arial.ttf", 45)
    color='rgb(50,250,200)'
    xPoint=int((1200-(len(text)*20))/2)
    (x,y)=(xPoint,650)
    draw.text((x,y),text,fill=color,font=font)
    image.save('nobody/merged'+str(i)+'.jpg')
