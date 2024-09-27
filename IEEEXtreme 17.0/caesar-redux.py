# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/caesar_redux

# Result: 66.67%
# Solved by ilyes, IEEEXtreme 17.0

n=int(input())
for message in range(n):
    shift=int(input())
    text=str(input())
    ans=""
    if (' the ' in text) or ('the ' in text): # -
        # print(text.index('the '))
        for c in text:
            old=ord(c)
            if old==32:
                ans+=c
            else:
                new=old-shift
                if new<97:
                    new+=26
                ans+=chr(new)
        print(ans)
    else:
        for s in text:
            old=ord(s)
            if old==32:
                ans+=s
            else:
                new=old+shift
                if new>122:
                    new-=26
                ans+=chr(new)
        print(ans)

    #+7
    # if 'the' in string -19