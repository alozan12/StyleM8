import psycopg2
import json

# Helper function to connect to database
def connect():
    conn = psycopg2.connect(
            database="412Project",
            host='localhost',  
            port='5432'
            )
    return conn

# Takes in memberID as int and returns [(outfitID, outfitName, closetID, shirtID, pantsID, shoesID)]
def MyCloset(memberID):
    try: 
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT o_outfitid, o_outfitname, o_closetid, o_shirtid, o_pantsid, o_shoesid FROM outfit, closet WHERE o_closetid = c_closetid AND c_memberid = %(memberID)s", {"memberID": memberID})
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# returns 4 shirts, 4 pants, 4 shoes in one list 
def FindYourOutfit():
    # returns as list of 12 items
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM shirt LIMIT 4")
        rows = cur.fetchall()
        cur.execute("SELECT * FROM pants LIMIT 4")
        rows = rows + cur.fetchall()
        cur.execute("SELECT * FROM shoes LIMIT 4")
        rows = rows + cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def GetClosetID(memberID):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT c_closetid FROM closet WHERE c_memberid = %(memberID)s", {"memberID": memberID})
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# LIMITED TO 100 RESULTS
def GetAllShirts():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT shi_shirtname, shi_shirtstyle, shi_shirtprice, shi_description FROM shirt LIMIT 100")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# LIMITED TO 100 RESULTS
def GetAllPants():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT p_pantsname, p_pantsstyle, p_pantsprice, p_description FROM pants LIMIT 100")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# LIMITED TO 100 RESULTS
def GetAllShoes():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT sho_shoesname, sho_shoesstyle, sho_shoesprice, sho_description FROM shoes LIMIT 100")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def GetShirt(shirtID):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT shi_shirtname, shi_shirtstyle, shi_shirtprice, shi_description, s_storename FROM shirt, store WHERE shi_shirtid = %(shirtID)s AND s_storeid = shi_storeid", {"shirtID": shirtID})
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def GetPants(pantsID):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT p_pantsname, p_pantsstyle, p_pantsprice p_description, s_storename FROM pants, store WHERE p_pantsid = %(pantsID)s AND s_storeid = p_storeid", {"pantsID": pantsID})
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def GetShoes(shoesID):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT sho_shoesname, sho_shoesstyle, sho_shoesprice, sho_description, s_storename FROM shoes, store WHERE sho_shoesid = %(shoesID)s AND s_storeid = sho_storeid", {"shoesID": shoesID})
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Takes in username as string and returns the memberid of the new member
# If username already exists in database, returns -1   
def CreateAccount(username):
    try:
        conn = connect()
        cur = conn.cursor()
        # RETRIEVES THE MOST RECENT ID
        cur.execute("SELECT * FROM member WHERE m_membername = %(username)s", {"username": username})
        result = cur.fetchall()
        if result == []:
            cur.execute("SELECT m_memberid FROM member ORDER BY m_memberid DESC LIMIT 1")
            result = cur.fetchall()
            lastID = int(result[0][0])
            newMemberID = lastID + 1
            cur.execute("INSERT INTO member VALUES(%(newMemberID)s, %(username)s, 1, 0)", {"newMemberID": newMemberID, "username": username})
            cur.execute("SELECT c_closetid FROM closet ORDER BY c_closetid DESC LIMIT 1")
            result = cur.fetchall()
            lastID = int(result[0][0])
            newClosetID = lastID + 1
            cur.execute("INSERT INTO closet VALUES(%(newClosetID)s, %(newMemberID)s, 'closet', 0)", {"newClosetID": newClosetID, "newMemberID": newMemberID})
            conn.commit()
            cur.execute("SELECT * FROM member WHERE m_membername = %(username)s", {"username": username})
            result = cur.fetchall()
            cur.close()
            conn.close()
            return result
        else:
            cur.close()
            conn.close()
            return -1
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Takes in username as string and returns [(memberID, memberName, numClosets, numOutfits)]
# If username does not exist in database, returns -1
def LogIn(username):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM member WHERE m_membername = %(username)s", {"username": username})
        result = cur.fetchall()
        if result == []:
            cur.close()
            conn.close()
            return -1
        else:
            cur.execute("SELECT * FROM member WHERE m_membername = %(username)s", {"username": username})
            result = cur.fetchall()
            cur.close()
            conn.close()
            return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Takes in memberID as int and returns [(memberID, memberName, numClosets, numOutfits)]
# If memberID does not exist in database, returns -1
def MyAccount(memberID):
    try: 
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM member WHERE m_memberID = %(memberID)s", {"memberID": memberID})
        result = cur.fetchall()
        if result == []:
            cur.close()
            conn.close()
            return -1
        else: 
            cur.close()
            conn.close()
            return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Takes in outfitName as string if no outfitName is provided creates a default name, closetID as int, 
