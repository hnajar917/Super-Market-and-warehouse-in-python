import os.path
import glob
import time
import datetime
from datetime import *
from Products import Products
from SuperMarket import SuperMarket

ok = 0
global products
products = []
global superMarkets
superMarkets = []
wareHouseFile = r"C:\Users\PC\Desktop\work\pythonProject\LinuxProject2\LinuxProject2\warehouse_items.txt"
superMarketsFile = r"C:\Users\PC\Desktop\work\pythonProject\LinuxProject2\LinuxProject2\superMarekets.txt"


# This method is to read the warehouse file
def read_Warehouse_File(fname):
    with open(fname) as f:
        # Store the result of splitting in a list
        content_list = [line.split(";") for line in f]

    for x in content_list:
        code = x[0].strip()
        if EXISTS(code):
            print("The product {0} is repeated".format(code))
            exit()

        products.append(Products(x[0].strip(), x[1].strip(), x[2].strip(), x[3].strip(), x[4].strip(), x[5].strip()))


def read_Supermarket_File(fname):
    with open(fname) as k:
        # Store the result of splitting in a list
        content_list = [line.split(";") for line in k]

    for x in content_list:
        superMarkets.append(SuperMarket(x[0].strip(), x[1].strip(), x[2].strip(), x[3].strip()))


# A method to update the file variables
def updateWarehouseFile():
    file_to_delete = open(wareHouseFile, 'w')  # to overwrite the contents of wareHouseFile
    file_to_delete.close()
    u = open(wareHouseFile, "a")  # 'a' stands for append
    for i in range(0, len(products)):
        u.write(
            products[i].get_code() + ";" + products[i].get_name() + ";" + products[i].get_ex_date() + ";" + products[
                i].get_wholesaleCost() + ";" + products[i].get_saleCost() + ";" + products[i].get_quantity())
        u.write("\n")
    u.close()


# A method to update the supermarket file variables
def updateSuprMarketFile():
    file2_to_delete = open(superMarketsFile, 'w')  # to overwrite the contents of wareHouseFile
    file2_to_delete.close()
    c = open(superMarketsFile, "a")  # 'a' stands for append
    for i in range(0, len(superMarkets)):
        c.write(superMarkets[i].get_code() + ";" + superMarkets[i].get_name() + ";" + superMarkets[
            i].get_address() + ";" + str(superMarkets[i].get_date()))
        c.write("\n")
    c.close()


# check if an item exists in the warehouse
def EXISTS(code):
    for p in products:
        if p.get_code() == code:
            return True

    return False


# check if an item exists in a certain Supermarket

def sEXISTS(code):
    for s in superMarkets:
        if s.get_code() == code:
            return True


def printProducts():
    d = {}
    idx = 0
    for p in products:
        d[idx] = p
        idx += 1

    print("{:<25} {:<25} {:<25} {:<25} {:<25} {:<25}".format('Product Code', 'Product Name', 'Product Expiry Date',
                                                             'Product WholeSale Cost', 'Products Sale Cost',
                                                             'Product Quantity'))
    for k, v in d.items():
        code = v.get_code()
        name = v.get_name()
        date = v.get_ex_date()
        wholesaleCost = v.get_wholesaleCost()
        saleCost = v.get_saleCost()
        quantity = v.get_quantity()
        print("{:<25} {:<25} {:<25} {:<25} {:<25} {:<25}".format(code, name, date, wholesaleCost, saleCost, quantity))


def printSuperMarkets():
    d = {}
    idx = 0
    for s in superMarkets:
        d[idx] = s
        idx += 1

    print("{:<25} {:<25} {:<25} {:<25}".format('SuperMarket Code', 'SuperMarket Name', 'SuperMarket Address',
                                               'SuperMarket Added Date'))
    for k, v in d.items():
        code = v.get_code()
        name = v.get_name()
        date = v.get_date()
        address = v.get_address()
        print("{:<25} {:<25} {:<25} {:<25}".format(code, name, address, date))


