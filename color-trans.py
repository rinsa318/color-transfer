"""
 ----------------------------------------------------
  @Author: tsukasa
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2018-06-19 16:09:45
  @Last Modified by:   tsukasa
  @Last Modified time: 2018-06-19 17:15:23
 ----------------------------------------------------

  Usage:
   python color-trans.py argvs[1] argvs[2] argvs[3]...
  
   argvs[1]  :  src image   -->   style
   argvs[2]  :  target image

"""



import numpy as np
import cv2
import sys
import os


def image_stats(image):

  # compute the mean and standard deviation of each channel
  # --------------------------
  # create new function!!
  # |
  # v
  # --------------------------


  # return the color statistics
  return (lMean, lStd, aMean, aStd, bMean, bStd)



def scale_array(arr):

  # NumPy array that has been scaled to be in [0, 255] range

  # --------------------------
  # create new function!!
  # |
  # v
  # --------------------------

  return scaled_arr




## ------------------------------
## load arg
## ------------------------------
argvs = sys.argv
src = argvs[1]
tar = argvs[2]





## ------------------------------
## difine filename
## ------------------------------
filename_src, ext_src = os.path.splitext( os.path.basename(src) )
filename_tar, ext_tar = os.path.splitext( os.path.basename(tar) )
path_src, filefullname_src = os.path.split( src )
path_tar, filefullname_tar = os.path.split( tar )
output = os.path.join(path_src + '/result_src_' + filename_src + '_tar_' + filename_tar + ext_src)

# check name
print("src --> " + filefullname_src)
print("src --> " + filefullname_tar)





## ------------------------------
# load image as lab color
## ------------------------------
source = cv2.cvtColor(cv2.imread(src), cv2.COLOR_BGR2LAB).astype("float32")
target = cv2.cvtColor(cv2.imread(tar), cv2.COLOR_BGR2LAB).astype("float32")




## ------------------------------
# calculate std each channel
## ------------------------------

# ---------------------------------
# youn have to create new function here
# |
# v
#
# compute the mean and standard deviation of each channel
# like -->
# (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
# (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)
#
# ---------------------------------



## ------------------------------
# apply color transfer
## ------------------------------
print("start color transfer")
# subtract the means from the target image
(l, a, b) = cv2.split(target)
l -= lMeanTar
a -= aMeanTar
b -= bMeanTar

# scale by the standard deviations
l = (lStdTar / lStdSrc) * l
a = (aStdTar / aStdSrc) * a
b = (bStdTar / bStdSrc) * b

# add in the source mean
l += lMeanSrc
a += aMeanSrc
b += bMeanSrc


# ---------------------------------
# youn have to create new function here
# |
# v

# you have to scale array 0 to 255
# like -->
#l = scale_array(l)
#a = scale_array(a)
#b = scale_array(b)

# ---------------------------------


# merge the channels together and convert back to the RGB color
# space, being sure to utilize the 8-bit unsigned integer data type
transfer = cv2.merge([l, a, b])
transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)
print("-------> done!!!!")
print("")
print("")




## ------------------------------
# show and save result
## ------------------------------
print("save output as --> " + output)
cv2.imshow(output, transfer)
cv2.imwrite(output, transfer)
cv2.waitKey(0)


