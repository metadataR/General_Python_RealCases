# This code is to replace existing names with thier second names fromt he text file in the input folder

#e.g. Input file
#<<
#"My name is Satya"
#I like python and spark
#>>
#my metadata file has conversion rule  for replacement :    

#   keyword      to be replaced keyword

#  Satya                       satyawan_kadalag

#  ABC                         XYZ

# DEF                           BADKW

#spark                          scala 

#On basis of my metadata file meta.txt, this program should generate new file as below
#<<
#"my name is satyawan_kadalag"
#I like python and scala
#>>
 
 
 ##### First Way ########
# create a yaml file ( exmaple : meta.yaml): 
#content of meta.yaml looks like
#Satya: satyawan_kadalag
#ABC: XYZ
#DEF: BADKW
#spark: scala

#python code to replace the values: 
import yaml

with open('meta.yaml', 'r+') as yaml_file:
    metadata = yaml.safe_load(yaml_file)
#print(metadata)

with open('my_text_input.txt') as input_file:
    output_file = open('output.txt', 'w+')
    input_data = input_file.read()
    for k,v in metadata.items():
        input_data = input_data.replace(k,v)
    output_file.write(input_data)
    output_file.close()
    
    
######### Second Way #######
keyword=[]

replace_with=[] 

with open('metadata filepath','r') as openfile:

    for line in openfile:

        keyword.append(line.split()[0])

        replace_with.append(line.split()[1])

    keyword = keyword[1:]

    replace_with = replace_with[1:]

openfile.close()

 

with open('input','r') as readwritefile:

    data = readwritefile.read()

readwritefile.close()

for key,repl in zip(keyword,replace_with):

    data=data.replace(key,repl)

 

with open('input','w') as readwritefile:

    readwritefile.write(data)
