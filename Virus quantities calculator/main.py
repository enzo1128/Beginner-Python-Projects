
first = int(input("How many plaques in the first well?\t"))
second = int(input("How many plaques in the second well?\t"))
dilution = int(input("What is the dilution for these wells?\t"))

mean = (first+second)/2

titer = "{:e}".format((mean/0.250)*(10**dilution))

print(f"the titer is {titer}PFU/mL")


