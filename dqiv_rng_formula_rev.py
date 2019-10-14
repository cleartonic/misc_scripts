# -*- coding: utf-8 -*-
"""
@author: cleartonic
"""

import datetime

def advance(x,num):
    heal_list = []
    checked_heal_lists = [[35,39,36,34,32,39,34,35,37,35],[39,40,30,33,36,40,33,40,31,33],[39,40,30,37,37,30,40,33,31,33],[40,35,38,34,38,30,31,33,39,37],[37,34,33,31,34,38,36,35,34,39]]
    rng = int(x,base=16)
    rng_hex = hex(rng).replace("0x","").zfill(8)
    for i in range(0,num):
        starting_rng = rng_hex
        r12 = int('5D588B65',base=16)
        r14 = int('269EC3',base=16)
        rng = ((rng * r12) + r14)
        rng_hex = hex(rng).replace("0x","")
        if len(rng_hex) > 8:
            rng_hex = rng_hex[(len(rng_hex)-8):]
        #print(rng_hex)
        
        rng = int(rng_hex,base=16)
        hoimi1 = rng >> 16
        hoimi_mult = int('B',base=16)  # 02080D68
        hoimi2 = (hoimi_mult * hoimi1) >> 16
        heal_val = hoimi2+30
        heal_list.append(heal_val)
        rng = int(rng_hex,base=16)
        
        rng = ((rng * r12) + r14)
        rng_hex = hex(rng).replace("0x","")
        if len(rng_hex) > 8:
            rng_hex = rng_hex[(len(rng_hex)-8):]
        rng = int(rng_hex,base=16)
        

        rng = ((rng * r12) + r14)
        rng_hex = hex(rng).replace("0x","")
        if len(rng_hex) > 8:
            rng_hex = rng_hex[(len(rng_hex)-8):]
        rng = int(rng_hex,base=16)


        
        
        rng_hex = rng_hex[6:8] + rng_hex[4:6] + rng_hex[2:4] + rng_hex[0:2]
        
        #print("DEBUG: Starting rng : "+starting_rng+ " Heal value: "+str(heal_val)+" Ending rng: "+rng_hex)
    
                

    for checked_heal_list in checked_heal_lists:
        if heal_list == checked_heal_list:
            print("MATCH: Starting rng : "+x+ " Heal value: "+str(heal_list))




def start_run():
    start = datetime.datetime.now()
    i = 4294967295
    while i > 0:
        advance(hex(i).replace("0x","").zfill(8),10)
        i = i - 1
    end = datetime.datetime.now()
    print("Runtime in seconds: "+str((end - start).seconds))

#advance('00000000',10)









































# WIP
def reverse_advance(x,num=1):
    rng = x[4:]
    print("Seed: "+rng)
    rng = int(x,base=16)
    tmp0 = rng * int('8965',base=16)
    sd_tmp0 = tmp0 & int('ffff',base=16)
    carry = tmp0
    carry >>= 16
    print(str(tmp0)+" | "+str(sd_tmp0)+" | "+str(carry))
    
    
    
    
#print("-------")
#reverse_advance('d2f51D47')