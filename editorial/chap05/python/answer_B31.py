# 입력
N = int(input())

# 計算
A1 = (N //   3); # 3 で割り切れるものの個数
A2 = (N //   5); # 5 で割り切れるものの個数
A3 = (N //   7); # 5 で割り切れるものの個数
A4 = (N //  15); # 3, 5 で割り切れるもの（= 15 の倍数）の個数
A5 = (N //  21); # 3, 7 で割り切れるもの（= 21 の倍数）の個数
A6 = (N //  35); # 5, 7 で割り切れるもの（= 35 の倍数）の個数
A7 = (N // 105); # 3, 5, 7 で割り切れるもの（= 105 の倍数）の個数

# 출력
print(A1 + A2 + A3 - A4 - A5 - A6 + A7)