def addSuperMarket():
    scode = input("Enter the code of the Supermarket: ")
    while True:
        if sEXISTS(scode):
            print("This code already exists, insert a new code, please!")
            scode = input("Enter the code of the Supermarket: ")
        elif any(not c.isnumeric() for c in scode):
            print("CODE has to contain numbers only!")
            scode = input("Enter numerical value for the code: ")
        else:
            break
    name = input("Enter the supermarket's name: ")

    address = input("Enter the address of the supermarket: ")
    okc = 0
    while okc == 0:
        if not any(c.isalpha() for c in address):
            print("You have to insert an address with characters")
            address = input("Enter the address of the supermarket: ")
            okc = 0
        else:
            okc = 1
    today = str(date.today())
    print()
    print(70 * '-')
    print("The supermarket has been added successfully")
    print()
    adds = SuperMarket(scode, name, address, today)

    superMarkets.append(adds)
    updateSuprMarketFile()
    printSuperMarkets()


def addProduct():
    print("Enter the Info for the new product")
    code = input("Enter product code: ")
    while True:  # this loop is to handle any exceptions that occur in the code
        if EXISTS(code):
            print("This product already exists, enter a new one.")
            code = input("Enter product code: ")
        elif any(not c.isnumeric() for c in code):
            print("CODE has to contain numbers (not characters)")
            code = input("Enter numerical 4-digit value for the code: ")
        elif (len(code) != 4):
            print("Code must be 4 digits")
            code = input("Enter numerical 4-digit value for the code: ")
        else:
            break
    name = input("Enter the product's name: ")
    global ok
    ok = 0
    while ok == 0:
        date1 = input("Enter product expiry date: ")
        checkDateValidity(date1)

    wholesaleCost = input("Enter product's wholesale cost: ")
    okc = 0
    while okc == 0:  # this loop is to handle any exceptions that occurs on the whole sale cost
        if any(c.isalpha() for c in wholesaleCost):
            print("You have to insert a number (not characters) ")
            wholesaleCost = input("Enter product's wholesale cost: ")
            okc = 0
        else:
            okc = 1
    saleCost = input("Enter product's sale cost: ")
    okcc = 0
    while okcc == 0:  # this loop is to handle any exceptions that occurs on the sale cost
        if any(c.isalpha() for c in saleCost):
            print("You have to insert numbers only!")
            saleCost = input("Enter product's sale cost: ")
            okcc = 0
        else:
            okcc = 1
    quantity = input("Enter product's quantity: ")
    okp = 0
    while okp == 0:  # this loop is to handle any exceptions that occurs on the quantity
        if any(c.isalpha() for c in quantity):
            print("You have to insert product's quantity with numbers only! ")
            quantity = input("Enter product's quantity: ")
            okp = 0
        elif int(quantity) < 0:
            print("Quantity shouldn't be negative")
            quantity = input("Enter product's quantity: ")
            okp = 0
        else:
            okp = 1
    addp = Products(code, name, date1, wholesaleCost, saleCost, quantity)
    products.append(addp)
    updateWarehouseFile()
    print()
    print(70 * '-')
    print("The product has been added successfully")
    print()
    printProducts()


def checkDateValidity(Date):
    global ok
    if len(Date) != 10:
        print("The date has to be in the format DD/MM/YYYY")
        print()
        print(70 * '-')
        ok = 0
    elif any(c.isalpha() for c in Date):
        print("You have to insert a date with numbers only")
        print()
        print(70 * '-')
        ok = 0
    elif Date[2] != '/' or Date[5] != '/':
        print("The date is invalid, enter the date with its valid format DD/MM/YYYY")
        print()
        print(70 * '-')
        ok = 0
    elif int(Date[3:5]) > 12 or int(Date[3:5]) < 1:
        print("month should be in range 1-12")
        ok = 0


    elif Date[3:5] == "02" and (int(Date[0:2]) > 29 or int(Date[0:2]) < 1):
        print("The Day should be in range 1-29 for this month")
        ok = 0

    elif (Date[3:5] == "04" or Date[3:5] == "06" or Date[3:5] == "09" or Date[3:5] == "11") and (int(Date[0:2]) > 30 or int(Date[0:2]) < 1):
        print("The Day should be in range 1-30 for this month")
        ok = 0

    elif int(Date[0:2]) > 31 or int(Date[0:2]) < 1:
        print("The day should be in range 1-31 for this month")
        ok = 0

    elif int(Date[6:10]) <= int(date.today().year):
        if int(Date[6:10]) == int(date.today().year):#To check years
            if int(Date[3:5]) > int(date.today().month):  # To check months
                ok=1
            elif int(Date[3:5]) == int(date.today().month):  # To check months
                    if int(Date[0:2]) <= int(date.today().day): #To check days
                        print("Enter a valid day, ple1ase!")
                        ok = 0
                    else:
                        ok=1

            else:
                print("Enter a valid month, please")
                ok = 0
        else:
            print("invalid year")
            ok = 0

    else:
        ok = 1


