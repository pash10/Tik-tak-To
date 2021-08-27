theBored = {
    "7": "", "8" : "", "9":"",
    "4": "","5" : "","6":"",
    "1":"","2":"", "3":""
}

def printBord():
    print(theBored["7"] + " |" + theBored["8"] + "  | " + theBored["9"])
    print("-+--+-")
    print(theBored["4"] + " |" + theBored["5"] + "  | " + theBored["6"])
    print("-+--+-")
    print(theBored["1"] + " |" + theBored["2"] + "  | " + theBored["3"])

def main(thebored):
 trun = "x"
 comp = "0"
 count = 0
 print(trun)
 printBord()
 stop = False
 print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
 while count < 9 and stop == False:
     coninte = True
     if trun == "x":
         temp = input("Choose number betten 1-9=> ")
         if thebored[temp] != "":
             conti = False
             while conti == False:
                 tempA = input("Choose number betten 1-9=> ")
                 if thebored[tempA] =="":
                     thebored[tempA] = "x"
                     count+=1
                     if winOrNot(trun,theBored) == True:
                         stop = True
                         printBord()
                         break
                     trun ="o"
         elif thebored[temp] =="":
             thebored[temp] ="x"
             if winOrNot(trun,theBored) == True:
                 stop = True
                 printBord()
                 break
             trun ="o"
             count+=1
     if trun == "o" and count <9:
         if compWin(theBored) == False:
             if compStop(theBored) == False:
                 compSet(theBored)
                 if winOrNot(trun,theBored) == True:
                    stop= True
                    printBord()
                    break
         trun = "x"
         count+=1
     print(trun)
     printBord()
     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("It a tie")

def winOrNot(trun,thebored):
    if thebored["7"] ==trun and thebored["5"] == trun and thebored["3"] == trun:
        print(trun + " won")  
        return True
    if thebored["1"] == trun and thebored["5"] == trun and thebored["9"] == trun:
       print(trun + " won")
       return True
    if thebored["7"] == trun and thebored["4"] == trun and thebored["1"] == trun:
        print(trun + " won")
        return True
    if thebored["8"] == trun and thebored["5"] == trun and thebored["2"] == trun:
        print(trun + " won")
        return True
    if thebored["9"] == trun and thebored["6"] == trun and thebored["3"] == trun:
        print(trun + " won")
        return True
    if thebored["7"] == trun and thebored["8"] == trun and thebored["9"] == trun:
        print(trun + " won")
        return True
    if thebored["4"] == trun and thebored["5"] == trun and thebored["6"] ==trun:
        print(trun + " won")
        return True
    if thebored["1"] == trun and thebored["2"] == trun and thebored["3"] == trun:
        print(trun + " won")
        return True 
         
def compSet(thebored):
    import random
    temp =0
    cont = True
    if thebored["5"] == "":
        thebored["5"] = "o"
    
    elif thebored["5"] !="":
        while cont == True:
            temp =random.randrange(1,9)
            tempA = str(temp)
            if thebored[tempA] == "":
                thebored[tempA] = "o"
                cont = False
                break
            
def compStop(thebored):
 if thebored["7"] == "x" and thebored["4"] == "x" and thebored["1"] =="":
     theBored["1"] = "o"
 elif thebored["7"] == "x" and thebored["4"] == "" and thebored["1"] =="x":
     theBored["4"] ="o"
 elif thebored["7"] == "" and thebored["4"] =="x" and thebored["1"] =="x":
     theBored["7"] ="o"
 elif thebored["8"] == "x" and thebored["5"] =="x" and thebored["2"] =="":
     theBored["2"] ="o"
 elif thebored["8"] == "" and thebored["5"] =="x" and thebored["2"] =="x":
     theBored["8"] ="o"
 elif thebored["8"] == "x" and thebored["5"] =="" and thebored["2"] =="x":
     theBored["5"] ="o"
 elif thebored["9"] == "x" and thebored["6"] =="x" and thebored["3"] =="":
     theBored["3"] ="o"
 elif thebored["9"] == "" and thebored["6"] =="x" and thebored["3"] =="x":
     theBored["9"] ="o"
 elif thebored["9"] == "x" and thebored["6"] =="" and thebored["3"] =="x":
     theBored["6"] ="o"
 elif thebored["7"] == "x" and thebored["8"] =="x" and thebored["9"] =="":
     theBored["9"] ="o"
 elif thebored["7"] == "" and thebored["8"] =="x" and thebored["9"] =="x":
     theBored["7"] ="o"
 elif thebored["7"] == "x" and thebored["8"] =="" and thebored["9"] =="x":
     theBored["8"] ="o"
 elif thebored["4"] == "x" and thebored["5"] =="x" and thebored["6"] =="":
     theBored["6"] ="o"
 elif thebored["4"] == "" and thebored["5"] =="x" and thebored["6"] =="x":
     theBored["4"] ="o"
 elif thebored["4"] == "x" and thebored["5"] =="" and thebored["6"] =="x":
     theBored["5"] ="o"
 elif thebored["1"] == "x" and thebored["2"] =="x" and thebored["3"] =="":
     theBored["3"] ="o"
 elif thebored["1"] == "x" and thebored["2"] =="" and thebored["3"] =="x":
     theBored["2"] ="o"
 elif thebored["1"] == "" and thebored["2"] =="x" and thebored["3"] =="x":
     theBored["1"] ="o"
 elif thebored["7"] == "x" and thebored["5"] =="x" and thebored["3"] =="":
     theBored["3"] ="o"
 elif thebored["7"] == "x" and thebored["5"] =="" and thebored["3"] =="x":
     theBored["5"] ="o"
 elif thebored["7"] == "" and thebored["5"] =="x" and thebored["3"] =="x":
     theBored["7"] ="o"
 elif thebored["9"] == "x" and thebored["5"] =="x" and thebored["1"] =="":
     theBored["1"] ="o"
 elif thebored["9"] == "x" and thebored["5"] =="" and thebored["1"] =="x":
     theBored["5"] ="o"
 elif thebored["9"] == "" and thebored["5"] =="x" and thebored["1"] =="x":
     theBored["9"] ="o"
 else:
    return False

