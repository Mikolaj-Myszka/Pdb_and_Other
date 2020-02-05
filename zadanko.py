# Case1
def fun(s_arg=[]):
    s_arg.append('Marcin')
    return s_arg

print(fun())
print(fun([]))
print(fun())


# Case2
# a = [1,2]
# b = a
# a = a + [3,4]
# print(a)
# print(b)


# Case3
# a = [1,2]
# b = a
# a += [3,4]
# print(a)
# print(b)
