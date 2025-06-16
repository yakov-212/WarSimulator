def bubble_Sort(my_list):
    n = len(my_list)

    for i in range(n):
        for j in range(n):
            for k in range(n-1-i):
                if my_list[j][k] != 0 and my_list[j][k+1] == 0:
                    my_list[j][k], my_list[j][k+1] = my_list[j][k+1], my_list[j][k]

        
    
    return my_list
board = [[0,4,8,2],
        [4,0,1,2],
        [2,0,0,0],
        [1,1,0,0]]
print(bubble_Sort(board))


