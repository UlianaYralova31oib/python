def print_list (lst, index):
    if index < len (lst):
        print (lst [index])
        print_list(lst,index+1)
    else:
        print("Конец списка")
        my_list=[0 ,1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12, 13 ,14 ,15 ,16]
        print_list(my_list,0)
        
