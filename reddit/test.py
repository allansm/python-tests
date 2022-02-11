from allansm.util import getJson

def body(text,start=""):
    text = text.replace("\n","\n"+start)

    print(start,end="")
    
    i=0
    for n in text:
        if(i == 50):
            print("\n"+start,end="")
            i=0
        else:
            print(n,end="")
            i+=1


q = input("search:")
q = q.replace(" ","+")

result = getJson("https://www.reddit.com/search/.json?q="+q)

i = 0
for n in result["data"]["children"]:
    print(str(i)+": "+n["data"]["title"])
    print("comments:"+str(n["data"]["num_comments"]))
    print("")

    i+=1

index = int(input("n:"))
result = getJson("https://www.reddit.com"+result["data"]["children"][index]["data"]["permalink"]+".json")

print(result[0]["data"]["children"][0]["data"]["title"])
print(result[0]["data"]["children"][0]["data"]["selftext"])
print("")

for n in result[1]["data"]["children"]:
    print(n["data"]["author"]+":\n")
    body(n["data"]["body"],"")
    
    print("\n")
    try:
        for replies in n["data"]["replies"]["data"]["children"]:
            print("\t"+replies["data"]["author"]+":\n")
            body(replies["data"]["body"],"\t")

            print("\n")
        print("")
    except:
        dummy=0
