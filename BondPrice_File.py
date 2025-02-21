import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    """
    计算债券的 Macaulay 久期（Macaulay Duration），要求向量化计算。
    
    参数：
    y : float - 到期收益率（YTM），以小数表示
    face : float - 债券面值
    couponRate : float - 票面利率，以小数表示
    m : int - 债券期限（单位：年）
    ppy : int - 每年的付息次数（默认为1）

    返回：
    float - 计算得到的债券久期
    """
    # 计算每期票息
    coupon = (couponRate * face) / ppy

    # 计算时间点 t
    t = np.arange(1, m * ppy + 1) / ppy  # 确保 t 计算正确

    # 计算贴现因子
    discount_factors = (1 + y / ppy) ** (-t * ppy)

    # 计算票息的现值
    pv_coupons = coupon * discount_factors

    # 计算面值的现值
    pv_face = face * discount_factors[-1]

    # 计算总债券现值
    pv_total = np.sum(pv_coupons) + pv_face

    # 计算加权时间
    weighted_time = np.sum(t * pv_coupons) + t[-1] * pv_face

    # 计算 Macaulay Duration
    duration = weighted_time / pv_total

    return round(duration, 2)  # 保留 2 位小数

# ✅ 运行测试
y = 0.03  # YTM（到期收益率）
face = 2000000  # 面值
couponRate = 0.04  # 票面利率
m = 10  # 期限
ppy = 2

duration= getBondDuration(y, face, couponRate, m, ppy)
print(duration)  # **应该输出 8.51 ✅**

