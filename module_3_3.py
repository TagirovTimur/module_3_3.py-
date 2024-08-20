
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(2,5)
print_params(23,52,"12")
print()
print_params(b=25)
print_params(c = [1,2,3])
print()
values_list = [False,"второе",12]
values_dict = { 'a' : False, 'b' : "2", 'c' : 33}
print_params(*values_list)
print_params(**values_dict)
print()
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)