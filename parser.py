def parse(txt):
    # checksum
    new_txt, checksum = txt[:-8], txt[-8:]
    if not validate_checksum(checksum):
        return None
    # parse text
    return rparse(new_txt)

def validate_checksum(checksum):
    return True # TODO add logic

def detect_nested_block(value):
    return False # TODO add logic

def rparse(txt, obj={}):

    # end of text
    if not txt:
        return obj

    # extract data from text
    field_no = txt[:2]
    size = int(txt[2:4])
    value = txt[4:4+size]
    new_txt = txt[4+size:]

    # validate value
    if size != len(value):
        return None

    # update object
    if detect_nested_block(value):
        obj[field_no] = rparse(value)
    else:
        obj[field_no] = value

    # recursive
    return rparse(new_txt, obj)