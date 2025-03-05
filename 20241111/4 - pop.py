import re, sys
from collections import defaultdict

def parse_classes(code):
    class_pattern = re.compile(r'classs+(w+)(s*(s*([w,s]*)s*))?:')
    classes = {}
    
    for line in code.splitlines():
        match = class_pattern.match(line)
        if match:
            class_name = match.group(1)
            parents = match.group(3)
            if parents:
                parents = [p.strip() for p in parents.split(',')]
            else:
                parents = []
            classes[class_name] = parents
    
    return classes

def c3_mro(class_name, classes):
    if class_name not in classes:
        return None
    
    mro = []
    visited = set()
    temp = []

    def merge(sequences):
        result = []
        while any(sequences):
            for seq in sequences:
                if not seq:
                    continue
                candidate = seq[0]
                if candidate not in result:
                    if all(candidate not in s[1:] for s in sequences):
                        result.append(candidate)
                        for s in sequences:
                            if s and s[0] == candidate:
                                s.pop(0)
                        break
            else:
                return None 
        return result
    
    def visit(cls):
        if cls in visited:
            return
        visited.add(cls)
        
        if cls in classes:
            parents = classes[cls]
            for parent in parents:
                visit(parent)
        
        temp.append(cls)
    
    visit(class_name)
    
    sequences = [temp] + [classes[cls] for cls in temp]
    mro = merge(sequences)

    return mro

def check_c3(classes):
    for class_name in classes:
        mro = c3_mro(class_name, classes)
        if mro is None or class_name not in mro:
            return False
        
        for parent in classes[class_name]:
            if parent not in mro:
                return False
            
            index = mro.index(parent)
            for child in classes[class_name]:
                if child in mro[index + 1:]:
                    return False
                
    return True

def main(code):
    if isinstance(code, list):
        code = "\n".join(code)
    
    classes = parse_classes(code)
    
    if check_c3(classes):
        print("Yes")
    else:
        print("No")



code = sys.stdin.read()

main(code)
