import pymupdf

doc = pymupdf.open("basic_house.pdf")

#image w x h = 683 x 384

def getItems():
    global doc
    items = []
    page = doc[0]
    paths = page.get_drawings()

    for path in paths:
        for item in path["items"]:
            items.append(item)
    
    return items

def getLines():
    global doc
    items = []
    page = doc[0]
    paths = page.get_drawings()

    for path in paths:
        for item in path["items"]:
            if(item[0] == 'l'):
                items.append(item)
    
    return items

def openPDF(fileName):
    global doc
    doc = pymupdf.open(fileName)

#if __name__ == "__main__":
#    openPDF("basic_house.pdf")
#    items = getItems()
#    print(items[0][2][0])
