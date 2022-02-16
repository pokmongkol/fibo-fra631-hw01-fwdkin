import numpy as np

def DH(a, alpha, d, theta):
    return [
        [np.cos(theta), -1*np.cos(alpha)*np.sin(theta), np.sin(alpha)*np.sin(theta), a*np.cos(theta)],
        [np.sin(theta), np.cos(alpha)*np.cos(theta), -1*np.sin(alpha)*np.cos(theta), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ]


## PARAMETERS.
TH1 = 30 # DEGREE
TH2 = 0 # DEGREE
TH3 = 60 # DEGREE
TH4 = 0 # DEGREE
TH5 = 0 # DEGREE
TH6 = 0 # DEGREE

L0 = 1
L1 = 1
L2 = 1
L3 = 0
L4 = 0
L5 = 0

## DEGREE TO RADIUS.
TH1 = (TH1/180.0)*np.pi
TH2 = (TH2/180.0)*np.pi
TH3 = (TH3/180.0)*np.pi
TH4 = (TH4/180.0)*np.pi
TH5 = (TH5/180.0)*np.pi
TH6 = (TH6/180.0)*np.pi

## FRAME1.
H01 = DH(L0, 0, 0, TH1)
# print('H01 = ', np.matrix(H01))

## FRAME2.
H12 = DH(L1, -90, 0, TH2)
# print('H02 = ', np.matrix(H12))

## FRAME3.
H23 = DH(L2, 0, 0, TH3)
# print('H03 = ', np.matrix(H23))

## FRAME4.
H34 = DH(L3, -90, 0, TH4)
# print('H04 = ', np.matrix(H34))

## FRAME5.
H45 = DH(L4, 90, 0, TH5)
# print('H05 = ', np.matrix(H45))

## FRAME6.
H56 = DH(L5, -90, 0, TH6)
# print('H06 = ', np.matrix(H56))

# HOMOGENEOUS TRANSFORMATION.
H06 = np.linalg.multi_dot([H01, H12, H23, H34, H45, H56])
print('H06 = ', np.matrix(H06))