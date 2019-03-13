"""
 ----------------------------------------------------
  @Author: tsukasa
  @Affiliation: Waseda University
  @Email: rinsa@suou.waseda.jp
  @Date: 2018-06-19 16:09:45
  @Last Modified by:   rinsa318
  @Last Modified time: 2019-03-14 03:29:58
 ----------------------------------------------------

  Usage:
   python colortransfer.py argvs[1] argvs[2] argvs[3]...
  
   argvs[1]  :  src image   -->   style
   argvs[2]  :  target image

"""



import numpy as np
import cv2
import sys
import os


def image_stats(image):

  ### compute the mean and standard deviation of each channel
  (l, a, b) = cv2.split(image)
  (lMean, lStd) = (l.mean(), l.std())
  (aMean, aStd) = (a.mean(), a.std())
  (bMean, bStd) = (b.mean(), b.std())
 
  return (lMean, lStd, aMean, aStd, bMean, bStd)





def colortransfer(src, tar):


  ### 1. convert bgr image array(opencv) to lab color
  source = cv2.cvtColor(src, cv2.COLOR_BGR2LAB).astype("float32")
  target = cv2.cvtColor(tar, cv2.COLOR_BGR2LAB).astype("float32")




  ### 2. compute the mean and standard deviation of each channel
  (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
  (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)



  ### 3. apply color transfer
  print("start color transfer")

  ## subtract the means from the target image
  (l, a, b) = cv2.split(target)
  l -= lMeanTar
  a -= aMeanTar
  b -= bMeanTar

  ## scale by the standard deviations
  l = (lStdTar / (lStdSrc + 1e-8)) * l
  a = (aStdTar / (aStdSrc + 1e-8)) * a
  b = (bStdTar / (bStdSrc + 1e-8)) * b

  ## add in the source mean
  l += lMeanSrc
  a += aMeanSrc
  b += bMeanSrc

  ## have to scale array 0 to 255
  l = scaled = np.clip(l, 0, 255)
  a = scaled = np.clip(a, 0, 255)
  b = scaled = np.clip(b, 0, 255)
  # l = scale_array(l)
  # a = scale_array(a)
  # b = scale_array(b)

  ## merge the channels together and convert back to the RGB color space
  ## note: If image consist of gray scale, only l space will transfer 
  if((aMeanSrc == 128.0 and bMeanSrc == 128.0) or (aMeanTar == 128.0 and bMeanTar == 128.0)):
    a_gray = np.ones((tar.shape[0], tar.shape[1]), dtype=np.float32) * 128.0
    b_gray = np.ones((tar.shape[0], tar.shape[1]), dtype=np.float32) * 128.0
    transfer = cv2.merge([l, a_gray, b_gray])
    transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)
  
  else:
    transfer = cv2.merge([l, a, b])
    transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)
  

  print("-------> done!!!!")


  return transfer







def main():


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
  path_src, filefullname_src = os.path.split( src_path )
  path_tar, filefullname_tar = os.path.split( tar_path )
  output_path = "{0}/transfered_src_{1}_tar_{2}{3}".format(path_tar, filename_src, filename_tar, ext_tar)

  ## check name
  print("source image --> " + filefullname_src)
  print("target image --> " + filefullname_tar)



  ## ------------------------------
  ## load image
  ## ------------------------------
  src = cv2.imread(src_path, 1)
  tar = cv2.imread(tar_path, 1)



  ## ------------------------------
  ## apply color transfer
  ## ------------------------------
  transfered = colortransfer(src, tar) 



  ## ------------------------------
  # show and save result
  ## ------------------------------
  print("save transfered image as --> {}".format(output_path))
  cv2.imshow(output_path, transfered)
  cv2.imwrite(output_path, transfered)
  cv2.waitKey(0)




# main()


