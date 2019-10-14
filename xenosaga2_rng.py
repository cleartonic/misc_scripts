"""
@author: cleartonic
"""


def f_int(x):
    return int(x,base=16)
    
def f_byte(x):
    return hex(x).replace("0x","").upper().zfill(16)

def shift_left(x):
    data = f_byte(f_int(x) << 32)
    if len(data) > 16:
        return data[8:]
    else:
        return data
def shift_right(x):
    data = f_byte(f_int(x) >> 32)
    if len(data) > 16:
        return data[8:]
    else:
        return data
def shift_right_a32(x):
    if bin(f_int(x)).replace("0b","").zfill(64)[0] == '1':
        data = f_byte(f_int(x) >> 32)
        data = "FFFFFFFF" + data[8:]
        return data
    else:
        data = f_byte(f_int(x) >> 32)
    if len(data) > 16:
        return data[8:]
    else:
        return data


def load_be(x):
    return x[8:] + x[:8]


def advance_rng(starting_value,print_flag=False):
    a0='0000000000000000'
    a1='0000000000000000'
    a2='0000000000000000'
    a3='0000000000000000'
    v0='0000000000000000'
    v1='0000000000000000'
    t0='0000000000000000'
    t1='FFFFFFFFA0000000'
    
    
    constant = '0000000041C64E6D'
    

    #1A75B8 - Load RNG value into register a0
    a0 = starting_value
    #1A75BC - Load constant 41C64E6D to a1
    a1 = constant
    #1A75C4 - Call function to handle RNG z_un_002a4ee8
    #2A4EE8 - Load constant 0x41C64E6D into register v0
    v0 = load_be(a1)
    #2A4EEC - Shift v0 right
    v0 = shift_right_a32(v0)
    #2A4EF0 - Shift register a1
    a1 = shift_right_a32(a1)

    #2A4EF4 - Load a0 into v1
    v1 = load_be(a0)
    #2A4EF8 - Shift v1 right

    v1 = shift_right_a32(v1)
    
    #2A4EFC - Multiply current v0 by v1             ######### ROOM FOR ERROR HERE

    temp_mult1 = f_byte(f_int(v0[8:]) * f_int(v1[8:]))
    #2A4F00 - Store low bytes into register a2
    a2 = a2[0:8] + temp_mult1[8:]
    #2A4F04 - Store high bytes into register t0
    t0 = t0[0:8] + temp_mult1[:8]

    #2A4F08 - Shift register a2 left
    a2 = shift_left(a2)
    #2A4F0C - Shift a0 right
    a0 = shift_right_a32(a0)
    #2A4F10 - Multiply v1 by a1 then save to v1
    
    v1 = f_byte(f_int(v1) * f_int(a1))

    #2A4F14 - Subtract 0x01 (1) from a1
    if (f_int(a1) - 1) < 0:
        a1 = f_byte(f_int("FFFFFFFFFFFFFFFF") - f_int(a1))
    else:
        a1 = f_byte(f_int(a1) - 1)
    
    #2A4F18 - Shift a1 left
    a1 = shift_left(a1)
    
    #2A4F10 - Multiply v0 by a0 then save to v0
    
    a0 = a0[:8] + f_byte(f_int(v0[8:]) * f_int(a0[8:]))[-8:]
    
    
    #2A4F20 - Shift a2 right
    a2 = shift_right(a2)
    #2A4F24 - Perform "AND" function (find all similar bytes) among t1 and a1, store in t1
    
    t1 = t1[:8] + f_byte(f_int(t1) & f_int(a1))[8:]

    #2A4F28 - Store $FF (6 of them) in a3
    a3 = "FFFFFFFFFFFF0000"
    
    #2A4F2C - Shift a3 right
    a3 = shift_right(a3)
    #2A4F30 - Perform "AND" function among t1 and a2, store in t1
    t1 = t1[:8] + f_byte(f_int(t1) | f_int(a2))[8:]
    #2A4F34 - Shift t0 left

    t0 = shift_left(t0)
    
    ##2A4F38 - Perform "AND" function among t1 and a3, store in t1
    t1 = f_byte(f_int(t1) & f_int(a3))
    
    ##2A4F3C - Perform "OR" function among t1 and t0, store in t1
    t1 = f_byte(f_int(t1) | f_int(t0))

    

    #2A4F40 - Add a0 to v1
    if (f_int(a0) + f_int(v1)) > f_int("FFFFFFFFFFFFFFFF"):
        v1 = f_byte(f_int(a0) + f_int(v1) - f_int("10000000000000000"))
    else:
        v1 = f_byte(f_int(a0) + f_int(v1))
    
    #2A4F44 - Shift arithmetic t1 into v0
    v0 = shift_right_a32(t1)
    
    #2A4F48 - Perform "AND" function among a3 and t1, store in a3
    a3 = a3[:8] + f_byte(f_int(a3) & f_int(t1))[8:]
    #2A4F4C - Add v1 to v0
#    print("a" + 2)
    if (f_int(v1) + f_int(v0)) > f_int("FFFFFFFFFFFFFFFF"):
        v0 = f_byte(f_int(v1) + f_int(v0) - f_int("10000000000000000"))
    else:
        v0 = v0[:8] + f_byte(f_int(v1) + f_int(v0))[-8:]
    #2A4F50 - Shift v0 left
    
    v0 = shift_left(v0)
    
    #2A4F54 - Jump to another function
    v0 = v0[:8] + a2[8:]
    #1A75D0 - Add constant 0x3039 to v0 (what is now current RNG)
    if (f_int(v0) + f_int("3039")) > f_int("FFFFFFFFFFFFFFFF"):
        v0 = f_byte(f_int(v0) + f_int("3039") - f_int("10000000000000000"))
    else:
        v0 = f_byte(f_int(v0) + f_int("3039"))
    #1A75D4 - Save RNG value in RAM
    if print_flag:
        print("--------------")
        print("Final RNG Value (BE): %s%s%s%s%s%s%s%s"  % 
              (v0[:2],
               v0[2:4],
               v0[4:6],
               v0[6:8],
               v0[8:10],
               v0[10:12],
               v0[12:14],
               v0[14:16],
               )
               )
        print("Final RNG Value (LE): %s%s%s%s%s%s%s%s"  % 
              (v0[14:16],
               v0[12:14],
               v0[10:12],
               v0[8:10],
               v0[6:8],
               v0[4:6],
               v0[2:4],
               v0[:2],
               )
               )
              
        print("--------------")
            
        print("v0: "+v0)
        print("v1: "+v1)
        print("a0: "+a0)
        print("a1: "+a1)
        print("a2: "+a2)
        print("a3: "+a3)
        print("t0: "+t0)
        print("t1: "+t1)
    
    return v0

starting_value = '81FC45F195FB7483'
def run(starting_value, num):
    print("1st Value: %s" % (starting_value))
    new_val = advance_rng(starting_value)
    print("RNG Value: %s " % (new_val))
    for i in range(0,num):
        new_val = advance_rng(new_val)
        print("RNG Value: %s " % (new_val))


