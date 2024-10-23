def superposition(funmod, funseq):
    funres = []
    for f in funseq:
        def fun(x, func=f):
            return funmod(func(x))
        funres.append(fun)
    return funres