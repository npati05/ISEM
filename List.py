#creating a list
college = ["BC Roy", "BSTM", "Saradamoni", "JIS"]
print(college[0])
print(college[2])
print(college[-1])
new_dict = {i:college[i] for i in range(len(college))}
print(new_dict)

UNIVERSITY = ["BURDWAN", "KOLKATA", "WBUT"]
new_dict = {i:college[i] for i in range(len(college))} ## new added
print(new_dict)
