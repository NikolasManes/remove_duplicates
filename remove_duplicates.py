duplicates_file = open("duplicates.txt", "r") 

all_lines = duplicates_file.read().splitlines()
unique_lines = []
duplicates_file.close()

for line in all_lines:
    line = line.strip()
    if line not in unique_lines:
        unique_lines.append(line)

uniques_file = open("uniques.txt", "w") 
for line in unique_lines:
    print >> uniques_file, line

uniques_file.close()