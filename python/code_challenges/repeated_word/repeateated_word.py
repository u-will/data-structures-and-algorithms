def repeate (paragraph):
    List = []
    paragraphList = paragraph.split()
    print(paragraphList)
    for word in paragraphList:
        if List.__contains__(word.lower()):
            return  word.lower()
        List.append(word.lower())
    return ''

repeate ('Once upon a time in a castle')
