"""
 ----------------------------------------------------
  @Author: rinsa318
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2019-03-14 03:23:10
  @Last Modified by:   rinsa318
  @Last Modified time: 2019-03-14 17:09:21
 ----------------------------------------------------

  Usage:
   python main.py argvs[1] argvs[2]
  
   argvs[1]  :  src image   -->   style
   argvs[2]  :  target image



"""


import sys
import os
import cv2
import colortransfer as ct





## ------------------------------
## load arg
## ------------------------------
argvs = sys.argv
src_path = argvs[1]
tar_path = argvs[2]



## ------------------------------
## difine filename
## ------------------------------
filename_src, ext_src = os.path.splitext( os.path.basename(src_path) )
filename_tar, ext_tar = os.path.splitext( os.path.basename(tar_path) )
src_dir, filefullname_src = os.path.split( src_path )
tar_dir, filefullname_tar = os.path.split( tar_path )
## check name
print("source image --> " + filefullname_src)
print("target image --> " + filefullname_tar)


## for output
output_dir = "{0}/result/{1}".format(tar_dir, filename_tar)
if(not(os.path.exists(output_dir))):
  os.mkdir(output_dir)

output_path = "{0}/transfered_src_{1}_tar_{2}{3}".format(output_dir, filename_src, filename_tar, ext_tar)





## ------------------------------
## load image
## ------------------------------
src = cv2.imread(src_path, 1)
tar = cv2.imread(tar_path, 1)



## ------------------------------
## apply color transfer
## ------------------------------
transfered = ct.colortransfer(src, tar) 



## ------------------------------
# show and save result
## ------------------------------
print("save transfered image as --> {}".format(output_path))
# cv2.imshow(output_path, transfered)
cv2.imwrite(output_path, transfered)
# cv2.waitKey(0)
