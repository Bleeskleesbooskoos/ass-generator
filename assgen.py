from math import floor

# GET YO ASS COOKED
def shartAss(assNum):
    assnNum = floor(abs(assNum))
    if assnNum == 0:
        print("GET YO ASS OUTTA HERE!")
        return None
    else:
        print("ASS!")
        return shartAss(assnNum - 1)
    
shartAss(69)
