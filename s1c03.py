from s1c02 import xor
import binascii as ba

'''
From this point on, I'm not providing the number of arguments.
Part of your job is to understand the contracts of these methods
and how they fit together.
'''

# input: message, key are hex-encoded byte strings
# output: hex-encoded byte string value of message encrypted with key
def caesarEncrypt(message, key):
    return xor(message, key)

# input: message, key are hex-encoded byte strings
# output: hex-encoded byte string value of message decrypted with key
def caesarDecrypt(message, key):
    return xor(message, key)

# To calculate score:
#   check if all are ascii-printable chars (0x00 to 0x7F)
#   check frequency of 12 most common chars ("etaoin shrdlu")
#       and 6 least common chars ("vkjxqz")
# input: hex encoded(!) byte string
# outut: int score
def scoreText(message):
    score = 0
    # most frequent chars: space(' ') and "etaoin shrdlu"
    most_freq_chars = [ord(' '),
                        ord('E'), ord('T'), ord('A'), ord('O'), ord('I'), ord('N'),
                        ord('S'), ord('H'), ord('R'), ord('D'), ord('L'), ord('U'),
                        ord('e'), ord('t'), ord('a'), ord('o'), ord('i'), ord('n'),
                        ord('s'), ord('h'), ord('r'), ord('d'), ord('l'), ord('u')]
    # least frequent chars: "vkjxqz"
    least_freq_chars = [ord('V'), ord('K'), ord('J'), ord('X'), ord('Q'), ord('Z'),
                        ord('v'), ord('k'), ord('j'), ord('x'), ord('q'), ord('z')]
    for i in message:
        if (i < 32 or i > 127):
            # not ascii-printable
            return -1
        if (i in most_freq_chars):
            score += 1
        if (i in least_freq_chars):
            score -= 1
    return score

# input: message is hex-encoded byte string
# output: hex-encoded byte string containing message w/ highest score
def solveS1C03(message):
    max_score = 0
    max_score_msg = b''
    # check all possible hex byte values as key
    for i in range(256):
        msg_decrypt = b''
        key = ba.hexlify(bytes([i]))
        # iterate over each hex byte in message
        for j in range(int(len(message)/2)):
            msg_index = j*2
            msg_decrypt += caesarDecrypt(message[msg_index:msg_index+2], key)
        msg_unhex = ba.unhexlify(msg_decrypt)
        score = scoreText(msg_unhex)
        if (score > max_score):
            max_score = score
            max_score_msg = msg_unhex
    return max_score_msg
