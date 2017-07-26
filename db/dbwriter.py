

class DB:
    def __init__(self, db_type, db_name):
        self.dbtype = db_type
        self.dbname = db_name

    def writedb(features, labels, datatype='train'):
        trans_s = datatype + '_%3d'
        db = core.C.create_db(db_type, db_name, core.C.Mode.write)
        transaction = db.new_transaction()
        for i in range(features.shape[0]):
            feature_and_label = caffe2_pb2.TensorProtos()
            feature_and_label.protos.extend([
                utils.NumpyArrayToCaffe2Tensor(features[i]),
                utils.NumpyArrayToCaffe2Tensor(labels[i])])
            transaction.put(
                trans_s.format(i),
                feature_and_label.SerializeToString())
        del transaction
        del db
                                                            