def check(date_input, p):
    datemask = "%d/%m/%Y"

    new_date1 = datetime.strptime(date_input, datemask)
    new_date2 = datetime.strptime(p, datemask)
    if new_date1 > new_date2:
        return True
    return False


def list_items():
    global ok
    ok = 0
    while ok == 0:
        date_input = input("Enter the date you want to compare with: ")
        checkDateValidity(date_input)

    total_wholesale = 0
    total_sale = 0
    print()
    print("Here are the list of products that have an expiry date before the input date : ")
    print()

    for p in products:
        p_date = str(p.get_ex_date())
        if not check(date_input, p_date):
            continue
        print(p.get_name())
        total_wholesale += float(p.get_wholesaleCost()) * float(p.get_quantity())
        total_sale += float(p.get_saleCost()) * float(p.get_quantity())
    print()
    print("Total wholesale price is: " + str(total_wholesale))
    print("Total sale price is: " + str(total_sale))


def clear():
    count = 0
    code = input("Enter product code: ")
    while True:  # this loop is to handle any exceptions that occur in the code
        if any(not c.isnumeric() for c in code):
            print("CODE has to contain numbers (not characters)")
            code = input("Enter numerical 4-digit value for the code: ")
        elif (len(code) != 4):
            print("Code must be 4 digits")
            code = input("Enter numerical 4-digit value for the code: ")
        else:
            break
    for i in range(0, (len(products) + 1)):  # a loop to search for the code and clear quantity
        if count > (len(products) - 1):  # if there are no products
            print("This code not found")
            clear()
            break
        if code != products[i].get_code():
            count = count + 1
        elif code == products[i].get_code():
            print("Product code: " + products[i].get_code() + "\n" + "Product name: " + products[
                i].get_name() + "\n" + "Product expiry date: " + products[
                      i].get_ex_date() + "\n" + "product Whole sale cost: " + products[
                      i].get_wholesaleCost() + "\n" + "Product sale cost: " + products[
                      i].get_saleCost() + "\n" + "Product quantity: " + products[i].get_quantity() + "\n")
            if products[i].get_quantity() == "0":
                print("No items left of this product!\n")
                break
            if int(products[i].get_quantity()) > 0:
                cleared = input("\nEnter the quantity that needs to be cleared\n")
                while int(cleared) > int(products[i].get_quantity()):
                    print
                    print("Available quantity: " + str(products[i].get_quantity() + "\n"))
                    print("Cleared quantity should be at most the available quantity.\n")
                    cleared = input("Enter the quantity that needs to be cleared\n")
                clearedQuantity = int(products[i].get_quantity()) - int(cleared)
                products[i].set_quantity(str(clearedQuantity))
                print("Successfully Cleared")
                # must update the warehouse file
                updateWarehouseFile()
                break


