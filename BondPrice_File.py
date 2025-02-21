import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):

    r = y / ppy
    N = m * ppy
    C = (couponRate * face) / ppy
    t = np.arange(1, N+1)

    pv_coupons = C / (1 + r) ** t
    pv_face = face / (1 + r) ** N
    bond_price = np.sum(pv_coupons) + pv_face

    return round(bond_price, 2)  


y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

bond_price = getBondPrice(y, face, couponRate, m, ppy)


print(round(bond_price, 2))  
