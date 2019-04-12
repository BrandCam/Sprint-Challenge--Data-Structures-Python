import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# duplicates = list(set(names_1).intersection(names_2))


 
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

names_dict = {}

for name in names_1:
    names_dict[name] = name

for name in names_2:     
    if name in names_dict:   
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

