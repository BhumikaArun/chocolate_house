
Chocolate House CLI Application
This Python-based CLI application helps manage a fictional Chocolate House business. It allows the management of seasonal chocolate flavors, inventory of ingredients, and customer suggestions related to flavors and allergies. The app uses an SQLite database for persistent storage and is packaged using Docker.

Features
SeasonalFlavors: Manage seasonal flavors with details like name, description, and availability.
Inventory: Keep track of ingredients, quantities, and units of measurement.
CustomerSuggestions: Store customer flavor suggestions and allergy concerns.
Dockerized Application: The app is containerized using Docker for easy setup and deployment.
Prerequisites
Python 3.10 (or later)
Docker (for containerization)
SQLite (used as the database for persistent storage)
Installation
1. Clone the repository
First, clone the repository to your local machine.

bash
Copy code
git clone https://github.com/yourusername/chocolate-house-cli.git
cd chocolate-house-cli

2. Set Up Python Environment
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
The requirements.txt file will install all the necessary Python packages, including sqlite3, SQLAlchemy for ORM support, and other dependencies.

3. Set Up Database
Run the setup_database() function to initialize the database and create necessary tables. This is done automatically when the application runs.



Running the Application

The application can be run as a CLI (command-line interface). It provides two commands:

Add a New Seasonal Flavor


