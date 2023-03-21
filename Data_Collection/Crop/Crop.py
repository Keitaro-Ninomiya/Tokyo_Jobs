{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62d4cc28-ad32-4611-8627-90eeab27efcc",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Crop:\n",
    "    def __init__(self,im):\n",
    "        self.im=im\n",
    "\n",
    "    def Crop_UR(self,im):\n",
    "        width,height=im.size\n",
    "        left=width/2\n",
    "        top=0\n",
    "        right=0.9*width\n",
    "        bottom=1.15*height/3\n",
    "        im=im.crop((left,top,right,bottom))\n",
    "        im = im.save(\"Test.jpg\")\n",
    "\n",
    "    def Crop_MR(self,im):\n",
    "        width,height=im.size\n",
    "        left=width/2\n",
    "        top=1.15*height/3\n",
    "        right=width\n",
    "        bottom=1.95*height/3\n",
    "        im1=im.crop((left,top,right,bottom))\n",
    "        im1 = im1.save(\"Test.jpg\")\n",
    "\n",
    "    def Crop_BR(self,im):\n",
    "        width,height=im.size\n",
    "        left=width/2\n",
    "        right=0.9*width\n",
    "        top=1.95*height/3\n",
    "        bottom=0.95*height\n",
    "        im1=im.crop((left,top,right,bottom))\n",
    "        im1 = im1.save(\"Test.jpg\")\n",
    "\n",
    "    def Crop_UL(self,im):\n",
    "        width,height=im.size\n",
    "        left=0.1*width\n",
    "        right=width/2\n",
    "        top=0\n",
    "        bottom=1.15*height/3\n",
    "        im=im.crop((left,top,right,bottom))\n",
    "        im = im.save(\"Test.jpg\")\n",
    "\n",
    "    def Crop_ML(self,im):\n",
    "        width,height=im.size\n",
    "        left=0.1*width\n",
    "        right=width/2\n",
    "        top=1.15*height/3\n",
    "        bottom=1.95*height/3\n",
    "        im1=im.crop((left,top,right,bottom))\n",
    "        im1 = im1.save(\"Test.jpg\")\n",
    "\n",
    "    def Crop_BL(self,im):\n",
    "        width,height=im.size\n",
    "        left=0.1*width\n",
    "        right=width/2\n",
    "        top=1.95*height/3\n",
    "        bottom=0.95*height\n",
    "        im1=im.crop((left,top,right,bottom))\n",
    "        im1 = im1.save(\"Test.jpg\")"
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
