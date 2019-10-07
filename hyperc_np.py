import math, time, random
import numpy as np
ntrials=10000000
dist=0
start_time=time.process_time()
x1=np.random.random()
y1=np.random.random()
x2=np.random.random()
y2=np.random.random()
dist=np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2)
e_time=time.process_time()-start_time
ex_dist=1/15*(math.sqrt(2)+2+5*math.log(1+math.sqrt(2)))
print("Ntrials=%d Ave dist=%9.7f Exact dist=%9.7f time=%6.2f"%(ntrails,dist,ex_dist,e_time))