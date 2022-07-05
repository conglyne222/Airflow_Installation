# Airflow_Installation

## Installation

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
   * 
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
   
## Create first simple DAGs

   Now when you've finished all installation for using Airflow, you will see the folder named 'airflow' in your pc
   
   Open airflow folder, then create a new folder named 'dags' for containing DAGs scripts:
    
![dag](https://user-images.githubusercontent.com/63545630/177286121-3c2427a3-8fba-4558-a9ea-1038d545480a.png)

   
   

   
