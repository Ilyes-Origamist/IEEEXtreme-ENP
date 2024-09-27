# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/xtreme-rappers/
# still some wrong answers

# Result: 82.35%
# Solved by ilyes, October 2023

def nb_words(K, J):
    if K+J<3 or K==0 or J==0:
        return 0
    else: # descending order
        if K==J:
            remaining=(2*K)%3
            ans=2*K//3
            if remaining ==2: return ans+1
            else: return ans
        elif J<K: words=[K, J]
        else: words=[J, K]

    if words[0]//words[1]>=2:
        return words[1]
    else:
        ans=0
        while (words[0]!=0 and words[1]!=0 and words[0]+words[1]>=3 and words[0]!=words[1]):
            words[0]-=2
            words[1]-=1
            ans+=1
        if words[0]==words[1]:
            ans+=2*words[0]//3
            remaining=(2*words[0])%3
            if remaining ==2: return ans+1
            else: return ans
        else: # meaning there is no more than a word for each of them
            return ans

K, J= map(int, input().split())
answer = nb_words(K, J)
print(answer)
