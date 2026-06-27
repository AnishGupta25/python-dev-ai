import numpy as np 
cpu = np.array([ 15,35,82,91,55,78,88,95 ]) 

cpu_80 = cpu[cpu > 80] 
print(cpu_80) 

cpu_50_90 = cpu[(cpu > 50) & (cpu < 90)] 
print(cpu_50_90) 

cpu_idx_90 = np.where(cpu > 90) 
print(cpu_idx_90) 

cpu[cpu > 90] = 90 
print(cpu) 

status = np.where( cpu > 80, "ALERT", "OK" ) 
print(status)
