Author: Tony Afula Maganga
Project: Busara Recruitment Portal
Email: tonyafula@gmail.com
Role: Senior Software Developer
Date: Aug 28, 2017


### About
Busara_recruit is Django a web application for managing job applications to Busara Centre for Behavioural Economics. 


### Prerequisites
Before running the application, ensure you have installed and configured
the following tools

- Django v1.11.4
- Python v3.4+
- MySQL Server 5.5+

### Installation
1. Copy the project,busara_recruit, to any directory of your choice.

2. Navigate to the root directory (busara_recuit) containing the manage.py file in a command line.

3. Run the following migration commands to prepare the database
   python manage.py makemigrations employers
   python manage.py makemigrations employees
   python manage.py makemigrations jobs
   python manage.py makemigrations candidates
   python manage.py makemigrations interviews
