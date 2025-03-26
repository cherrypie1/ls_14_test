# a, b, c, d = bool(input("Input a,b,c,d: ")), bool(input()), bool(input()), bool(input())
# f = not a and (b or c) or d
# temp_f = (a or b) and (not c or d)
#
# print("Result: ", f, temp_f)

# time = int(input())
# hour = time // 3600
# time %= 3600
# int_min = time // 60
# time %= 60
# print(hour, int_min, time)

a = int(input())
int_cel = a//10
int_ost = a % 10
#res = int_cel + int_ost
res = int_ost*10 + int_cel
print(res)
