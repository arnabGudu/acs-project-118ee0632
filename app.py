import streamlit as st
import numpy as np
from math import sqrt


if __name__ == '__main__':
    st.title("Advanced Control System Project")
    st.write("Arnab Paikaray (118ee0632)")

    st.write("Topic:")

    size = st.selectbox('Select Matrix Size', ('2x2', '3x3', '4x4', '5x5'))
    size = int(size[0])
    input_matrix = []

    st.write('Enter matrix elements: ')
    for row in range(size):
        cols = st.beta_columns(size)
        row_val = []
        for i, col in enumerate(cols):
            row_val.append(float(col.text_input(str(f'({row+1}, {i+1})'), key=row*size+i)))
        input_matrix.append(row_val)

    st.write('')
    power = st.number_input('Enter Power: ', min_value=1, value=1)
    if st.button('Calculate'):
        print(input_matrix)
        M = np.matrix(input_matrix)
        P = np.linalg.matrix_power(M, power)
        print(P)
        st.write('Output Matrix: ')
        for row in range(size):
            cols = st.beta_columns(size)
            for i, col in enumerate(cols):
                col.write(f'{P.item((row, i))}')
