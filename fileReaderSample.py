file1=open('nobody/actors.txt','r')
realNames=[]
for i in file1:
    realNames.append(i.strip())
file1=open('nobody/actors0.txt','r')
movieNames=[]
for i in file1:
    movieNames.append(i.strip())
for i in range(0,len(realNames)):
    text=realNames[i]+" as "+movieNames[i]
    print(len(text))
