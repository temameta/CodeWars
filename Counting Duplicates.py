def duplicate_count(text):
    count = 0
    scanned = []
    for k in range(0,len(text)):
        for i in range(k+1,len(text)):
            if (text[k] == text[i].lower() or text[k] == text[i].upper()) and not(text[k] in scanned) :
                scanned.append(text[k].lower())
                scanned.append(text[k].upper())
                count+=1
    return count
     
print(duplicate_count("Indivisibilities"))
        
