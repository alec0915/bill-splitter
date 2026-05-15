import io


def get_input():
    totalPrice = float(input("Enter your total bill amount: "))
    numPeople = int(input("Enter the number of people splitting the bill: "))
    percentTip = int(input("Enter the percentage tip you would like to give: "))
    return totalPrice, numPeople, percentTip

def calculate_tip(totalprice, percentTip):
    tip = totalprice * percentTip / 100
    return tip

def calculate_individual_proportion(totalprice, numpeople)-> dict: 
    splitdict={}
    for i in range(numpeople):
        person= input(f"Enter the name of person {i+1}: ")
        numItems = int(input(f"Enter the number of items {person} ordered: "))
        total=0
        for j in range(numItems):
            total+=float(input(f"Enter the price of item {j+1}: "))
        splitdict[person] = total/totalprice
    return splitdict



def main():
    totalPrice,numPeople,percentTip = get_input()
    tipCost = calculate_tip(totalPrice,percentTip)
    ProportionDict = calculate_individual_proportion(totalPrice,numPeople)
    for name in ProportionDict:
        print(f"The total for {name} comes out to {(totalPrice*ProportionDict[name])+(tipCost*ProportionDict[name]):.2f}")
        print(f"That's {totalPrice*ProportionDict[name]:.2f} for the bill and {tipCost*ProportionDict[name]:.2f} for tip")

    

if __name__ == '__main__':
    main()