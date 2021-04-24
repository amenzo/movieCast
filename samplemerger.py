from PIL import Image
image1=Image.open('nobody/0.jpg')
image2=Image.open('nobody/0.1.jpg')
width=320
height=960

image1=image1.resize((width,height))
image2=image2.resize((width,height))

newImage=Image.new('RGB',(2*width,height),(250,250,250))
newImage.paste(image1,(0,0))
newImage.paste(image2,(image1.size[0],0))
newImage=newImage.resize((640,960))
newImage.save('nobody/mergednew0.jpg','JPEG')
