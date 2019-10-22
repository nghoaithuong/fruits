import os
os.chdir('/home/hoaithuong/PycharmProjects/multiple_fruits/Blueberry')
i=1
for file in os.listdir():
      src=file
      dst="blueberry."+str(i)+".jpg"
      os.rename(src,dst)
      i+=1
