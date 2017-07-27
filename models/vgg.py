

def ConvBNReLUDrop(model, inputblob, outputblob,
                   input_dim, output_dim, drop_ration=None):
    inputblob = model.Conv(
        inputblob,
        outputblob,
        input_dim,
        output_dim,
        3,
        ('XavierFill', {}),
        ('ConstantFill', {}),
        stride = 1,
        pad = 1)
    inputblog = model.SpatialBN(inputblob,
                                str(inputblob) + 'bn',
                                output_dim, epsilon = 1e-3)
    inputblog = model.Relu(inputblob, inputblob)
    if drop_ratio:
        inputblob = model.Dropout(inputblob,
                                  str(inputblob) + 'dropout',
                                  ration = drop_ratio)
        return inputblob

def VGG(model, data):
    conv1 = ConvBNReLUDrop(model, data, 'conv1', 3, 64, drop_ratio)

