# coding=utf-8

import os 

#base_dir = '../NewsandTalks/'
base_dir = './data/NewsandTalks/'
k =1;


path = base_dir
dst_dir  = './data/Name/'
for filename in os.listdir(path):
        #os.system("mv %s %s"%(os.path.join(path,filename),os.path.join(path,str(k)+'.mp3')))
    os.system('cp "%s" "%s"'%(os.path.join(path,filename),os.path.join(dst_dir,str(k)+'.mp3')))
    k+=1
