#!/usr/bin/python3
def matrix_mul(m_a, m_b):

    #[[1,2] [[1,2]
    #[3,4]] [3,4]]

    new_m = [a[:] for a in m_a]

    for i in range(len(m_a)):
        for j in range(0,len(m_a[0])):
            print(m_a[j][i])
            m_a[i][j] = m_a[j][i]


   
    return new_m
