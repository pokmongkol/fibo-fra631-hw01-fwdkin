import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

def htTranslateZ(L):
    return [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, L], [0, 0, 0, 1]]
def htRotateY(TH):
    return [[np.cos(TH), 0, np.sin(TH), 0], [0, 1, 0, 0],  [-1*np.sin(TH), 0, np.cos(TH), 0], [0, 0, 0, 1]]
def htRotateZ(TH):
    return [[np.cos(TH), -1*np.sin(TH), 0, 0], [np.sin(TH), np.cos(TH), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

## PARAMETERS.
TH1 = 0.247 # DEGREE
TH2 = -90.697 # DEGREE
TH3 = 181.09 # DEGREE
TH4 = 360.922 # DEGREE
TH5 = 90.241 # DEGREE
TH6 = -0.333 # DEGREE

L0 = 40
L1 = 35
L2 = 10
L3 = 15
L4 = 23
L5 = 30

## DEGREE TO RADIUS.
TH1 = (TH1/180.0)*np.pi
TH2 = (TH2/180.0)*np.pi
TH3 = (TH3/180.0)*np.pi
TH4 = (TH4/180.0)*np.pi
TH5 = (TH5/180.0)*np.pi
TH6 = (TH6/180.0)*np.pi

## FRAME1.
T0 = htTranslateZ(L0)
# print('T0 = ', np.matrix(T0))
R0 = htRotateZ(TH1)
# print('R0 = ', np.matrix(R0))
H01 = np.dot(T0, R0)
print('H01 = ', np.matrix(H01))

## FRAME2.
T1 = htTranslateZ(L1)
# print('T1 = ', np.matrix(T1))
R1 = htRotateY(TH2)
# print('R1 = ', np.matrix(R1))
H12 = np.dot(T1, R1)
print('H12 = ', np.matrix(H12))

## FRAME3.
T2 = htTranslateZ(L2)
# print('T2 = ', np.matrix(T2))
R2 = htRotateY(TH3)
# print('R2 = ', np.matrix(R2))
H23 = np.dot(T2, R2)
print('H23 = ', np.matrix(H23))

## FRAME4.
T3 = htTranslateZ(L3)
# print('T3 = ', np.matrix(T3))
R3 = htRotateZ(TH4)
# print('R3 = ', np.matrix(R3))
H34 = np.dot(T3, R3)
print('H34 = ', np.matrix(H34))

## FRAME5.
T4 = htTranslateZ(L4)
# print('T4 = ', np.matrix(T4))
R4 = htRotateY(TH5)
# print('R4 = ', np.matrix(R4))
H45 = np.dot(T4, R4)
print('H45 = ', np.matrix(H45))

## FRAME6.
T5 = htTranslateZ(L5)
# print('T5 = ', np.matrix(T5))
R5 = htRotateY(TH6)
# print('R5 = ', np.matrix(R5))
H56 = np.dot(T5, R5)
print('H56 = ', np.matrix(H56))

## HOMOGENEOUS TRANSFORMATION.
H06 = np.linalg.multi_dot([H01, H12, H23, H34, H45, H56])
print('H06 = ', np.matrix(H06))
