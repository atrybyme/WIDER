import numpy as np 

final_data=[]

file = open('wider_face_train_bbx_gt.txt','r')

file_name=[]

num_of_persons_per_file=[]

cnt=0

ARR=[]

for line in file:
	temp_list=[]
	temp_list.append(line[:-1])
	file_name.append(line[:-1])
	#print(file_name)
	num_of_persons=next(file)
	num_of_persons_per_file.append(int(num_of_persons))
	temp_list.append(int(num_of_persons))
	#print(num_of_persons_per_file)
	
	arr=[]
	for i in range(int(num_of_persons)):
		
		coord=next(file)
		xx=map(int, coord.split())
		xx=xx[:4]
		arr.append(xx)

		if i==(int(num_of_persons)-1):
			#print(arr)
			arri=np.array(arr)
			ARR.append(arri)
	# if(cnt==3):
	# 	break
	# cnt=cnt+1
	temp_list.append(np.array(arr))
	final_data.append(temp_list)
ARRI=np.array(ARR)

dicti={}
dicti['file_names']=file_name
dicti['n_of_persons_per_file']=num_of_persons_per_file
dicti['coordinates']=ARRI
print(file_name[110])
# print(ARRI[3])
# print(num_of_persons_per_file[3])
print(final_data[2][2][0][0])

