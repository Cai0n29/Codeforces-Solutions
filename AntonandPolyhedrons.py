n = int(input())
shapes =0
for i in range(n):

    k = input().lower()
    if k == 'tetrahedron':
        shapes = shapes + 4
    elif k == 'cube':
        shapes = shapes + 6
    elif k == 'octahedron':
        shapes = shapes + 8
    elif k == 'dodecahedron':
        shapes = shapes + 12
    elif k == 'icosahedron':
        shapes = shapes + 20

print(shapes)