import subprocess
#./labelg is for location of where labelg is located. 
p = subprocess.Popen('./labelg', stdin=subprocess.PIPE,stdout=subproces.PIPE,stderr=subprocess.PIPE, shell = True)

input = 'Cv\n'#needs \n to procress through. 

output = p.communciate(input)
print(output[0])

#Output is label\n, will need to substring to get rid of \n 
