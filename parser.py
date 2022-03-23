def parse(txt):
    # checksum
    new_txt, checksum = txt[:-8], txt[-8:]
    if not validate_checksum(checksum):
        return None
    # parse text
    return rparse(new_txt)

def validate_checksum(checksum):
    return True # TODO add validate logic

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
    obj[field_no] = value

    # recursive
    return rparse(new_txt, obj)
