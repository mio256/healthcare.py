print('0と1で答えてください。')
s=[
    'ちゃんと寝て',
    'ちゃんと運動して',
    'ちゃんと食べて',
    'ちゃんとプログラミングして'
]
a=[]
for i in range(len(s)):
    a.append(int(input(s[i]+'ますか？>')))
for i in range(len(s)):
    if a[i] == 0:
        print(s[i])