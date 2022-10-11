

def q(*args, **kwargs):
    a = [str(i) for i in args]
    s = sum(args)

    if kwargs["mode"] == "+":
        a = kwargs["+"].join(a)
    else:
        a = " ".join(a)
    print(kwargs)
    return a + " = " + str(s)

print(q(1, 2, 3, a = "+"))
