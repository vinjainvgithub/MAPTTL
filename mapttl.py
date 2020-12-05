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
