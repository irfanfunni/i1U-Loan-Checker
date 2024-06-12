import numpy as np



parameter_dict = dict(delimiter=",",
                      dtype=[('name', 'U'),('total_enrolment','U'),('category','U')],
                      names=True)
raw_data = np.genfromtxt('diversity_school.csv', **parameter_dict)
filtered_data = np.array([(row['name'],row['category']) for row in raw_data if row[0] != -1 and row[1] != -1])



print(filtered_data)