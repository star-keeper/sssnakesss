import binascii as ba
# inputs: byte string
# outputs: byte strings?

def b64ToHex(b64String):
    binary_data = ba.a2b_base64(b64String)
    return ba.hexlify(binary_data)

def hexToB64(hexString):
    binary_data = ba.unhexlify(hexString)
    return ba.b2a_base64(binary_data, newline=False) #.decode("utf-8")
