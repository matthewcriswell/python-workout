'''
joins stuff
'''

def anyjoin(myseq='cheeseburger', **kwargs):
    ''' joins a sequence with args in strange ways '''
    glue = ''
    keeb = ''
    if kwargs:
        for j in kwargs:
            glue = kwargs[j]
            keeb = j

    if isinstance(myseq, str):
        mutable_myseq = [*myseq]
    else:
        mutable_myseq = myseq

    output = []
    popper = str(mutable_myseq.pop())
    for i in mutable_myseq:
        output.append(str(i))
        if glue:
            output.append(str(glue))

    output.append(popper)
    if glue:
        output.insert(0, ': ')

    return keeb + ''.join(output)
