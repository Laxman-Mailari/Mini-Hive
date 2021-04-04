import re
import sys
import subprocess
import time
import random

class load:
    args=[]
    def __init__(self):
        pass
    def load_data(args):
        schema=args[3].strip("()")
        schema=schema.replace(":"," ")
        #schema=schema.replace(",",";")
        schema=schema + "\n"

        file_name=args[1].split("/")[-1]
        with open("/home/hduser/Desktop/"+file_name, "r+") as f:
            a = f.read()
            with open("/home/hduser/Desktop/"+file_name, "w+") as f:
                f.write( schema + a)
                f.close()
        schema_file="/home/hduser/Desktop/" + file_name
        db_path=args[1].split("/")
        db_path=db_path[:-1]
        db_path="/".join(db_path)
        #print("schema:",schema_file)
        #print("db_path:",db_path)
        subprocess.run(['hdfs','dfs','-put',''+schema_file,''+db_path])
        print("--------Data Loaded successfully-----------")


class select:
	args=[]
	
	def match(value):
		pass
				
	def mapper(args):
		count=False
		table=args[3]
		log=open('/home/hduser/Desktop/hd_file.txt','w+')
		subprocess.Popen(['hdfs','dfs','-cat',''+table],stdout=log)
		log.close()
		time.sleep(random.randint(2,6))
		
		agg_col=args[1]
		if re.match("MIN",agg_col):
			agg_col=agg_col.strip("MIN()")
		elif re.match("MAX",agg_col):
			agg_col=agg_col.strip("MAX()")
		elif re.match("COUNT",agg_col):
			agg_col=agg_col.strip("COUNT()")
			count = True
		
		con_col = None
		table=args[3]
		with open('/home/hduser/Desktop/hd_file.txt',"r+") as fd:
			line=fd.readline()
			if "WHERE" in args:
				con_col = args[5]
				value = args[7]
			line_arr=line.split(",")
			col_ind=0
			con_ind=0
			for i in range(len(line_arr)):
				col_name_arr=line_arr[i].split(" ")
				if col_name_arr[0] == con_col:
					con_ind=i
				if col_name_arr[0] == agg_col:
					col_ind=i
			flag=0
			while True:
				line=fd.readline()
				if not line:
					break
				line_arr=line.split(",")
				
				if con_col != None :
					'''if re.search('[a-zA-Z]',value):
						line_arr[col_ind]=str(line_arr[col_ind])'''
					#print(type(line_arr[con_ind]))
					
					if line_arr[con_ind] == value and re.match("=",args[6]):
						if count == True:
							yield(line_arr[col_ind],1)
						else:
							yield(line_arr[col_ind])
						flag=1
					elif line_arr[con_ind] >= value and re.match(">=",args[6]):
						if count == True:
							yield(line_arr[col_ind],1)
						else:
							yield(line_arr[col_ind])
						flag=1
					elif line_arr[con_ind] <= value and re.match("<=",args[6]):
						if count == True:
							yield(line_arr[col_ind],1)
						else:
							yield(line_arr[col_ind])
						flag=1
					
				else:
					if count == True:
						yield(line_arr[col_ind],1)
					else:
						yield(line_arr[col_ind])
			if con_col != None and flag==0:
				print("---None of them is matched-----")


	def reducer(obj,var):
		if var == 'MIN':
			mn=1000
			for i in obj:
				if float(i) < mn:
					mn=float(i)
			print("minimum:",mn)
		elif var == 'MAX':
			mx=0
			for i in obj:
				if float(i) > mx:
					mx=float(i)
			print("maximum:",mx)
		elif var == 'COUNT':
			count=0
			for i,c in obj:
				count += c
			print("count:",count)

	def select_cols(args):
		
		y=select.mapper(args)
		for i in y:
			print(i)
			
		
	def aggregate(args):
		if re.match("MIN",args[1]): var='MIN'
		elif re.match("MAX",args[1]): var='MAX'
		elif re.match("COUNT",args[1]): var ='COUNT'
		y=select.mapper(args)
		select.reducer(y,var)

			
class delete:
	args=[]
	def delete_col(args):
		y=select.mapper(args)
		
		

if __name__ == "__main__":
    print("\n\n************** MINI HIVE ***************\n\n")
    #print("we have a database called CARS\n\n")
    while True:
        input_array=[]
        input_data=str(input("Mini-hive >> "))
        input_data=input_data.strip()
        if(input_data == 'exit'):
            exit()
        input_array=re.split(" ",input_data)
        if input_array[0] == 'SELECT' or input_array[0] == 'select':
        	if re.match("MIN",input_array[1]) or re.match("COUNT",input_array[1]) or re.match("MAX",input_array[1]):
        		select.aggregate(input_array)
        	else: 
           		select.select_cols(input_array)
        elif input_array[0] == 'LOAD' or input_array[0] == 'load':
            print("loading...")
            load.load_data(input_array)
        elif input_array[0] == 'DELETE' or input_array[0] == 'delete':
        	print("deleting...")
        	
        print(" ")
