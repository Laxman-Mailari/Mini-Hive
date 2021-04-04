This projest is related to the creating SQL Engine for quering the data from dataware house.(mimic hive)

POINTS:
1.Basically if we consider normal database.data is stored on single machine every time when query executed.the query is porcessed on the dataset and result will be displayed.
2.if we consider bigdata system.the size of the data is huge i.e in petabytes and zetabytes.so that data can't be stored on single system.the data needs to be stored on multiple node.


	In this project we dealing with the BigData so we are using hadoop to store the data.Hadoop is is basically stores the data in distrubuted file system so it is called HDFS(Hadoop Distrubuted File System).
	
	so when we store the data in HDFS.it is indirectly stores the data in diffrent nodes.to avoid data loss it create the replica of the data and keep it another node.
	
	To access the data from all the nodes we run MapReduce job to fetch the data from all node.the advantage is Map Reduce run parallel so that the time taken is very less
	
	
	
Project details(MIMIC HIVE):

required tools:
java 1.8 and above version
Hadoop present runing version

you can install hive for reference


step-1:
 switch to hduser if your installed in hduser
 	$ sudo su - hduser
 	
 run the dfs
 	$ start-dfs.sh
 	
 run the yarn
 	$ start-yarn.sh
 	
 check in the browser.you suppose to get namenode(something green).port number may be changed.check online do trial and error method
 	localhost://50070	
 	
 step-2:
 	create the folder in hdfs
 		$ hdfs dfs -mkdir /folder_name

	verify
		$ hdfs dfs -ls /	
		
		
	some more commands:
	
		$hdfs dfs -rm -r (path of the folder or file)	//it removes the fiel from hdfs
		$hdfs dfs -put home/desktop/file.txt /folder/file	//1st part related to the local and 2nd is hdfs folders
		$hdfs dfs -put -f (local file path) (hdfs file path) // it update the exist data in te hdfs
		
setp-3:
	you need to create the txt file in desktop.so that when ever you do query.the data is loaded to that txt file.
	
	keep you csv file also in the desktop and remove the 1st row of the csv file which basically contain the column names.
	
step-4:
	run the code 
	
	load the data to the hdfs by mentioning the created folder
	>>LOAD /you_folder/name.csv AS (mention all the column names alike i mentioned in the query file)
	
	do all the queries which are mentioned in the query file
	
	......:)
