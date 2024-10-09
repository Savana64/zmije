assert 3+2 == 5
assert 9+5 == 5

def foo(l):
    assert type(l) == list
    l.append(42)

# assert = předpolkádám, že je to tak, ale je to pomapé, složité
    
# existuje unittest

import inuttest
class  TestSum ()# nemá kostruktor, ale to neva klas dědí z unittestu