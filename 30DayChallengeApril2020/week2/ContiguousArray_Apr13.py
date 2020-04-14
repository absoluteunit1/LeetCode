# ****review the solution!!! ****

def findMaxLength(nums):
    c,d,m = 0,{0:0},0
    for i,v in enumerate(nums):
        c += 2*v -1
        if c in d:
            m = max(m,i+1-d[c])
        else:
            d[c] = i+1                
    return m 


a = [1,0,1,0,1,1,1]
