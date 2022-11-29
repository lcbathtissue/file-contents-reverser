input_file = "test1"
output_file = "test2"

f = open(input_file, "r")
read_data = f.read().split("\n")
max_index = len(read_data) - 1
read_data = reversed(read_data)

f = open(output_file, "w")
f.write("")
f.close()

f = open(output_file, "w")
for i, line in enumerate(read_data):
    if i != max_index:
        f.write(f"{line}\n")
    else:
        f.write(f"{line}")
f.close()