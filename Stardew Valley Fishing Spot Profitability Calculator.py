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
        for location in ["ocean","town river","forest river","mountain lake","forest pond","secret woods pond","the sewers","witch's swamp","ginger island ocean","mines 20f","mines 60f","mines 100f","volcano caldera","calico desert","ginger island pond","ginger island river","mutant bug lair","ginger island pirate cove"]:
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