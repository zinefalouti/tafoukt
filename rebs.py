
from collections import Counter

# Mock Data
data = [
    [1, 3, 0, 6, 7, 0, 1, 2, 4, 6, 4],
    [0, 2, 5, 7, 9, 4, 3, 1, 2, 0, 3],
    [7, 9, 1, 9, 13, 12, 19, 31, 0, 0, 1],
    [79, 12, 13, 46, 12, 36, 19, 0, 0, 0, 6],
    [1, 3, 0, 6, 7, 0, 1, 2, 4, 6, 3],
    [0, 2, 5, 7, 9, 4, 3, 1, 2, 0, 1],
    [7, 9, 1, 9, 13, 12, 19, 31, 0, 0, 3],
    [79, 12, 13, 46, 12, 36, 19, 0, 0, 0, 6],
    [0, 2, 5, 7, 9, 4, 3, 1, 2, 0, 1]
]

# Mock Objectives for Local Testing
objectives = [1,6,7,3,4]

# Initialize consumed set and matches list globally
consumed = set()
matches = []

#Main To Test Locally
def main():
    result = allin(data, objectives, (1,1), 1, 1, False)
    for r in result:
        print(f"Found {r[0]} at X:{r[1]} and Y: {r[2]}")

#Function To Import From Other Files
def allin(data, objectives, expansion=(1,1), hprec=1, vprec=1, debug=False):
    global matches
    x, y = center(data)
    initialize(data, objectives, (x, y), expansion, hprec, vprec, debug)
    expand_rythm(data, objectives, (x, y), expansion, hprec, vprec, debug)
    
    if debug:
        counter = Counter(t[0] for t in matches)
        duplicates = {key: count for key, count in counter.items() if count > 1}
        print("-"*33)
        for key, value in duplicates.items():
            print(f"For objective {key} there are: {value} results found")
        print("-"*33)
        visualize(data, (x, y), matches)

    return matches

#Preview Stats Globally
def overview(matches):
    counter = Counter(t[0] for t in matches)
    duplicates = {key: count for key, count in counter.items() if count > 1}
    return duplicates

#Function Picking The Matrix Center
def center(d):
    try:
        if d and d[0]:
            (centerX, centerY) = int(len(d[0])/2), int(len(d)/2)
            return (centerX, centerY)
        else:
            print("Error! Data is empty or malformed.")
            return None
    except (IndexError, ValueError):
        print("Error! Data Insufficient or Invalid Format.")
        return

#Function Initializing First Draw
def initialize(data, objectives, center, vector=(1,1), hprec=1, vprec=1, debug=False):
    global matches
    x, y = center
    w, h = vector
    fetched = []    

    # Check for small precision or radius scale
    w = max(w, 1)
    h = max(h, 1)
    
    # Clamp Precision
    hprec = max(min(hprec, 1), 0.1)
    vprec = max(min(vprec, 1), 0.1)

    width = range(x - int(w * hprec), x + int(w * hprec) + 1)
    height = range(y - int(h * vprec), y + int(h * vprec) + 1)

    consumed.clear() 
    for row in height:
        for col in width:
            if 0 <= row < len(data) and 0 <= col < len(data[0]):
                for o in objectives:
                    if o == data[row][col]:
                        matches.append((data[row][col], col, row))
                        consumed.add((row, col))

    return fetched

#Base Expand Function
def expand(data, objectives, center, expansion=(1,1), hprec=1, vprec=1, debug=False):
    global consumed, matches
    x, y = center
    vectorx, vectory = expansion
    result = []
    crust = set()

    hprec = max(min(hprec, 1), 0.1)
    vprec = max(min(vprec, 1), 0.1)

    for i in range(-vectorx - 1, vectorx + 2):
        if 0 <= x + i * hprec < len(data[0]): 
            for j in range(-vectory - 1, vectory + 2):
                if 0 <= y + j * vprec < len(data):
                    crust.add((int(x + i * hprec), int(y + j * vprec)))

    crust -= consumed 

    for c in crust:
        cellx, celly = c
        for o in objectives:
            if o == data[celly][cellx]:
                result.append(data[celly][cellx])
                matches.append((data[celly][cellx], cellx, celly))

    consumed.update(crust) 
    return result
 
#Looping Expand
def expand_rythm(data, objectives, center, expansion=(1,1), hprec=1, vprec=1, debug=False):
    vectorX, vectorY = expansion
    maxX = len(data[0]) - (2 * vectorX + 1)
    maxY = len(data) - (2 * vectorY + 1)
    x, y = center
    max_expand_x = int(maxX / vectorX)
    max_expand_y = int(maxY / vectorY)
    loops = int(min(max_expand_x, max_expand_y))

    if loops < 1:
        print("Expansion vector is too big for the data, please reduce it a bit.")
    else:
        expandX, expandY = vectorX, vectorY
        for _ in range(loops):
            expand(data, objectives, (x, y), expansion=(expandX, expandY), hprec=hprec, vprec=vprec, debug=debug)
            expandX += vectorX
            expandY += vectorY

#Visualizer
def visualize(data, center, matches):
    try:
        x, y = center
        for i, row in enumerate(data): 
            for j, cell in enumerate(row):  
                if i == x and j == y: 
                    print("C", end=" ") 
                else:
                    match_found = False
                    for result, posX, posY in matches:
                        if posX == i and posY == j:
                            print(f"R:{result}", end=" ") 
                            match_found = True
                            break
                    if not match_found:
                        print("*", end=" ")
            print()

    except (ValueError, IndexError):
        print("Error! Data is corrupt or non-existent to visualize.")

#Function For Benchmark
def parseRaw(data, objectives):


    result = []
    for index, d in enumerate(data):
        for linedx, line in enumerate(d): 
            for o in objectives:
                if o == line:
                    result.append((o, linedx, index))  
    return result

if __name__ == "__main__":
    main()