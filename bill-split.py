import io


def get_input():
    subtotal = float(input("Enter the subtotal of your bill: "))
    tax = float(input("Enter the tax of your bill: "))
    percentTip = int(input("Enter the percentage tip you would like to give: "))
    numPeople = int(input("Enter the number of people splitting the bill: "))
    return subtotal, tax, numPeople, percentTip


def calculate_tip(totalPrice, percentTip):
    tip = totalPrice * percentTip / 100
    return tip

def calculate_individual_proportion(subtotal, numpeople)-> dict: 
    splitdict={}
    for i in range(numpeople):
        person= input(f"Enter the name of person {i+1}: ")
        numItems = int(input(f"Enter the number of items {person} ordered: "))
        total=0
        for j in range(numItems):
            total+=float(input(f"Enter the price of item {j+1}: "))
        splitdict[person] = total/subtotal
    return splitdict



def main():
    subtotal, tax, numPeople, percentTip = get_input()
    price = subtotal + tax
    tip = calculate_tip(price,percentTip)
    splitDict = calculate_individual_proportion(subtotal,numPeople)

    for i in splitDict:
        indivSub = splitDict[i] * subtotal
        indivTax = splitDict[i] * tax
        indivTip = splitDict[i] * tip

        print(f"{i}'s contribution is {indivSub} for the bill, {indivTax} for the tax, and {indivTip} for the tip")
        print(f"{i}'s total is {indivSub+indivTax+indivTip}")
    

if __name__ == '__main__':
    main()
