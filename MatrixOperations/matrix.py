#!/usr/bin/python36

print("content-type: text/html")
print("")
				###input 	
m1=int(input("input no of rows for first matrix"))
n1=int(input("input no of columns for first matrix"))

m2=int(input("input no of rows for second matrix"))
n2=int(input("input no of columns for second matrix"))
	
###############################################################################################################

				###list initialization for matrix input
matrix1=[[0 for i in range(n1)] for j in range(m1)] 

matrix2=[[0 for i in range(n2)] for j in range(m2)] 
 
################################################################################################################

				###input for matrices
print('\t\t',"matrix1 input")
for i in range(m1):
	for j in range(n1):
		matrix1[i][j]=int(input("input values for matrix1"))


print('\t\t',"matrix2 input")
for i in range(m2):
	for j in range(n2):
		matrix2[i][j]=int(input("input values for matrix2"))


################################################################################################################ 
				###matrices output

print('\t','\t',"MATRIX:1")
for i in range(m1):
	for j in range(n1):
		print(matrix1[i][j],'\t',end='')
	print("")

print('\t','\t',"MATRIX:2")
for i in range(m2):
	for j in range(n2):
		print(matrix2[i][j],'\t',end='')
	print("")



################################################################################################################

				###matrix multiplication
if n1==m2:
	matrix3= [[0 for i in range(n2)]for j in range(m1)]
	for i in range(m1):
		for j in range(n2):
			sum=0
			for k in range(n1):	###n1==m2
				sum+=matrix1[i][k]*matrix2[k][j]
			matrix3[i][j]=sum

else:
	print("matrix multiplication can not be done")	



################################################################################################################

				###matrix multiplication output
print('\t\t',"MATRIX:3")
for i in range(m1):
	for j in range(n2):
		print(matrix3[i][j],'\t',end='')
	print("")

################################################################################################################

				###matrices transpose
print('\t\tMATRIX:1 TRANSPOSE')
matrix4=[[0 for i in range(m1)]for j in range(n1)]
for i in range(n1):
	for j in range(m1):
		matrix4[i][j]=matrix1[j][i]
		print(matrix4[i][j],'\t',end='')
	print("")	


print('\t\tMATRIX:2 TRANSPOSE')
matrix5=[[0 for i in range(m2)]for j in range(n2)]
for i in range(n2):
	for j in range(m2):
		matrix5[i][j]=matrix2[j][i]
		print(matrix5[i][j],'\t',end='')
	print("")	

################################################################################################################


























