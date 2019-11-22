def f(x):
    return 3*x + 1

print(f(2))


### the same with lambda ###
l = lambda x: 3*x + 1
print(l(2))


## Combine first name and last name into a single "Full Name"
full_name = lambda fn,ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("   leonard", "EULER"))


# lambda with no name
scifi_authors = ["Alberto Sousa", "K.C. Jones", "Bardo jones Zizi"]

# help(scifi_authors.sort) # if needed

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)


## Then we go deeper, we will write a function that makes functions
def build_quadratic_function(a, b, c):
    """Returns the function f(x)=ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2,3,-5)
print(f(0))
print(f(1))
print(f(2))


print(build_quadratic_function(3,0,1)(2)) # 3x^2+1 evaluated for x=2
