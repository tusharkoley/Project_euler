import numpy as np

def get_sprial_mat(n):
    
    if n==1:
        return np.ones((1,1))
    
    mat = np.ones((n,n))    
    mat[1:n-1,1:n-1] = get_sprial_mat(n-2)    
    mat[1:n,n-1]=list(range((n-2)**2 + 1 , (n-2)**2 + n))        
    mat[n-1,0:n-1] = list(range( (n-2)**2 + 2*n-2, (n-2)**2 + n-1,-1))    
    mat[0:n-1,0] = list(range((n-2)**2 + 3*n-3, (n-2)**2 + 2*n-2, -1))    
    mat[0,1:n] = list(range((n-2)**2 + 3*n-2, (n-2)**2 + 4*n-3))
    
    return mat


mat = get_sprial_mat(1001)
print (int(sum (mat.diagonal()) + sum(np.fliplr(mat).diagonal()) -1))