def compWin(thebored):
 if thebored["7"] == "o" and thebored["4"] == "o" and thebored["1"] =="":
     thebored["1"] = "o"
 elif thebored["7"] == "o" and thebored["4"] == "" and thebored["1"] =="o":
     thebored["4"] ="o"
 elif thebored["7"] == "" and thebored["4"] =="o" and thebored["1"] =="o":
     thebored["7"] ="o"
 elif thebored["8"] == "o" and thebored["5"] =="o" and thebored["2"] =="":
     thebored["2"] ="o"
 elif thebored["8"] == "" and thebored["5"] =="o" and thebored["2"] =="o":
     thebored["8"] ="o"
 elif thebored["8"] == "o" and thebored["5"] =="" and thebored["2"] =="o":
     thebored["5"] ="o"
 elif thebored["9"] == "o" and thebored["6"] =="o" and thebored["3"] =="":
     thebored["3"] ="o"
 elif thebored["9"] == "" and thebored["6"] =="o" and thebored["3"] =="o":
     thebored["9"] ="o"
 elif thebored["9"] == "o" and thebored["6"] =="" and thebored["3"] =="o":
     thebored["6"] ="o"
 elif thebored["7"] == "o" and thebored["8"] =="o" and thebored["9"] =="":
     thebored["9"] ="o"
 elif thebored["7"] == "" and thebored["8"] =="o" and thebored["9"] =="o":
     thebored["7"] ="o"
 elif thebored["7"] == "o" and thebored["8"] =="" and thebored["9"] =="o":
     thebored["8"] ="o"
 elif thebored["4"] == "o" and thebored["5"] =="o" and thebored["6"] =="":
     thebored["6"] ="o"
 elif thebored["4"] == "" and thebored["5"] =="o" and thebored["6"] =="o":
     thebored["4"] ="o"
 elif thebored["4"] == "o" and thebored["5"] =="" and thebored["6"] =="o":
     thebored["5"] ="o"
 elif thebored["1"] == "o" and thebored["2"] =="o" and thebored["3"] =="":
     thebored["3"] ="o"
 elif thebored["1"] == "o" and thebored["2"] =="" and thebored["3"] =="o":
     thebored["2"] ="o"
 elif thebored["1"] == "" and thebored["2"] =="o" and thebored["3"] =="o":
     thebored["1"] ="o"
 elif thebored["7"] == "o" and thebored["5"] =="o" and thebored["3"] =="":
     thebored["3"] ="o"
 elif thebored["7"] == "o" and thebored["5"] =="" and thebored["3"] =="o":
     thebored["5"] ="o"
 elif thebored["7"] == "" and thebored["5"] =="o" and thebored["3"] =="o":
     thebored["7"] ="o"
 elif thebored["9"] == "o" and thebored["5"] =="o" and thebored["1"] =="":
     thebored["1"] ="o"
 elif thebored["9"] == "o" and thebored["5"] =="" and thebored["1"] =="o":
     thebored["5"] ="o"
 elif thebored["9"] == "" and thebored["5"] =="o" and thebored["1"] =="o":
     thebored["9"] ="o"
 else:
     return False
     
main(theBored)