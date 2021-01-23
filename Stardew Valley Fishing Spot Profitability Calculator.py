with open("Fish Data.txt", "r") as file:
    bob = file.read()

#print(bob)
def average(inputlist):
    try:
        output = sum(inputlist)/len(inputlist)
    except:
        output = "not defined"
    finally:
        return output


List1 = bob.split("\n")

List2=[]


for season in ["spring","summer","fall","winter"]:
    for weather in ["clear","rainy"]:
        for location in ["calico desert","forest pond","forest river","ginger island ocean","ginger island pirate cove","gi pond","gi river","mines 100f","mines 20f","mines 60f","mountain lake","mutant bug lair","ocean","secret woods pond","the sewers","town river","volcano caldera","witchs swamp"]:
            templist = []
            for item in List1:
                item = item.split("|")
                if season in item and location in item and weather in item:
                    price = int(item[0])
                    templist.append(price)
            List2.append([season+" "+location+" "+weather,average(templist)])
#print(List2)
#print(average(List2))
for item in List2:
    print(item)