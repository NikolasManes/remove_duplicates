count = 0
delta = 1


def main():
    global count
    global delta
    start_point = 0
    end_point = 2
    n = 64
    delta = abs(start_point - end_point) / n
    print(f"\n[{start_point} , {end_point}] , n = {n} | delta = {delta}\n")
    min_x = find_min(start_point, end_point, delta)
    print(f"\nf({min_x}) = {f_x(min_x)}\n")
    count = 0
    min_x = fast_find_min(start_point, end_point, delta)
    print(f"\nf({min_x}) = {f_x(min_x)}")
    exit(0)


def f_x(x):
    return 3 * x ** 3 - 2 * x


def df_dx(x):
    return (f_x(x+delta) - f_x(x-delta))/(2*delta)


def find_min(start, end, d):
    global count
    length = abs(end - start)
    middle = start + length / 2
    print(f"#{count}:  ({start:.6f}, {end:.6f}) - mid = {middle:.6f}, d = {length:8f}, f'(mid) = {df_dx(middle):6f}")
    count += 1
    if length > d:
        if df_dx(middle) > 0:
            return find_min(start, middle, d)
        elif df_dx(middle) < 0:
            return find_min(middle, end, d)
    else:
        if df_dx(middle) > 0:
            return start
        elif df_dx(middle) < 0:
            return end


def fast_find_min(start, end, d):
    global count
    length = abs(end - start)
    point_1 = start + length / 3
    point_2 = start + 2 * length / 3
    print(f"#{count}: ({start:.6f}, {end:.6f}) - p_1 = {point_1:.6f} , p_2 = {point_2:.6f} - d = {length/3:.6f} - "
          f" f'(p_1) = {df_dx(point_1):.4f} , f'(p_2) = {df_dx(point_2):.4f}")
    count += 1
    if length > d:
        if df_dx(point_1) > 0:
            return fast_find_min(start, point_1, d)
        elif df_dx(point_2) < 0:
            return fast_find_min(point_2, end, d)
        else:
            return fast_find_min(point_1, point_2, d)
    else:
        if df_dx(point_1) > 0:
            return start
        elif df_dx(point_2) <= 0:
            return end


main()
