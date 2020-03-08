import binascii as ba

def xor(s1, s2):
    if len(s1) != len(s2):
        raise RuntimeError("Inputs are not of equal length\n  s1: " + len(s1) + "\n  s2: " + len(s2))
    
    s1_asBytes = ba.unhexlify(s1)
    s2_asBytes = ba.unhexlify(s2)

    res_asBytes = b''
    for i in range(len(s1_asBytes)):
        res_asBytes += bytes(s1_asBytes[i] ^ s2_asBytes[i])
        print(s1_asBytes[i]^s2_asBytes[i])
    
    return ba.hexlify(res_asBytes)