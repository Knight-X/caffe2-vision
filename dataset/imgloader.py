import skimage
import numpy as np
import skimage.io as io
import skimage.transform

class RandomSampler:
    def __init__(self, data_source):
        self.data_source = data_source
    def __iter__(self):
        return iter(np.random.permutation(len(self.data_source)))

def image_loader(filepath):
    img = skimage.img_as_float(skimage.io.imread(filepath)).astype(np.float32)

    return img 

class ImgLoaderIter(object):
    def __init__(self, loader):
        self.sample_iter = iter(loader.sampler)
        self.loader = loader
    def __next__(self):
        idx = next(self.sample_iter)

        return self.loader.getitem(idx)
    next = __next__

class ImgLoader(object):
    def __init__(self, dataset, transform = None, loader = image_loader, sampler = RandomSampler):
        self.dataset = dataset
        self.transform = transform
        self.loader = loader 
        self.sampler = sampler(dataset) 

    def getitem(self, idx):
        dataset = self.dataset.images()

        img, label = dataset[idx]

        img_l = self.loader(img)
        img_l = skimage.transform.resize(img_l, [28, 28], mode = "reflect")
        img_l = img_l.swapaxes(1, 2).swapaxes(0, 1)
        img_l = img_l[(2, 1, 0), :, :]
        pair = (img_l, label)
        return pair

    def __iter__(self):
        return ImgLoaderIter(self)
