import numpy as np 

def GaussianElimination(mat): 
    """
    Calculate Gaussian elimination form of a square matrix A. 
    """
    A = mat.copy()
    n = A.shape[0]
    
    for i in range(n):
        if i+1 < n:
            for j in range(i+1,n):
                factor = - A[j,i]/A[i,i]
                A[j,:] = A[j,:] +  factor*A[i,:]  
                
    return A


B = np.array([[2, 0, -1], 
              [3, 1, 1],
              [0, -1, 1]])
GaussianElimination(B)