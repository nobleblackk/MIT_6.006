#!/usr/bin/python36

print("content-type: text/html")
print("")

################################################################################################################
				###input 	
r1=int(input("input no of rows for  matrix"))
c1=int(input("input no of columns for  matrix"))

################################################################################################################

				###list initilisation
matrix1=[[0 for i in range(c1) ] for j in range(r1) ]
 
################################################################################################################

				###matrix input
print('\t\t',"matrix1 input")
for i in range(r1):
	for j in range(c1):
		matrix1[i][j]=int(input("input values for matrix1"))

################################################################################################################ 
				###matrix output

print('\t','\t',"MATRIX1")
for i in range(r1):
	for j in range(c1):
		print(matrix1[i][j],'\t',end='')
	print("")

################################################################################################################

				###matrix determinant
def getDeterminant(matrix1):
	determinant=0
	if len(matrix1)==2:
		return (matrix1[0][0]*matrix1[1][1])-(matrix1[0][1]*matrix1[1][0])
	for r in range(len(matrix1)):
		p=0;q=r
		temp=[[0 for k in range ((len(matrix1)-1))] for l in range((len(matrix1)-1))]
		i2=0;j2=0
		for i in range(len(matrix1)):
			for j in range(len(matrix1)):
				if(i!=p and j!=q):
					temp[i2][j2]=matrix1[i][j]
					j2=j2+1
			if(j2==((len(matrix1)-1))):	
				i2=i2+1
				j2=0
		determinant+=((-1)**(r))*(matrix1[0][r])*getDeterminant(temp)
	return determinant					
	
################################################################################################################

				###matrix cofactor
def getCofactor(matrix1):
	matrix2=[[0 for i in range(len(matrix1))] for j in range(len(matrix1))]
	if len(matrix1)==2:
		matrix2[0][0]=matrix1[1][1]
		matrix2[0][1],matrix2[1][0]=-matrix1[1][0],-matrix1[0][1]
		return matrix2

	for r in range(len(matrix1)):
		for c in range(len(matrix1)):
			p1=r;q1=c
			temp=[[0 for k in range ((len(matrix1)-1))] for l in range((len(matrix1)-1))]
			i2=0;j2=0
			for i in range(len(matrix1)):
				for j in range(len(matrix1)):
					if(i!=p1 and j!=q1):
						temp[i2][j2]=matrix1[i][j]
						j2=j2+1
				if(j2==((len(matrix1)-1))):	
					i2=i2+1
					j2=0	
			matrix2[r][c]=(-1)**(r+c)*getDeterminant(temp)
	return matrix2							

################################################################################################################

				###cofactor-matrix transpose
def getAdjoint(matrix1):
	matrix3=[[0 for i in range(len(matrix1))] for j in range(len(matrix1))]
	for i in range(len(matrix1)):
		for j in range(len(matrix1)):
			matrix3[i][j]=matrix1[j][i]
	return matrix3

################################################################################################################

				###matrix inverse
det=getDeterminant(matrix1)
cofactor=getCofactor(matrix1)
adjoint=getAdjoint(cofactor)

matrix4=[[0 for i in range(len(matrix1))] for j in range(len(matrix1))]
for i in range(len(matrix1)):
	for j in range(len(matrix1)):
		matrix4[i][j]=(adjoint[i][j]/det)
		
################################################################################################################
			
				###inverse matrix output
print("\t\t\tMATRIX-INVERSE ::")
for i in range(len(matrix4)):
	for j in range(len(matrix4)):
		print(matrix4[i][j],'\t\t',end='')
	print("")

################################################################################################################











					










		

