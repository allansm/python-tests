from allansm.downloader import getSource

code = getSource("https://www.google.com/search?q=python")
code = code.replace("\n","")
before = ""
find = ""
for n in code.split("<a "):
    if("href" in n and "/url?" in n):
        #print("<a "+n+"\n")
        
        for x in n.split("<div "):
            x = x.replace("\"","\n")
            x = x.replace("'","\n")
            x = x.replace("<","\n")
            x = x.replace(">","\n")
            #print(x.split("\n"))
            #print("")
            islink = False
            isText = False
            if(x.split("\n")[0] == "href="):
                islink = True
            if(islink):
                print(">>>>>>> "+x.split("\n")[1])
            else:
                for y in x.split("\n"):
                    if("/h3" in y or "/a" in y):
                        isText = True
                if(isText):
                    print(">>>>>>>> "+x.split("\n")[3])
            #for y in x.split("\n"):
                
            '''
            for y in x.split("\n"):
                if("href=" in before):
                    print(y+"\n\n")
                elif("h3 " in before):
                   find = y
                    #if(y != ""):
                    #print(y+"\n\n")
                    #exit()
                elif(find in before and find != ""):
                    print(y+"\n")
                    exit()
                #else:
                    #print(before)
                
                before = y'''
