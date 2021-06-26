'''
go to https://acs-project-118ee0632.herokuapp.com/
or
install requirement.txt and use "streamlit run app.py" to run web api
'''
import streamlit as st
import numpy as np
from math import sqrt


def matrix_power(matrix):
    M = np.matrix(input_matrix)
    P = np.linalg.matrix_power(M, power)
    return P


if __name__ == '__main__':
    st.title("Advanced Control System Project")
    st.write("Arnab Paikaray (118ee0632)")

    st.header("Calculate Matrix Raised to Power K")

    size = st.selectbox('Select Matrix Size', ('2x2', '3x3', '4x4', '5x5'))
    size = int(size[0])
    input_matrix = []

    st.subheader('Enter matrix elements: ')
    for row in range(size):
        cols = st.beta_columns(size)
        row_val = []
        for i, col in enumerate(cols):
            row_val.append(col.text_input(str(f'({row+1}, {i+1})'), key=row*size+i))
        input_matrix.append(row_val)

    power = st.number_input('Enter Power, K: ', min_value=1, value=1)
    if st.button('Calculate'):
        input_matrix = [[float(x) for x in row] for row in input_matrix]
        M = np.matrix(input_matrix)
        P = np.linalg.matrix_power(M, power)
        st.write('Output Matrix: ')
        for row in range(size):
            cols = st.beta_columns(size)
            for i, col in enumerate(cols):
                col.write(f'{P.item((row, i))}')
