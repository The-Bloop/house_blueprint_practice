import pymupdf

doc = pymupdf.open("basic_house.pdf")

#image w x h = 683 x 384

#This will append all the items into an array
def getItems():
    global doc
    items = []
    page = doc[0]
    paths = page.get_drawings()

    for path in paths:
        for item in path["items"]:
            items.append(item)
    
    return items

#This will append all the lines into an array:
#   skipFrame = True : Doesn't include the outline of the image.
def getLines(skipFrame):
    global doc
    items = []
    page = doc[0]
    paths = page.get_drawings()
    
    i = 0

    for path in paths:
        for item in path["items"]:
            if(item[0] == 'l'):
                if(skipFrame == False or i>3):
                    items.append(item)
                i += 1
    
    return items

def openPDF(fileName):
    global doc
    doc = pymupdf.open(fileName)

#if __name__ == "__main__":
#    openPDF("basic_house.pdf")
#    items = getItems()
#    print(items[0][2][0])
