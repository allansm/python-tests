from allansm.util import getJson

q = input("search:")
q = q.replace(" ","+")

result = getJson("https://www.reddit.com/search/.json?q="+q)

i = 0
for n in result["data"]["children"]:
    print(str(i)+":"+n["data"]["title"])
    print("comments:"+str(n["data"]["num_comments"]))
    print("")

    i+=1

index = int(input("n:"))
result = getJson("https://www.reddit.com"+result["data"]["children"][index]["data"]["permalink"]+".json")

print(result[0]["data"]["children"][0]["data"]["title"])
print(result[0]["data"]["children"][0]["data"]["selftext"])
print("")

for n in result[1]["data"]["children"]:
    print(n["data"]["author"]+":")
    print("\t"+n["data"]["body"])
    
    try:
        for x in n["data"]["replies"]:
            for replies in x["data"]["children"]:
                print("\t\t"+replies["data"]["body"])
    except:
        dummy=0
    
    print("") 
