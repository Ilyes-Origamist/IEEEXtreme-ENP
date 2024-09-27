# problem link
# https://csacademy.com/contest/interview-archive/task/anagrams/

# result: 100%

N = int(input())
anag_dict={}

for i in range(N):
    word = str(input())  # Read the input word
    sorted_word = ''.join(sorted(word))  # Sort the letters in the word
    if sorted_word not in anag_dict:
        anag_dict[sorted_word]=[i+1]
    else:
        anag_dict[sorted_word].append(i+1)

max_n = max(anag_dict.values(), key=len)
print(len(max_n))