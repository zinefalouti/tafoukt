import rebs
import random
import time
import gebs
import lebs

rows = 3600
cols = 3600 

data = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

start_time = time.time() 

objectives = [2,6,3,9]

#result = rebs.allin(data,objectives,(360,360),1,1,False) #Using R.E.B.S

#result = gebs.oversee(data,objectives,(260,260),(0.7,0.7)) #Using G.E.B.S

#result = rebs.parseRaw(data,objectives)  #Using Python Raw Loop

result = lebs.learner(data,objectives,(630,630),False) #Using L.E.B.S

end_time = time.time() 

print("-"*33)
print(f"Total Results fetched {len(result)}")
print("-"*33)

#overview = rebs.overview(result)
#overview =gebs.overview(result)
#overview = rgbs.overview(result)

#print(overview)

elapsed_time = end_time - start_time
print (f"Elapsed time: {elapsed_time:.6f} seconds") 



