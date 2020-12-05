import time

#global final_ttl
dict_ttl = {}
dict = {}
dict_key = {}
global key_time

def put(key, value, ttl):
#global final_ttl
    global dict_ttl
    dict[key] = value
    global key_time
    key_time = time.time()
    dict_key[key] = key_time
    dict_ttl[key] = ttl

#final_ttl = ttl
   # print (dict_ttl[key],key_time)


def get(key):
#global final_ttl
    global dict_ttl
    now_time = time.time()
    diff = now_time - dict_key[key]


    if diff > dict_ttl[key]:
        del dict[key]

    print (dict[key])
    return dict[key]


list1 = ["Vinay", "Rahul"]
list2 = [2400, 3000]
list3 = [5, 30]

#put("Vinay", 2400, 5)
# put ("Rahul",3000, 30)

result = map(put, list1, list2, list3)
#print (result)
print (list(result))
get("Vinay")      # Key Vinay has TTL 5 sec
get("Rahul")      # Key rahul TTL= 30
time.sleep(6)   # test after 6 sec.Key for vinay give error but Rahul prints
get("Rahul")
get("Vinay")