# shirtID as int, pantsID as int, shoesID as int
# Adds the outfit to the outfit table
# Increments the c_totaloutfits and m_numoutfits columns by 1 to reflect adding an outfit
def CreateOutfit(outfitName, closetID, shirtID, pantsID, shoesID):
    try: 
        conn = connect()
        cur = conn.cursor()
        if len(outfitName) == 0:
            outfitName = "My Outfit"
        cur.execute("SELECT o_outfitid FROM outfit ORDER BY o_outfitid DESC limit 1")
        result = cur.fetchall()
        newOutfitID = result[0][0] + 1
        cur.execute("INSERT INTO outfit VALUES(%(newOutfitID)s, %(outfitName)s, %(closetID)s, %(shirtID)s, %(pantsID)s, %(shoesID)s)", {"newOutfitID": newOutfitID, "outfitName": outfitName, "closetID": closetID, "shirtID": shirtID, "pantsID": pantsID, "shoesID": shoesID})
        conn.commit()
        cur.execute("SELECT * FROM closet WHERE c_closetID = %(closetID)s", {"closetID": closetID})
        result = cur.fetchall()
        memberID = result[0][1]
        totalOutfitsCloset = result[0][3] + 1
        cur.execute("UPDATE closet SET c_totaloutfits = %(totalOutfitsCloset)s WHERE c_closetID = %(closetID)s", {"totalOutfitsCloset": totalOutfitsCloset, "closetID": closetID})
        conn.commit()
        cur.execute("SELECT COUNT(*) FROM member, closet, outfit WHERE m_memberid = c_memberid AND o_closetid = c_closetid AND m_memberid = %(memberID)s", {"memberID": memberID})
        result = cur.fetchall()
        totalOutfitsMember = result[0][0]
        cur.execute("UPDATE member SET m_numoutfits = %(totalOutfitsMember)s", {"totalOutfitsMember": totalOutfitsMember})
        conn.commit()
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def Spacer():
    print("\n====================================\n")

def SignInMenu():
    print("Welcome To StyleM8")
    print("1. Log In")
    print("2. Create Account")
    option = input("Enter Choice: ")
    if option == '1':
        print("Log In")
        username = input("Enter Username: ")
        id = LogIn(username)
        while id == -1:
            print("invalid username")
            username = input("Enter Username: ")
            id = LogIn(username)
        AccountInfo(id[0][0])

    elif option == '2':
        print("Create New Account")
        username = input("Enter Username: ")
        id = CreateAccount(username)
        AccountInfo(id[0][0])

    else:
        print("invalid")


def AccountInfo(memberID):
    result = MyAccount(memberID)
    Spacer()
    print(f"Welcome, {result[0][1]}")
    print(f"You have {result[0][3]} outfits")
    MainMenu(memberID)

def CreateOutfitMenu(memberID):
    Spacer()
    result = GetClosetID(memberID)
    id = int(result[0][0])
    name = input("Enter a name for the outfit: ")
    shirtID = int(input("Enter a Valid Shirt ID (0 - 99999): "))
    pantsID = int(input("Enter a Valid Pants ID (0 - 99999): "))
    shoesID = int(input("Enter a Valid Shoes ID (0 - 99999): "))
    CreateOutfit(name, id, shirtID, pantsID, shoesID)

    
def MainMenu(memberID):
    option = ''
    while option != '6':
        Spacer()
        print("1. View My Closet")
        print("2. List Shirts")
        print("3. List Pants")
        print("4. List Shoes")
        print("5. Create a new outfit")
        print("6. Log Out")
        option = input("Enter Choice: ")
        Spacer()

        if option == '1':
            result = MyCloset(memberID)
            if len(result) == 0:
                print("Your closet is empty")
            for row in result:
                print(f"Outfit Name: {row[1]}, ShirtID: {row[3]} Pants: {row[4]} Shoes: {row[5]}")
        elif option == '2':
            result = GetAllShirts()
            for row in result:
                #print(row)
                print(f"Name: {row[0]}, Style: {row[1]}, Price: {row[2]}, Description: {row[3]}")
        elif option == '3':
            result = GetAllPants()
            for row in result:
                
                print(f"Name: {row[0]}, Style: {row[1]}, Price: {row[2]}, Description: {row[3]}")
        elif option == '4':
            result = GetAllShoes()
            for row in result:
                print(f"Name: {row[0]}, Style: {row[1]}, Price: {row[2]}, Description: {row[3]}")
        elif option == '5':
            CreateOutfitMenu(memberID) 
        elif option == '6':
            print("logging out...")
        else:
            print("invalid")
    
SignInMenu()