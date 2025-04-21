def get_length(dir, dir_lst):
    lengths = []
    length = 0

    for i in range(dir):
        if i in dir_lst:
            lengths.append(length)
            length = 0
        length += 1
    lengths.append(length)

    return lengths


w, h = map(int, input().split())
cut = int(input())
widths = []
heights = []

for _ in range(cut):
    dir, num = map(int, input().split())
    if dir == 0:
        heights.append(num)
    else:
        widths.append(num)

w_length = get_length(w, widths)
h_length = get_length(h, heights)

max_v = 0
for x in w_length:
    for y in h_length:
       max_v = max(x*y, max_v)

print(max_v)