import numpy as np

hosts = np.array([
    "web1",
    "web2",
    "web3",
    "web4",
    "web5",
    "web6",
    "web7",
    "web8"
])

cpu = np.array([
    15,
    35,
    82,
    91,
    55,
    78,
    88,
    95
])

high_utlization = hosts[cpu > 80]
print(high_utlization)

highest_host = hosts[np.argmax(cpu)]
print(highest_host)

host_above_80 = np.mean(cpu[cpu > 80])
print(host_above_80)

top_3_cpu = cpu[np.argsort(cpu)[-3:]]
print(top_3_cpu)

status = np.where((cpu >= 90),"CRITICAL",
        np.where((cpu >= 80) & (cpu < 90),
        "WARNING",
        "OK"))
print(status)

