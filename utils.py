from math import pow

def GetPoint(index, length=1, level=1, offset=False):
    points = [
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0]
    ]
    i = index & 3
    point = points[i]

    for x in range(1, level):
        val = pow(2, x)
        
        index = index >> 2
        i = index & 3

        if i == 0:
            point[0], point[1] = point[1], point[0]
            
        elif i == 1:
            point[1] += val

        elif i == 2:
            point[0] += val
            point[1] += val

        elif i == 3:
            point[0], point[1] = val-1-point[1], val-1-point[0]
            point[0] += val
        
    point = [
        point[0] * length, 
        point[1] * length
    ]

    if offset:
        point = [
            point[0] + length/2, 
            point[1] + length/2
        ]

    return point



    
