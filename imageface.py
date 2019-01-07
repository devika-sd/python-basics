{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "facecase=cv2.CascadeClassifier(\"haarcascade_frontalface_default.xml\")\n",
    "img=cv2.imread(\"/media/devika/01D45E0FB94A6D50/p5l/my collection/quotes/12898351_245505382456829_1244158023359260704_o.jpg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "cv2.imshow(\"face\",img)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "error",
     "evalue": "/home/travis/miniconda/conda-bld/conda_1486587069159/work/opencv-3.1.0/modules/objdetect/src/cascadedetect.cpp:1639: error: (-215) !empty() in function detectMultiScale\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31merror\u001b[0m                                     Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-00cac8c20dfa>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mgrayimg\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcv2\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcvtColor\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimg\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mcv2\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCOLOR_BGR2GRAY\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mface\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfacecase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdetectMultiScale\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mgrayimg\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mscaleFactor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1.05\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mminNeighbors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31merror\u001b[0m: /home/travis/miniconda/conda-bld/conda_1486587069159/work/opencv-3.1.0/modules/objdetect/src/cascadedetect.cpp:1639: error: (-215) !empty() in function detectMultiScale\n"
     ]
    }
   ],
   "source": [
    "grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
    "face=facecase.detectMultiScale(grayimg,scaleFactor=1.05,minNeighbors=5)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
