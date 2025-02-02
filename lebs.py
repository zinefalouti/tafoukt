#Imports
import random
from collections import defaultdict, Counter
import numpy as np

#Generate Mock Matrix & Objectives
rows = 1400 
cols = 1400 

data = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

objectives = [3,1,6]

#Main Function
def main():
    learner(data,objectives,(350,350))


#Assembly Function to Execute From Other Py files
def learner(data, objectives, vector=(1,1), brutal=False):
    results = parsesectors(data, objectives, vector, brutal)
    stats = overview(results)

    #Printing Stats
    for sector, values in stats.items():
        print(f"In sector {sector}:")
        for value, count in values.items():
            print(f"  - For value {value}, we found a total of {count}")

    viz(data, vector)
    
    return results


#Sector Referential Logic
def parsesectors(data,objectives,vector=(1,1), brutal=False):
    sx, sy = vector

    sdata = np.array(data)

    totalx = int(len(data[0])/sx)
    totaly = int(len(data)/sy)

    matches = []

    sector = 0

    #Learning Process
    if not brutal:
        pattern_y0, pattern_x0 = singlepattern(sdata[0:sy,0:sx],objectives)
        pattern_ymid, pattern_xmid = singlepattern(sdata[int(totaly/2)*sy:(int(totaly/2)*sy)+sy,int(totalx/2)*sx:(int(totalx/2)*sx)+sx],objectives)
        pattern_ylast, pattern_xlast = singlepattern(sdata[(totaly-1)*sy:, -sx:], objectives)

        pattern_y, pattern_x = globalpattern(pattern_y0,pattern_x0,pattern_ymid,pattern_xmid,pattern_ylast,pattern_xlast)


    for row in range(totaly):
        for col in range(totalx):
            currentarr = sdata[row*sy:(row+1)*sy,col*sx:(col+1)*sx]
            
            if not brutal:
                for py in pattern_y:
                    for px in pattern_x:
                        if 0 <= py < len(currentarr) and 0 <= px < len(currentarr[0]):
                            item = currentarr[py][px]
                            if item in objectives:
                                matches.append({'value':item,'position':(px,py),'sector':sector})
            else:
                for iy, row_data in enumerate(currentarr):
                    for ix, col_data in enumerate(row_data):
                        if col_data in objectives:
                            matches.append({'value':col_data,'position':(ix,iy),'sector':sector})

            sector += 1
        
    
    return matches
    
 
#Stats Overview
def overview(matches):
    sector_summary = defaultdict(Counter)

    # Aggregate counts per sector
    for match in matches:
        value = match['value']
        sector = match['sector']
        sector_summary[sector][value] += 1

    # Convert to a more readable format
    summary = {sector: dict(counts) for sector, counts in sector_summary.items()}
    
    return summary


#Single Pattern Function
def singlepattern(array, objectives):
    
    pattern_y = []
    pattern_x = []

    for index_y, row in enumerate(array):
        for index_x, col in enumerate(row):
            if col in objectives:
                pattern_y.append(index_y)
                pattern_x.append(index_x)
    
    return pattern_y, pattern_x

#Poisson Layering the 3 Patterns
def globalpattern(p0y, p0x, pmidy, pmidx, ply, plx):
    sum_pattern_y = p0y + pmidy + ply
    sum_pattern_x = p0x + pmidx + plx

    lambda_y = np.mean(sum_pattern_y) if sum_pattern_y else 1 
    lambda_x = np.mean(sum_pattern_x) if sum_pattern_x else 1

    global_pattern_y = set(np.random.poisson(lambda_y, size=len(sum_pattern_y)))
    global_pattern_x = set(np.random.poisson(lambda_x, size=len(sum_pattern_x)))
    
    return sorted(global_pattern_y), sorted(global_pattern_x)

#Sector Visualizer
def viz(data, vector=(1,1)):
    sx, sy = vector

    totalx = int(len(data[0])/sx)
    totaly = int(len(data)/sy)

    counter = 0
    print('-'*totalx*9)     
    for row in range(totaly):     
        for col in range(totalx):            
            print(f'| S:{(col+counter)} | ', end = " ")       
        counter += totalx 
        print("\n")
    print('-'*totalx*9)   
        
        
            

if __name__ == '__main__':
    main()