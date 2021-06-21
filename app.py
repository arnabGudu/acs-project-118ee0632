import streamlit as st
import numpy as np
from sympy import Matrix
from math import sqrt
I = 1

if __name__ == '__main__':
    st.title("ACS Project")
    st.write("By Arnab Paikaray (118ee0632)")

    size = st.selectbox('Select Matrix Size', ('2x2', '3x3', '4x4', '5x5'))
    size = int(size[0])
    input_matrix = []

    st.write('Enter matrix elements: ')
    for row in range(size):
        cols = st.beta_columns(size)
        row_val = []
        for i, col in enumerate(cols):
            row_val.append(col.text_input(str(f'({row+1}, {i+1})'), key=row*size+i))
        input_matrix.append(row_val)

    if st.button('Calculate'):
        M = Matrix(input_matrix)
        P, D = M.diagonalize()
        # print("Diagonal of a matrix : {}".format(D))

        D = np.array(D)
        st.write('Output Matrix: ')
        for row in range(size):
            cols = st.beta_columns(size)
            row_val = []
            for i, col in enumerate(cols):
                col.write(f'{eval(str(D[row][i])):.2f}')
