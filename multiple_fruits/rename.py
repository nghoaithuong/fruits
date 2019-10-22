import os
os.chdir('/home/hoaithuong/PycharmProjects/multiple_fruits/Peach')
i=1
for file in os.listdir():
      src=file
      dst="peach."+str(i)+".jpg"
      os.rename(src,dst)
      i+=1
