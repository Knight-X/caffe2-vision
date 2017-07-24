# caffe2-vision


This is the util for making image dataset. 


Usage:
  import imgfolder as folder
  import imgloader as loader

  dataset = folder.ImageFolder("your file path")
  imgs = loader.ImgLoader(dataset)

  imgs is the list contains (index, images(img_data, label_data))

  for i, data in enumerate(imgs):
     img_data, label_data = data


This is inspired by pytorch/vision.
