def printer_error(s):
    unacceptable_symbols = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    count_errors = 0
    for k in s:
        for i in unacceptable_symbols:
            if k == i:
                count_errors += 1
    return str(count_errors) + "/" + str(len(s))