class wire:
    def __init__(self, path):
        self.coords = self.draw(path)

    def trace(self, path):
        step = {'U':(0,1),
                'D':(0,-1),
                'L':(-1,0),
                'R':(1,0)}
    
        x = y = 0
    
        for seg in path:
            dx,dy = step[seg[0]]
            length = int(seg[1:])
    
            for n in range(length):
                x += dx
                y += dy
                yield x, y
    
    def draw(self, path):
        coords = {}
    
        for path_length, coord in enumerate(self.trace(path), 1):
            if coord not in coords:
                coords[coord] = path_length
    
        return coords


if __name__ == "__main__":
    input_data = open("day3.txt", 'r')
    path1 = input_data.readline()
    path2 = input_data.readline()

    wire1 = wire(path1.split(','))
    wire2 = wire(path2.split(','))

    intersections = wire1.coords.keys() & wire2.coords.keys()

    print(min(abs(x)+abs(y) for x,y in intersections))
    print(min(wire1.coords[coord] + wire2.coords[coord] for coord in intersections))
