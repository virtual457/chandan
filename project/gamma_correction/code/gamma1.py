import matplotlib.pyplot as plt
import sys

def gamma_correction(r,gamma,c = 1):
	return int(c*(r**gamma))

input_array = plt.imread(sys.argv[1])

output_array = list()
for row in input_array:
	temp = list()
	for p in row:
		temp.append([gamma_correction(p[0],gamma=float(sys.argv[2]))]*3)
	output_array.append(temp)

print("Gamma Correction over")

plt.imsave("result.png",arr=output_array)
plt.imshow(output_array)
plt.show()

