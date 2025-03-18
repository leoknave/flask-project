# **Flask User Management App - Step-by-Step Guide**

## **📌 Overview**
This project is a **Flask web application** that displays a webpage with simple text and database records.  
Follow these **exact** steps to set up, run, and test the application.  

If **any step is missing** or incorrect, the project **will not be graded**. **Read carefully and follow every instruction.**  

## **🚀 Step 1: Install Dependencies**  
### **Create and Activate Virtual Environment**  
Before starting, open the terminal or command prompt and navigate to the project directory.

#### **For Mac/Linux**:

python3 -m venv venv
source venv/bin/activate
For Windows (CMD):
Copy:
python -m venv venv
venv\Scripts\activate
For Windows (PowerShell):
Copy:
python -m venv venv
venv\Scripts\Activate
Note: If the virtual environment is activated, you should see (venv) at the beginning of the terminal prompt.

Now, install the required dependencies:
Copy:
pip install -r requirements.txt
## **⚙️ Step 2: Set Up the Database
Before running the app, initialize the database.

Set Environment Variables
For Mac/Linux:
Copy:
export FLASK_APP=run.py
export FLASK_ENV=development
For Windows (CMD):
Copy:
set FLASK_APP=run.py
set FLASK_ENV=development
For Windows (PowerShell):
powershell
Copy:
$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"
Run Database Migrations
Now, run these commands in order:
Copy:
flask db upgrade
If you see:
"No changes in schema detected."
It means the database is ready.

🛠 Step 3: Insert Sample Data
To insert sample users into the database, run:
Copy:
python query.py
If successful, you should see:
Copy:
Sample data inserted!
🚀 Step 4: Run the Application
Start the Flask app by running:
Copy:
python run.py
If everything works correctly, the terminal should show:
Running on http://127.0.0.1:5000/
Now, open http://127.0.0.1:5000/ in your web browser.
You should see a list of registered users displayed in a table.

