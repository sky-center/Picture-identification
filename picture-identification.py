
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
                         break
        else:
            file_list.extend(get_suffix_file(item, suffixs=special_suffix))
    return file_list

def list_of_groups(init_list, children_list_len):
    list_of_groups = zip(*(iter(init_list),) *children_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % children_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list

if __name__ == '__main__':
    listmage = get_suffix_file('/Downloads/image/')
    TruelistDir="/Downloads/image/Trueimage/"
    FalselistDir="/Downloads/image/Falseimage/"
    Badimagedir="/Downloads/image/Badimage/"
    Trueimagelist = []
    Falseimagelist = []
    for mage in listmage:
        try:
            status = check_image_is_vague(mage)
            if status == True:
                Trueimagelist.append(mage)
            else:
                Falseimagelist.append(mage)
        #except cv2.error:
        except Exception:
            shutil.copy(mage, Badimagedir)

    truelist_len = round(len(Trueimagelist)/8) + 1
    truelist = list_of_groups(Trueimagelist,truelist_len)
    for truenum in truelist:
        trueflag = truelist.index(truenum)
        truetempdir=TruelistDir + "{}/".format(trueflag)
        #print(truetempdir)
        os.mkdir(truetempdir)
        for trueimage in truenum:
            shutil.copy(trueimage, truetempdir)

    falselist_len = round(len(Falseimagelist)/8) + 1
    falselist =list_of_groups(Falseimagelist,falselist_len)
    for falsenum in falselist:
        falseflag=falselist.index(falsenum)
        falsetempdir = FalselistDir + "{}/".format(falseflag)
        os.mkdir(falsetempdir)
        for falseimage in falsenum:
            shutil.copy(falseimage, falsetempdir)

