# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/gaius-letters/

# Result: 100%
# Solved by ilyes, October 2023

# Funny challenge
def decryption(s: str)->str:
    ans=""
    for c in s:
        uni_code=ord(c)
        if ((uni_code>=65 and uni_code<=76) or (uni_code>=97 and uni_code<=108)): # a-l
            uni_code+=14
            ans+=chr(uni_code)
        elif ((uni_code>=77 and uni_code<=90) or (uni_code>=109 and uni_code<=122)): # m-
            uni_code-=12
            ans+=chr(uni_code)
        else:
            ans+=c
    return ans
    
z=str(input())
answer=decryption(z)
print(answer)
