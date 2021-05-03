
### About
Busara_recruit is Django a web application for managing job applications to Busara Centre for Behavioural Economics. 


### Prerequisites
Before running the application, ensure you have installed and configured
the following tools

- Django v1.11.5
- Python v3.6


### Installation
1. Copy the project, busara_recruit, to any directory of your choice.

2. Navigate to the root directory (busara_recuit) containing the manage.py file in a command line.

3. Install dependencies

   ```
   $ pip install -r requirements.txt
   ```
 
4. Run the migrate command in a shell to create the database tables automatically.

   ```
   $ python manage.py migrate
   ```


   
5. Execute the runserver command in a shell to start the development server. This will enable you to access
   the web application in a browser.

   ```
   $ python manage.py runserver
   ```


   
6. Copy the following url in a browser
   
   http://localhost:8000/
   
   NB: The development server runs on port 8000 by default   
   
### Running tests

In a terminal navigate to the root directory of the project containing the manage.py file,
then run the following command in a shell:

  ```
  $ python manage.py test
  ```

Optionally you can specify an app to test
e.g

  ```
  $ python manage.py test jobs
  ```
