import numpy as np

cpu = np.array([
    15,35,82,91,55,78,88,95
])

print(np.mean(cpu[cpu > 80]))

print(np.max(cpu[cpu < 80]))

status = np.where( cpu >= 90, "CRITICAL",
            np.where((cpu >= 80) & (cpu < 90) ,
                "WARNING" , "OK"))
print(status)
