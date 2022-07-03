from glob import glob

list_file = glob("G://2_smoke//1_house//images//*")
textfile = open("list.txt", "w")

for file_path in list_file:
    name_file = file_path.split('\\')[-1].split('.png')[0]
    name_out = name_file + ' 1 1 1'
    print(name_out)
    textfile.write(name_out + "\n")
    
textfile.close()
    