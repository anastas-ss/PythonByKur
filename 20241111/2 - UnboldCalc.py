def calculator():
    variables = {}
    
    while True:
        try:
            line = input().strip()
            if not line:
                break
            
            if line[0] == '#':
                continue
            
            if '=' in line:
                left, right = line.split('=', 1)
                left = left.strip()
                right = right.strip()

                if not left.isidentifier():
                    print("Assignment error")
                else:
                    try:
                        result = eval(right, {"__builtins__": {}}, variables)
                        variables[left] = result
                    except SyntaxError:
                        print("Syntax error")
                    except NameError:
                        print("Name error")
                    except Exception:
                        print("Runtime error")
            else:
                try:
                    result = eval(line, {"__builtins__": {}}, variables)
                    print(result)
                except SyntaxError:
                    print("Syntax error")
                except NameError:
                    print("Name error")
                except Exception:
                    print("Runtime error")
        
        except EOFError:
            break
        except Exception as e:
            print("Runtime error")

calculator()