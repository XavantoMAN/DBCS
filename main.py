import queryModule as qm
import os

# 'SELECT=>tb;cond'
# 'CREATE=>tb;d1, d2 .. dn'
# 'UPDATE=>tb;id'
# 'DELETE=>tb;id'
# 'INSERT=>tb;d1, d2 .. dn'
while True:
    data = qm.query(input('>'))
    try:
        for i in data:
            print(i)
    except:
        pass
