# Client Query Management System:

# Project Overview:
    The Client Query Management System is a web-based application developed using Python and Streamlit. The main purpose of this system is to provide a simple platform where clients can submit their queries and the support team can manage and respond to those queries efficiently. In many organizations, client requests are often handled through emails or manual records, which can become difficult to track and manage. This project solves that problem by creating a centralized system where all queries are stored and managed in one place.

# Objective of the Project:
    The objective of this project is to build a simple and user-friendly system that helps organizations handle client queries in an organized way. It allows clients to submit their issues or requests through an interface while the support team can view and manage these requests. The system also ensures secure login functionality so that only authorized users can access their respective dashboards.

# Technologies Used:
    This project is developed using Python as the core programming language. The user interface is built using Streamlit, which allows the application to run as an interactive web application. SQLite is used as the database to store user credentials and client queries. Password security is implemented using the Hashlib library which encrypts passwords using the SHA-256 hashing algorithm before storing them in the database.

# System Architecture:
     The system consists of three main components: the login module, the client module, and the support module. The login module handles authentication and user registration. Once logged in, users are directed to different dashboards depending on their role. Clients are able to submit queries through the client module, while the support team can view and manage those queries through the support module. All data is stored in the SQLite database and accessed through the database configuration file.

# Project Structure:
     The project contains several Python files that manage different parts of the application. The Login.py file handles user login and registration. The db_config.py file manages the connection between the application and the SQLite database. The init_db.py file initializes the database and creates the required tables. Inside the pages folder, the 1_Client.py file provides the client interface for submitting queries and the 2_Support.py file provides the support dashboard for viewing and managing those queries.

# Features of the System:
     The system provides a secure login and registration system for users. Clients can submit queries through a simple interface and store them in the database. The support team can access the submitted queries and manage them from their dashboard. Passwords are securely stored using hashing, which improves the security of user credentials. The application also provides a clean and interactive interface using Streamlit.

# Database Design:
     The application uses SQLite as its database system. The database stores information such as user details, login credentials, and client queries. The database tables are created automatically when the init_db.py script is executed. This ensures that the application has all required tables before running.

# How to Run the Project:
# Step 1: 

First, clone the project repository from GitHub to your local machine.

git clone https://github.com/your-username/client-query-management-system.git

# Step 2: Navigate to the Project Folder:

Move into the project directory using the command below.

cd client-query-management-system

# Step 3: Install Required Libraries

Install the required Python library using pip.

pip install streamlit

# Step 4: Initialize the Database:

Run the database initialization file to create the required tables.

python init_db.py

# Step 5: Run the Application:

Start the Streamlit application using the following command.

streamlit run Login.py

After running the command, the application will open automatically in your browser where users can register and log in to the system.

