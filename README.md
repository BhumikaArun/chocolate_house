Chocolate House CLI Application

**Overview:**
This Python-based CLI application helps manage a fictional Chocolate House business. It allows the management of seasonal chocolate flavors, inventory of ingredients, and customer suggestions related to flavors and allergies. The app uses an SQLite database for storage and is packaged using Docker.

**Features**
SeasonalFlavors: Manage seasonal flavors with details like name, description, and availability.
Inventory: tracking ingredients, quantities, and units of measurement.
CustomerSuggestions: Store customer flavor suggestions and allergy concerns.
Dockerized Application: The app is containerized using Docker.

**Prerequisites**
Python 3.10 .
SQLite 
Docker 

**Installation**
1. Clone the repository
First, clone the repository to your local machine.

2. Set Up Python Environment
Create a virtual environment and install dependencies:
The requirements.txt file will install all the necessary Python packages, including sqlite3, SQLAlchemy for ORM support, and other dependencies.

3. Set Up Database
Run the setup_database() function to initialize the database and create necessary tables. This is done automatically when the application runs.
Below is the ER diagram of Database:
![image](https://github.com/user-attachments/assets/c83baff8-869e-4429-8920-1c91b905647a)

**Running the Application**
The application can be run as a CLI (command-line interface). 
1. Add a New Seasonal Flavor :
![image](https://github.com/user-attachments/assets/83e3ae19-c78f-4599-95e5-b985b358ddf0)
![image](https://github.com/user-attachments/assets/51c6e630-29a8-4721-ae3a-444758d0362b)

2. List of all added flavours : 
![image](https://github.com/user-attachments/assets/3e1459b5-224f-45fe-97c0-1f127f72ee7f)

3. We can also perform other operations such as delete and display the list as well.

4. Dockerization
To run the application within a Docker container, follow these steps:
Build the Docker Image:
![image](https://github.com/user-attachments/assets/94c45f50-060e-422a-a301-08225ce6c1cc)

**Acknowledgements**
This project uses SQLite for lightweight database management.
Thanks to SQLAlchemy for providing ORM capabilities. 




