def calc_expr(values):
    expr = change_operators(
        values, {'add': '+', 'sub': '-', 'mult': '*', 'div': '/'})
    
    return eval("".join(expr))

def change_operators(values, context):
    return list(map(lambda x: context[x] if x.isalpha() else x, values))
