from io import StringIO
# 写入StringIO:
f = StringIO()
f.write('hello world!')
print(f.getvalue())
# 读取StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO
# 写入BytesIO:
f = BytesIO()
f.write(b'hello world!')
print(f.getvalue())
# 读取BytesIO:
data = '人闲桂花落，\n夜静春山空。\n月出惊山鸟，\n时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())