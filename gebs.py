#Necessary Imports
import random
import numpy as np
from collections import defaultdict


#Generate Mock Matrix
rows = 1300 
cols = 1300 

data = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]


#Main Function To Test Locally
def main():
    objectives= [6,3,9]

    matches = oversee(data,objectives,(130,130), (0.2,0.7))



    print(overview(matches))


#Assembly Function To Use Outside
def oversee(data, objectives, vector=(1,1), gradient=(0.2,0.7)):
    d = np.array(data)
    core, rest = slicer(d,vector)
    pruned = pruning(rest,gradient)
    
    matched_objectives = []

    for array_name, array in [('Central Close Radius', core), ('Far Gradient Radius', pruned)]:

        if isinstance(array, np.ndarray):
            flattened = array.flatten() 
        else:
            flattened = (item for sublist in array for subsublist in sublist for item in subsublist)  

        for idx, element in enumerate(flattened):
            if element in objectives:
                matched_objectives.append({
                    'objective': element,
                    'position' : idx,
                    'area': array_name
                })

    return matched_objectives

#Global Stats Per Area
def overview(matched_objectives):
    # Create a dictionary to hold counts of objectives per area
    objectives_summary = defaultdict(lambda: defaultdict(int))
    
    # Loop through the matched objectives to count occurrences
    for match in matched_objectives:
        objective = match['objective']
        area = match['area']
        objectives_summary[objective][area] += 1
    
    # Prepare the summary in a structured format
    summary = []
    for objective, areas in objectives_summary.items():
        area_details = []
        for area, count in areas.items():
            area_details.append(f"Area '{area}': {count} times")
        summary.append(f"Objective '{objective}': " + ", ".join(area_details))
    
    return "\n".join(summary)


#Pruning the Gradient
def pruning(gradient,precision=(0.2,0.7)):
      
        min_precision , max_precision = precision

        min_precision = min(max(0.13, min_precision),0.7)
        max_precision = max(min(0.7, max_precision), 0.13)


        for index, g in enumerate(gradient):

            counter = sinusoidal(index, len(gradient), min_precision, max_precision)

            removetotalc = int(g.shape[1]*counter)
            removetotalr = int(g.shape[0]*counter)

            g = np.delete(g, np.s_[0:removetotalc], axis=1)
            g = np.delete(g, np.s_[0:removetotalr], axis=0)
            
            gradient[index]=g
        
        return gradient

#Gradient Function
def sinusoidal(t, length, minval, maxval):
    value = 0.5 * (1 + np.cos(np.pi * t / (length / 2))) * (maxval - minval) + minval
    return min(max(value, minval), maxval)


#Slicing the Data For the Spiral
def slicer(cdata, vector=(1,1)):
    vx, vy = vector

    cx, cy = (int(len(cdata[0])/2), int(len(cdata)/2))

    mdata0 = cdata[cy-vy:cy+vy,cx-vx:cx+vx]

    mdata1 = cdata[cy-vy:cy+vy,cx-(3*vx):(cx-vx)]

    mdata2 = cdata[cy-(3*vy):(cy-vy),cx-(3*vx):(cx-vx)]

    mdata3 = cdata[cy-(3*vy):cy-vy,cx-vx:cx+vx]

    mdata4 = cdata[cy-(3*vy):cy-vy,cx+vx:cx+(3*vx)]

    mdata5 = cdata[cy-vy:cy+vy,cx+vx:cx+(3*vx)]

    mdata6 = cdata[cy+vy:cy+(3*vy),cx+vx:cx+(3*vx)]

    mdata7 = cdata[cy+vy:cy+(3*vy),cx-vx:cx+vx]

    mdata8 = cdata[cy+vy:cy+(3*vy),cx-(3*vx):cx-vx]

    sliced = [mdata0,mdata1,mdata2,mdata3,mdata4,mdata5,mdata6,mdata7,mdata8]

    gradientzone = seq_slicer(cdata, (vx*2,vy*2))

    gradientzone = [f for f in gradientzone if not any(np.array_equal(f, s) for s in sliced)]

    return sliced, gradientzone


#Normal Slicer Function
def seq_slicer(data, vector=(1,1)):
    vx, vy = vector

    #Check How Many Slices Are Needed
    yslices = int(len(data)/(vy))
    xslices = int(len(data[0])/(vx))

    sliced = []

    for y in range(yslices+1):
        for x in range(xslices+1):
            # Ensure slice doesn't go out of bounds
            y_start = y * vy
            x_start = x * vx
            y_end = min((y + 1) * vy, len(data))
            x_end = min((x + 1) * vx, len(data[0]))
            sliced.append(data[y_start:y_end, x_start:x_end])
    
    return sliced

if __name__ == '__main__':
    main()