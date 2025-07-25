# MY-FINAL-PROJECT

_Automated Manual Payments Portal

##  Overview
MY-FINAL-PROJECT is designed to automate and streamline manual payment processes.my final project: a Django-based payment manager that allows users to add payees, record payments, and track totals – similar to how Chamas manage group contributions. Built using **Python**, this project aims to provide a robust and user-friendly portal for handling payment tasks efficiently.


This is in adherence to UN SDG 8

 SDG 8 – Decent Work and Economic Growth
Why it fits: Promotes sustainable economic growth, productive employment, and financial inclusion. If your system helps people save better or manage group funds, it supports entrepreneurship and long-term planning.

Relevant Targets:

8.3 – Promote development-oriented policies that support productive activities, decent job creation, entrepreneurship, and access to financial services.

8.10 – Strengthen the capacity of financial institutions to encourage and expand access to banking, insurance, and financial services.

##  Main Features
- Automated payment workflows
- User-friendly interface for manual payment handling
- Support for multiple payment methods
- Secure and reliable transaction management
- Currency selection for payments
- Payment confirmation page
- Search and filtering for payments
- User authentication and authorization

- MY-FINAL-PROJECT
├── payments/             # Django app for payment & payee logic
│   ├── migrations/
│   ├── templates/
│   │   └── payments/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── index.html
│   │       ├── payee_form.html
│   │       ├── payment_confirmation.html
│   │       └── payment_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md


Clone the repo:

1.How to Run Locally

git clone https://github.com/Papi1997/MY-FINAL-PROJECT.git
cd MY-FINAL-PROJECT

2.Set up a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies:


pip install django
4. Run migrations:

python manage.py migrate

5.Run the server:
python manage.py runserver
Visit http://127.0.0.1:8000/




## Technologies Used
- **Python** (main programming language)
- [Add any frameworks, libraries, or dependencies here]

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Papi1997/MY-FINAL-PROJECT.git
   ```
2. **Install dependencies:**
   ```bash
   # Example for Python
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   # Adjust this command based on your project
   python main.py
   ```

## Usage
- Access the portal via your local machine or server.
- Follow on-screen instructions to initiate and manage manual payments.

##  Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with a descriptive message.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

##  Contact
Have questions or want to connect? Reach out via (https://github.com/Papi1997).



##To run this website on your local machine, you will need to have Python and Django installed. Here are the steps you can follow:

Download the code: Download the project files to your laptop.
Install Python: If you don't have Python installed, you can download it from the official Python website.
Install Django: Open a terminal or command prompt, navigate to the project's root directory, and run the following command to install Django:
pip install -r requirements.txt
Run database migrations: In the same terminal, run the following commands to set up the database:
python manage.py makemigrations
python manage.py migrate
Create a superuser: To access the admin panel, you'll need a superuser account. Create one by running this command and following the prompts:
python manage.py createsuperuser
Run the development server: Finally, start the development server with this command:
python manage.py runserver
Access the website: Open your web browser and go to
Home page: http://127.0.0.1:8000/

Dashboard: http://127.0.0.1:8000/dashboard/

Admin panel: http://127.0.0.1:8000/admin/

Admin username:Tonny.Onwonga
password:Tonny1997.
