import binascii as ba

# input: s1, s2 are hex-encoded byte strings
# output: hex-encoded byte string containing XOR result
def xor(s1, s2):
    if len(s1) != len(s2):
        raise RuntimeError("Inputs are not of equal length\n  s1: " + len(s1) + "\n  s2: " + len(s2))
    
    s1_asBytes = ba.unhexlify(s1)
    s2_asBytes = ba.unhexlify(s2)

    res_asInt = []
    for i in range(len(s1_asBytes)):
        res_asInt.append(s1_asBytes[i] ^ s2_asBytes[i])
    res_asBytes = bytes(res_asInt)
    return ba.hexlify(res_asBytes)