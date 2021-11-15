

def try_me(a_list):
    if type(a_list) == list:
        for i, j in enumerate(a_list):
        print(i, j)
    else:
        print('Enter a list')
