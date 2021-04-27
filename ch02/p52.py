# 특정 글자 수 변환
oneLine = "this is one line string"
print('t 글자 수 : ', oneLine.count('t'))

# 접두어 문자 비교 판단
print(oneLine.startswith('this'))
print(oneLine.startswith('that'))

# 문자열 교체
print(oneLine.replace('this', 'that'))

# 문자열 분리(split)
multiLine = """
this is
multi line
string
"""
sent = multiLine.split('\n')
print('문장 : ', sent)

# 문자열 분리 2
words = oneLine.split(' ')
print('단어 : ', words)

# 문자열 결합(join)
sent2 = ','.join(words)
print(sent2)

