import art
import os

print(art.logo)

bids={}

flag=True
while flag == True:
    name=input("Enter you name:")
    
    try:
        bid=int(input("What is your bid?:"))
        
    except ValueError:
        bid=int(input("Please enter a valid bid:"))
    
    #write a logic such that only an integer value is accepted--------(future scope)
    bids[name]=bid
    #print(bids)
    response=input("\n\nAre there any other players?\n").lower()
    if response == "yes":
        os.system('cls')
        flag = True
    else:
        print("\nGame ended!")
        max_bid=max(bids.values())
        print(f"The highest bid is {max_bid}!\n\n")
        
        #make a list of key and values separately
        highest_bidder=max(bids, key=bids.get)
        print(f"The winner is {highest_bidder}!")
        #logic such that if there are two highest values, all of 'em win-----(future scope)
        flag=False
