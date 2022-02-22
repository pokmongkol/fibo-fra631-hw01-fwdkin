import numpy as np

def DH(a, alpha, d, theta):
    return np.round([
        [np.cos(theta), -1*np.cos(alpha)*np.sin(theta), np.sin(alpha)*np.sin(theta), a*np.cos(theta)],
        [np.sin(theta), np.cos(alpha)*np.cos(theta), -1*np.sin(alpha)*np.cos(theta), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1],
    ], 3)

## PARAMETERS.
TH1 = 30 # DEGREE
TH2 = 0 # DEGREE
TH3 = 60 # DEGREE
TH4 = 0 # DEGREE
TH5 = 0 # DEGREE
TH6 = 0 # DEGREE

ALP1 = 0 # DEGREE
ALP2 = -90 # DEGREE
ALP3 = 0 # DEGREE
ALP4 = -90 # DEGREE
ALP5 = 90 # DEGREE
ALP6 = -90 # DEGREE

A1 = 40
A2 = 35
A3 = 10
A4 = 15
A5 = 23
A6 = 30

D1 = 0
D2 = 0
D3 = 0
D4 = 0
D5 = 0
D6 = 0

## DEGREE TO RADIUS.
TH1 = (TH1/180.0)*np.pi
TH2 = (TH2/180.0)*np.pi
TH3 = (TH3/180.0)*np.pi
TH4 = (TH4/180.0)*np.pi
TH5 = (TH5/180.0)*np.pi
TH6 = (TH6/180.0)*np.pi
ALP1 = (ALP1/180.0)*np.pi
ALP2 = (ALP2/180.0)*np.pi
ALP3 = (ALP3/180.0)*np.pi
ALP4 = (ALP4/180.0)*np.pi
ALP5 = (ALP5/180.0)*np.pi
ALP6 = (ALP6/180.0)*np.pi

## FRAME1.
H01 = DH(A1, ALP1, D1, TH1)
print('H01 = ', np.matrix(H01))
## FRAME2.
H12 = DH(A2, ALP2, D2, TH2)
print('H02 = ', np.matrix(H12))
## FRAME3.
H23 = DH(A3, ALP3, D3, TH3)
print('H03 = ', np.matrix(H23))
## FRAME4.
H34 = DH(A4, ALP4, D4, TH4)
print('H04 = ', np.matrix(H34))
## FRAME5.
H45 = DH(A5, ALP5, D5, TH5)
print('H05 = ', np.matrix(H45))
## FRAME6.
H56 = DH(A6, ALP6, D6, TH6)
print('H06 = ', np.matrix(H56))
## HOMOGENEOUS TRANSFORMATION.
H06 = np.round(np.linalg.multi_dot([H01, H12, H23, H34, H45, H56]), 3)
print('H06 = ', np.matrix(H06))