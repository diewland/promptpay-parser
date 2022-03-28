def parse(txt):
    # checksum
    new_txt, checksum = txt[:-8], txt[-8:]
    if not validate_checksum(checksum):
        return None
    # parse text
    return rparse(new_txt)

def validate_checksum(checksum):
    return True # TODO add logic

def extract_block_data(txt):
    field_no = txt[:2]
    size = int(txt[2:4])
    value = txt[4:4+size]
    next_txt = txt[4+size:]
    return field_no, size, value, next_txt

def detect_block(txt):
    idx = 0
    while idx < len(txt):
        new_txt = txt[idx:]
        try:
            _, size, value, _ = extract_block_data(new_txt)
        except:
            return False
        if size <= 0 or size != len(value):
            return False
        idx += 4 + size
    new_txt = txt[idx:]
    if not new_txt:
        return True
    else:
        return False

def rparse(txt):
    obj = {}
    idx = 0
    while idx < len(txt):
        new_txt = txt[idx:]
        field_no, size, value, _ = extract_block_data(new_txt)
        if detect_block(value):
            obj[field_no] = rparse(value)
        else:
            obj[field_no] = value
        idx += 4 + size
    return obj