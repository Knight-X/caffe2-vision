import os
import os.path


IMG_FILETYPE = [
    '.jpg', '.JPG', '.jpeg', '.JPEG']

def is_image_file(img):
    for filetype in IMG_FILETYPE:
        if img.endswith(filetype):
            return True
    return False

def classes_maker(dirname):
    dirname = os.path.expanduser(dirname)
    classes = []
    for d in os.listdir(dirname):
        if os.path.isdir(os.path.join(dirname, d)):
            classes.append(d)

    class_idx = {classes[i]: i for i in range(len(classes))}
    return class_idx, classes

def dataset_maker(dirname, class_idx):
    imgs = []
    dirname = os.path.expanduser(dirname)
    for t_dir in sorted(os.listdir(dirname)):
        d = os.path.join(dirname, t_dir)
        if not os.path.isdir(d):
            continue

        for root, _, filename in sorted(os.walk(d)):
            for f in filename:
                if is_image_file(f):
                    path = os.path.join(root, f)
                    img_pair = (path, class_idx[t_dir])
                    imgs.append(img_pair)
    return imgs

class ImageFolder:
    def __init__(self, root):
        class_idx, classes = classes_maker(root)
        imgs = dataset_maker(root, class_idx)

        self.root = root
        self.imgs = imgs
        self.class_idx = class_idx

    def images(self):
        return self.imgs

    def __len__(self):
        return len(self.imgs)
