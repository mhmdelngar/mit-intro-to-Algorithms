def solve_tilt(B, t):
    '''
    Input:  B | Starting board configuration
            t | Tuple t = (x, y) representing the target square
    Output: M | List of moves that solves B (or None if B not solvable)
    '''
    M = []
    if B[t[1]][t[0]] == 'o':
        M.append(B)
        return M
 
    rightspot=None
    level=[[B]]
    parent ={B:[B,'']}
    while 0 < len(level[-1]):
        level.append([])
    
        for m in level[-2] :
            up=move(m, 'up')
            down=move(m, 'down')
            right=move(m, 'right')
            left=move(m, 'left')
            lis=[[up,'up'],[right,'right'],[left,'left'],[down,'down']]
            for z in lis:
                level[-1].append(z[0])
            for adi in lis:
                if parent.get(adi[0]) is None: 
                    parent[adi[0]]=[m,adi[1]]
                l= t[1]      
                if adi[0][t[1]][t[0]]== 'o' :    
                    rightspot=[m,adi[1]]
                    break
            if   rightspot is not None:
                break  
        if   rightspot is not None:
                break


    if rightspot is None :
        return M 
    else :
        while rightspot[1] !='':
            M.append(rightspot[1])
            rightspot=parent[rightspot[0]]
    M.reverse()  
    return M

####################################
# USE BUT DO NOT MODIFY CODE BELOW #
####################################
def move(B, d):
    '''
    Input:  B  | Board configuration
            d  | Direction: either 'up', down', 'left', or 'right'
    Output: B_ | New configuration made by tilting B in direction d
    '''
    n = len(B)
    B_ = list(list(row) for row in B)
    if d == 'up':
        for x in range(n):  
            y_ = 0          
            for y in range(n):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ += 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'down':
        for x in range(n):  
            y_ = n - 1
            for y in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ -= 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'left':
        for y in range(n):  
            x_ = 0          
            for x in range(n):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ += 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    if d == 'right':
        for y in range(n):  
            x_ = n - 1
            for x in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ -= 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    B_ = tuple(tuple(row) for row in B_)
    return B_

def board_str(B):
    '''
    Input:  B | Board configuration
    Output: s | ASCII string representing configuration B
    '''
    n = len(B)
    rows = ['+' + ('-'*n) + '+']
    for row in B:
        rows.append('|' + ''.join(row) + '|')
    rows.append(rows[0])
    S = '\n'.join(rows)
    return S
