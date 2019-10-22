import os
os.chdir('/home/hoaithuong/PycharmProjects/multiple_fruits/Pineapple')
i=1
for file in os.listdir():
      src=file
      dst="pinea."+str(i)+".jpg"
      os.rename(src,dst)
      i+=1
