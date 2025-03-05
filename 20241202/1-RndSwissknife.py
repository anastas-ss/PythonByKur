import random
from collections.abc import Sequence, Iterable

def rnd(a, b=None):
    if isinstance(a, str) and isinstance(b, int):
        start = random.randint(0, len(a) - b)
        return a[start:start + b]
    
    match (a, b):
        case (int(), None):
            return random.randint(0, a)
        
        case (int(), int()):
            return random.randint(a, b)
        
        case (float(), float()):
            return random.uniform(a, b)
        
        case (float(), int()) | (int(), float()):
            return random.uniform(a, b)
        
        case (str(), None):
            return random.choice(a.split())
        
        case (str(), str()):
            return random.choice(a.split(b))
        
        case (Sequence(), None):
            return random.choice(a)
        
        case (Sequence(), int()):
            return random.choices(a, k=b)
        
        case (Iterable(), None):
            return random.choice(list(a))
        
        case (Iterable(), int()):
            return random.choices(list(a), k=b)