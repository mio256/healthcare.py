print('0と1で答えてください。')
s=[
    'ちゃんと寝て',
    'ちゃんと運動して',
    'ちゃんと食べて',
    'ちゃんとプログラミングして'
]
a=[]
for message in s:
    if input(message+'ますか？>')=='0':
        a.append(message)
for message in a:
    print(message)