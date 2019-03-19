
def read_file(filename, search_blob):
    with open(filename, 'rb') as file_obj:
        ls = file_obj.read()
        if len(ls) == 0:
            return 0
        elif len(search_blob) == 0:
            return 1
        elif len(ls) == 0 and len(search_blob) == 0:
            return 1
        elif isinstance(search_blob, type(file_obj.read())):
            index_position = ls.find(search_blob)
            return "index_position", index_position
        else:
            return 0


    # index_position = ls.find(search_blob)
    # return "index_position", index_position
    # # data = file_obj.read().decode("hex")
    # # return data



print(read_file("download.png", b'>'))







with open("download.png", "rb") as file_obj:
    s = file_obj.read()
    print(s)
    stm = b'>'
    print("jknhjk",type(b'>'))
print(s.find(stm))