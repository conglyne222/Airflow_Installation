# AIRFLOW INSTALLATION AND FIRST SIMPLE DAGS

## 1. INSTALLATION

### Install Virtual Environment (Conda)

   1. Create a new virtual environment (Anaconda):
   
      Open in Ubuntu terminal and use this command line:
   
   ```
   conda create --name airflow_env python=3.9 -y 
   ```
   2. To activate the new virtual environment created, use cmd:
   ```
   conda activate airflow_env
   ```
   
### Install Apache Airflow
   ```
   pip install "apache-airflow==2.2.3" --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.2.3/constraints-no-providers-3.9.txt
   ```
### Setup Airflow databases and user
   1. Create an airflow folder in root directory

   ```
   airflow db init
   ```
   After then, navigate to the directory
   
   ```
   cd ~/airflow
   ```
   Use ```ls``` to see list of items in this dir
   
   2. Create Airflow User:
   To create an airflow user, type in cmd:
   ```
   airflow users create \
   ```
   then, create username and password
   ```
   > --username YOUR_USERNAME \ # Type in your username (for example: ```--username lync \```)
   > --password YOUR_PASSWORD \ # Type in your password
   > --firstname YOUR_FIRSTNAME \ # Type in your firstname
   > --lastname YOUR_LASTNAME \ # Type in your lastname
   > --role Admin \ #Set your role as admin
   > --email YOUR_EMAIL_ACCOUNT # Type in your gmail
   ```
   then press Enter, you'll see a line that is  ```User "lync" created with role "Admin"```
   
### Start Airflow webserver and scheduler
   Apache Airflow consists of 2 core parts which are:
   * Webserver
   * Scheduler
   
   There is needed for running both of them to render & inspect DAGs
   1. Webserver
   ```
   airflow webserver -D
   ```
   You can see it's running on port 8080 (by DEFAULT) 
   
   2. Scheduler
   Similar command for running Scheduler
   ```
   airflow scheduler -D
   ```
   Now let's open it in a web browser ```localhost: 8080```
   
   Use user credentials that you've created before to sign in
   
   ![login](https://user-images.githubusercontent.com/63545630/177294200-f93791d6-5fe6-4619-a8af-f121ca02c55b.png)
   
## 2. CREATE FIRST SIMPLE DAGS

   Now when you've finished all installation for using Airflow, you will see the folder named 'airflow' in your pc
   
   Open airflow folder, then create a new folder named 'dags' for containing DAGs scripts:
    
![dag](https://user-images.githubusercontent.com/63545630/177286877-96c9f39a-44aa-49f0-9fc4-ab6aab539bc5.png)

   After that, open Visual Studio Code, create a new .py file inside of dags folder

For instance, ```first_dag.py```

Create first dag with 2 task: ```task_get_datetime``` for taking current datetime and ```task_process_datetime``` for taking detail info from current datetime (month, year, day, weekday) as the scripts uploaded

![1st_dag](https://user-images.githubusercontent.com/63545630/177289252-c2be0876-b2a5-4386-a3fc-92a68406d36c.png)

with chain ```task_get_datetime >> task_process_datetime``` (Execute get datetime then process datetime)

Open cmd, cd into dags folder and run command below:
```
airflow tasks test first_airflow_dag get_datetime 2022-2-1
```

```get_datetime```: task id
```2022-2-1```: date that you want to get

As result below, now we get the current datetime:

![get_date](https://user-images.githubusercontent.com/63545630/177291682-bebd6fd3-e8fd-4aec-b373-9f992d943ca5.png)

Similar commandline for ```task_process_datetime``` but replace the task_id as ```process_datetime```, you'll see the result as below

![process_date](https://user-images.githubusercontent.com/63545630/177292111-8158946f-9ff6-4e57-aeeb-512e9066a77c.png)

Now we got a dictionary with attributes ```day, month, year, weekday``` as we specified in the script

Next stuff, let's see the interface of Airflow in your browser

![airflow1](https://user-images.githubusercontent.com/63545630/177292563-bffd55a0-de4b-42f4-a75a-a7620a9876de.png)
You can see the DAG you created

![airflow2](https://user-images.githubusercontent.com/63545630/177292614-e0d3aefa-0f12-41c0-982a-33ff1897b66b.png)
And the chain of DAG that you made

## Operation System
Ubuntu 20.04

## Language
Python 3.9














   
   

   
