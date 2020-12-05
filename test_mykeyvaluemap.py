from mapttl import *

def test_getValuesThroughMap():
    list1 = ["Vinay", "Rahul"] # This is the Key list for the dictionary
    list2 = [2400, 3000] # This is the value list for the dictionary
    list3 = [5, 30] # This is the specific ttl value list for keys

    result = map(put, list1, list2, list3) # mapped the key value list with the ttl and added in put function
    print(list(result))

def test_getKeysTTLnotexpired():
    get("Vinay")
    get("Rahul")
    print(" Both Key values printed successfully before ttl expire")

def test_getKeysTTLexpired_6sec():
    time.sleep(6)  # Key value printing attempt after ttl=5 sec expire
    get("Rahul")  ##  (Key value of Rahul is tried after 6 sec and return successful )
    print("Key values printed successfully after 6sec for Rahul as TTL is 30")
    try:
        get("Vinay") ## ( Key value of Vinay is tried after 6 sec but  expired .)
    except KeyError:
        print("key-value of Vinay not printed after ttl expire as TTL was 5")

def test_getKeysTTLexpired_31sec():
    time.sleep(25)  # Key value printing attempt after ttl=30 sec expire
    try:
        get("Rahul")
    except KeyError:
        print("key-value of Rahul not printed after ttl expire as TTL was 30")






