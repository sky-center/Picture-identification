#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2,os,shutil
def check_image_is_vague(image, threshold=10):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    print('image vague is {}'.format(fm))
    if fm > threshold:
        return True
    return False

def get_suffix_file(dir, suffixs=None):
    special_suffix = suffixs or ['png','jpg']
    file_list = []
    for item in os.listdir(dir):
        item = os.path.join(dir, item)
        if os.path.isfile(item):
            for suffix in special_suffix:
                if item.endswith(suffix):
                    file_list.append(item)
                    break
        else:
            file_list.extend(get_suffix_file(item, suffixs=special_suffix))
    return file_list
if __name__ == '__main__':
    listmage = get_suffix_file('/Downloads/')
    TruelistDir="/Downloads/Trueimage/"
    FalselistDir="/Downloads/Falseimage/"
    BadlistDir="/Downloads/Badimage/"
    for mage in listmage:
        try:
            status = check_image_is_vague(mage)
            if status == True:
                shutil.copy(mage,TruelistDir)
            else:
                shutil.copy(mage,FalselistDir)
        except:
            shutil.copy(mage,BadlistDir)
