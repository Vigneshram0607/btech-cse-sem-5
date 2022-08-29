import math

PI = 3.14


def short_dist(x, y, z, sx, sy, sz):
    dis = 0.0
    temp_ls = []
    # print(sx,sy,sz)
    if (z == sz and (x == sx or y == sy) and sz != 0):  # if the Z-axis and any one of the X-axis or Y-axis is same.

        if (x != sx):  # if the next co-ordinate’s x axis is same
            dis = (2*PI * (abs(x-sx)))/6.0

        else:  # if the next co-ordinate’s Y axis is same
            dis = (2 * PI * (abs(y-sy)))/6.0


    else:  # if bee is moving to another face
        # dis = int((math.sqrt(pow(x-sx,2) + pow(y-sy, 2)) + abs(z – sz)))  # find eculidean distance between x and y and the abs distance of Z axis
        dis = int((math.sqrt(pow(x-sx,2) + pow(y-sy,2) + pow(z-sz,2) )))
        # assigning new starting cordinate as bee moved to that point
        sx = x
        sy = y
        sz = z
        temp_ls = [dis, sx, sy, sz]
        # return dis, sx, sy, sz
        return temp_ls

n = int(input())
points = list(map(int, input().split(',')))
print(type(points))
# starting co-ordinate
sx = points[0]
sy = points[1]
sz = points[2]
sum = 0
ls = []
# traverse the list
for i in range(3, 3 * n, 3):
    ls = short_dist(points[i], points[i + 1], points[i + 2], sx, sy, sz)
    x = ls[0]
    sx = ls[1]
    sy=ls[2]
    sz=ls[3]
    sum = sum + x

print(round(sum, 2))