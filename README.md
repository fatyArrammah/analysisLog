# Logs Analysis Project

   This project is an internal tool built into a news site to analyze users' logs.

## Getting Started

 ### Prerequisites
  This program requires pre-installed database on linux VM. This database includes articles and user log tables.
  ##### Software Installation 
  - Install latest version of [python3](https://www.python.org/downloads/)
  - Install  [Vagrant](https://www.vagrantup.com/downloads.html) 
  - Install latest version of [Virtual Machine](https://www.virtualbox.org/wiki/Downloads)
  - download [FSDN virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)
  -  if your system is running on **windows OS** , you need to use a **_Git bash_** terminal 

### Software Running
- ##### Software and data setup
    
    This program will run on Linux system. After you have installed the previous software, you need to follow these instructions:

    + Boot and login into VM by the following
    
        ```
        vagrant up
        vagrant ssh
        ```
    + Download [this project](https://github.com/fatyArrammah/analysisLog.git) into **/vagrant** directory , then unzip this folder
    + Download [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), then also unzip this folder
    + Save all files (**newsdata.sql** and **logAnalysis.py**) in **/vagrant** directory
    + Load "news" database by running the following using **_Git bash_**
        ```
        psql -d news -f newsdata.sql
        ```
    + Go to **/vagrant** directory using **_Git bash_** terminal by 
        ```
        cd vagrant
        ```
- ##### Software execution

    + This project used PostgreSQL environment. So, if psycopg2 library has not been installed yet, you can run the following by  **_Git bash_**
    
        ```
        pip3 install psycopg2
        ```
    + Run python file by **_Git bash_** terminal
        ```
        python3 logAnalysis.py
        ```

### System Output
The python file **logAnalysis.py** treats the database tabls to answer the following questions:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

These questions are answered by this software which connects to the "news" database and triggers the required **_SQL_** statements. The output will be on the **_Git bash_** terminal as well as on logAnalysisResult.txt. Each **_SQL_** consists of main structure:
```
SELECT column_name FROM table_name Where condition_of_rows_filter 
```
There are other clauses used within **_SQL_** query to catch more informative and accurate results 


## Author
+ Fatima Al-Rammah - all work - **_[fatyArrammah](https://github.com/fatyArrammah)_**