def destribution():
    # smCode stands for Supermarket Code
    smCode = input("Enter the supermarket's code\n")
    name = "DistributeItems_" + smCode + ".txt"
    # Searching for the file then saving it in the list 'm'
    m = glob.glob(name, recursive=True)
    # As the smCode is unique then it will be stored as the fist element of the list m
    filename = m[0]
    filepath = os.path.abspath(filename)  # getting the path of the file
    p = open(filepath)
    for line in p:
        seperated = line.split(";")
        for i in range(0, len(superMarkets)):
            if superMarkets[i].get_code() == str(smCode):

                count = 0
                for s in range(0, (len(products) + 1)):  # a loop to search for the code and clear quantity
                    if count > (len(products) - 1):
                        print("The product Code (" + seperated[0] + ") doesn't match any product in the warehouse")
                        print("The product {} and the requested amonut {}".format(seperated[0], seperated[1]))
                        break
                    if seperated[0] != products[s].get_code():
                        count = count + 1
                    elif seperated[0] == products[s].get_code():
                        if (int(products[s].get_quantity()) == 0):
                            print("No items left of (", seperated[0] + ") are left!\n")
                            break
                        elif int(products[s].get_quantity()) > 0:
                            if int(products[s].get_quantity()) >= int(seperated[1]):
                                cleared = seperated[1]
                                cleardQuantity = int(products[s].get_quantity()) - int(cleared)
                                products[s].set_quantity(str(cleardQuantity))
                                superMarkets[i].productsInS[seperated[0]] = [int(seperated[1])]
                                # must update the warehouse file
                                updateWarehouseFile()
                                s = 0
                                break
                            if int(seperated[1]) > int(products[s].get_quantity()):
                                print("the product: " + products[s].get_code() + " ,that is: " + products[
                                    s].get_name() + " ,is not vailable with the requested amount.")
                                print("Requested amount: " + seperated[1])
                                print("Available amount: " + products[s].get_quantity())
                                print("Distributed amount: " + products[s].get_quantity())
                                superMarkets[i].productsInS[seperated[0]] = [products[s].get_quantity()]
                                products[s].set_quantity("0")
                                updateWarehouseFile()
                                break
    p.close()
    print("Distribution is finished")


def report():
    print("Sales Status report:\n")
    totalWholeSaleCost = 0
    totalSalesCost = 0
    n = open(wareHouseFile)
    numOfProducts = len(n.readlines())
    n.close
    print("Number of products is:- " + str(numOfProducts) + "\n")
    t = open(wareHouseFile)
    for line in t:
        separated = line.split(";")
        totalWholeSaleCost += (float(separated[3]) * float(
            separated[5]))  # whole sale cost multiplied by quantity for each item added to the whole summation
        totalSalesCost += float(separated[4]) * float(
            separated[5])  # whole item sale cost unit multiplied by quantity for each item added to the whole summation
    ExpectedProfit = totalSalesCost - totalWholeSaleCost
    print("Total wholesale cost of all items in the warehouse: " + str(totalWholeSaleCost) + "\n")
    print("Total sales cost of all items in the warehouse: " + str(totalSalesCost) + "\n")
    print("Expected profit after selling all items in the warehouse: " + str(ExpectedProfit) + "\n")


def menu():
    print(70 * '-')
    print("Choose a number from 1 to 7")
    print("1- Add product items to the warehouse")
    print("2- Add a new supermarket to the management system")
    print("3- List of items in the warehouse based on expiry date")
    print("4- Clear an item from the warehouse")
    print("5- Distribute products from the warehouse to a supermarket")
    print("6- Generate a report about the sales status of the warehouse")
    print("7- Exit")
    print(70 * '-')
    n = int(input("\nEnter your choice: "))
    print()
    print(70 * '-')
    if n == 1:
        addProduct()
    elif n == 2:
        print("Enter the Info of the SuperMarket")
        addSuperMarket()
        pass
    elif n == 3:
        list_items()
    elif n == 4:
        clear()
    elif n == 5:
        destribution()
    elif n == 6:
        report()
    elif n == 7:
        exit()
    else:
        print("Please enter a valid number, or enter 7 to exit the program")
        menu()

    menu()


file_exists = open(wareHouseFile)
file2_exists = open(superMarketsFile)

if file_exists and file2_exists:
    read_Warehouse_File(wareHouseFile)
    read_Supermarket_File(superMarketsFile)
    menu()
else:
    print("Files does not exists")
