import matplotlib.pyplot as plt
import sys

input_array = plt.imread(sys.argv[1])
x, y, _ = input_array.shape

histogram = [0]*256

for row in input_array:
	for p in row:
		histogram[p[0]] += 1

pdf = [i/(x*y) for i in histogram]

cdf = [pdf[0]]
for i in range(1,256):
	cdf.append(pdf[i]+cdf[i-1])

nth = [int(i*255) for i in cdf]

output_array = list()
for row in input_array:
	temp = list()
	for p in row: 		
		p_new = nth[p[0]]	
		temp.append([p_new]*3)
	output_array.append(temp)

print("Histogram Equilization is done.")
plt.imsave("result.png",arr=output_array)
plt.imshow(output_array)
plt.show()
