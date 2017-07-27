# caffe2-vision

 This is the util for making image dataset for Caffe2 . 

## Datasets Module:
  It will search and load images from folder, and help to create the dataset easily .

  * ImageFolder
  * ImageLoader

  ### ImageFolder
  ```
  rootfolder/boat/xxx.jpg
  rootfolder/boat/123.jpg
  rootfolder/boat/456.jpg

  rootfolder/car/123.jpg
  rootfolder/car/456.jpg
  rootfolder/car/cjf.jpg
  ```

  ```
  import imgfolder as folder
  import imgloader as loader
  dataset = folder.ImageFolder("your file path")
  imgs = loader.ImgLoader(dataset)      
  ```

  ##### imgs is the list contains (index,images(img_data, label_data))

  ```
  for i, data in enumerate(imgs):
        img_data, label_data = data
  ```

## DB Writer
  - minidb

## Models
  - ResNet




This is inspired by pytorch/vision.
