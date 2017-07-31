from caffe2.proto import caffe2_pb2
def splitmodel(prednet, initnet, target):
    lookup = {}
    forward = False
    for layer in prednet.op:
        for inop in layer.input:
            tmp = ""
            for outop in layer.output:
                tmp = outop if forward else inop

                if forward:
                    if inop in lookup:
                        lookup[inop].append(tmp)
                    else:
                        lookup[inop] = []
                        lookup[inop].append(tmp)
                else:
                    if outop in lookup:
                        lookup[outop].append(tmp)
                    else:
                        lookup[outop] = []
                        lookup[outop].append(tmp)


    res = []
    step = [target]
    print target
    while len(step):
        next_i = []
        for l in step:
            if l not in res:
                res.append(l)
                if l in lookup:
                    for g in lookup[l]:
                        next_i.append(g)
        step = next_i
    
    second = caffe2_pb2.NetDef()
    second.name = "gy"
    for op in prednet.op:
        if op.output[0] in res:
            new_op = second.op.add()
            new_op.CopyFrom(op)
            
    secondinit = caffe2_pb2.NetDef()
    secondinit.name = "gyinit"
    for op in initnet.op:
        if op.output[0] in res:
            new_op = secondinit.op.add()
            new_op.CopyFrom(op)
            
    for ins in initnet.external_output:
        if ins in res:
            g = secondinit.external_output
            g.append(ins)
    g = second.external_output
    g.append(target)
    
    for ins in prednet.external_input:
        if ins in res:
            g = second.external_input
            g.append(ins)

    for ins in prednet.external_output:
        if ins in res:
            g = second.external_output
            g.append(ins)
    return second, secondinit

