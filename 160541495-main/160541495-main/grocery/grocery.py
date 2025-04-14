dic={}
try:
    while True:
        x=input("")
        x=x.upper()
        if x in dic:
            dic[f"{x}"] = dic[f"{x}"]+1
        else:
            dic[f"{x}"] = 1
except EOFError:
    s_dic={k:dic[k] for k in sorted(dic)} #ojoooooooooo

    for key, value in s_dic.items():
        print(f"{value} {key}")
    pass
