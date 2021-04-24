from PIL import Image

for i in range(0,13):
    image1=Image.open('nobody/'+str(i)+'.jpg')
    image2=Image.open('nobody/'+str(i)+'.1.jpg')

    width=int((image1.size[0]+image2.size[0])/2)
    height=int((image1.size[1]+image2.size[1])/2)

    width=600
    height=360

    image1=image1.resize((width,height))
    image2=image2.resize((width,height))

    newImage=Image.new('RGB',(2*width,height),(250,250,250))
    newImage.paste(image1,(0,0))
    newImage.paste(image2,(image1.size[0],0))
    newWidth=int(0.75*newImage.size[0])
    newHeight=int(1*newImage.size[1])
    newImage=newImage.resize((1200,720))
    newImage.save('nobody/merged'+str(i)+'.jpg','JPEG')
