import pstats


def remove_and_split(string,word):
    strig1=string.replace(word,"universe")
    return strig1.strip()


str="   We are the best in the world   "
print(str)
a=remove_and_split(str,"world")
print(a)