# CRM_App
CRM  Customer relationship Management application which help users to management customer
processes. the development method is expained step by step below, this application is build using Python framework Django as Backend and Vuejs Frontend.

* Feautures includes
-Leads
-Clients
-Teams 
-Admin 

* Teams can subscribe to different plan FREE, Small, Big plan base on the plan 
selected they can get Leads, Clients Free with min of 5Leads/5Clients
Small Plan 15Leads/15Client Big Plan 50Leads/50Clients




Step1
Done -Install Vue and some Libraries
 Done -npm install -g @vue/cli
 Done -vue create frontend
 Done -npm install bulma  
 Done -npm install bulma-toast
 Done -npm install axios

Done -Setup the Libraries
   -config axio in src\main.js

 
Done -Create a component for the menu
Done -Create a simple page for Sign up
Done -Create a simple page for Login
Done -Create a simplage page for User Account
Done -Configure the Vueex Store
Done -Setup up router gards

Step 2
Done -Install virtual environment, create and activate
   -pip install virtual env
   -py -3 -m venv name_of_project
   -activate on windows cd venv_3_11 cd Script type activate then enter
Done - Install Django
   -pip install django
Done -Install django-rest-framework
   -pip install django-rest-framework
Done Install django-cors-headers
   -pip install django-cors-headers
Done -Install djoser
   -pip install djoser
Done - Create Django project
    -django-admin startproject backend
Done -Configure the project
  -go to settings/installed_app add the below
       - 'rest_framework',
       - 'rest_framework.authtoken',
       - 'corsheaders',
       - 'djoser'
  - CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080'
   ] --- this is the url to the frontend view
  - MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware'
   ]
Done - Add Djoser to the urls
  - on the urls add
  - 1 from django.urls import path, include
  -  2  urlpatterns = [ 
    path('api/v1/', include('djoser.urls')),
    path('api/v1', include('djoser.urls.authtoken')),
    ]
-Done Initialize database
   - python manage.py makemigrations
   - python manage,py migrate ----to initialize the database
   - python manage.py createsuperuser
     
-Done Create superuser
     - detials
     - username: admin
     - email: atonujekemena@gmail.com
     - password: Hacking001@123
Done Run the development server
    * python manage.py runserver
-Done Make it possible to sign up from the frontend
-Done Make it possible to log in from the frontend
-Done Make it possible to log out from the frontend 

Step 3
-Done   implement a loading bar
-Done Create a Django app for the leads
      * python manage.py startapp lead
      * setup the app
      * settings INSTALLED_APPS = [
         'lead.apps.LeadConfig'
      ]
       
-Done Database model for leads
   * after creating the models
   * run python manage.py makemigrations
   * run python manage.py migrate

-Done Serializer for the leads
 * serializer help take data from the backend to display on the frontend
 * on the lead folder create a new file called serializers.py

-Done View for the leads
-Done Set up the urls
-Done Create page for showing the leads
-Done Make it possible to add leads

Step 4
-Done Add leads Link in the menu
-Done Hide Sign up/Login buttons when Authenticated
-Done Make it posible to view a lead
-Done Make it possible to edit a lead
-Done Show toast when saving leads
-Done Show toast when adding leads

Step 5
-Done Create Django app and model
   * create team app
   * use: python manage.py startapp team
-Done Serializer and View
-Done Store your user info in Vuex
-Done Add team-id and name to Vuex
-Done if you don't have team, send a create team page
-Done Create page for adding teams
-Done Fix login to implement teams (Vuex)

Step 6
Done -update the lead model
-Make it possible to add members
   Done -Update the views.py in the team app
   Done -Update the serializer.py
   Done -New page for team
   Done -Make it possible to add members

   Step 7
   Done -Only owner can add members
   -Assign leads to a member
     Done -Update lead model
     Done -Update lead serializer
     Done  -Override update function
     Done  -Change the edit lead page
  Done -Show assignee in leads list
  Done  Show assignee on lead detail page

   Step 8
   Done -show list of Clients
   Done -page for Clients
   Done -Make it possible add Clients
      Done -Django app and modle
      Done -Serializer
      Done -view
      Done -urls
      Done -vue page for creating clients
      Done -send information to server
   Done-Show list of clients
     Done -Get clients from server
   Done -Detail view of a client
   Done  -Page for clients
   Done   -Get client from server
   Done -Edit cleint
   Done   -Page for editing
   Done   -Get client from server
   Done   -Send updates to server

   Step 9
   Done -Add notes to a client
     Done -Database model
     Done -Serializer
     Done -Views
     Done -Page for adding notes
     Done -Send information to server
     Done -show notes on the details page of a client
     Done -Edit note
        Done -page for editing notes
        Done -send update to server
     Done -Change information about users
       Done -Endpoint for getting information
       Done -Add Edit page for users

      
      Step 10
      Done-Show full name in the CRM
      Done-leads page
      Done -Lead page
      Done  -Member page
      Done-Converting a lead to a client
       Done  -Create view
       Done  -Add button for converting lead
      Done-Create model for plans for the teams
        Done -Add plans in the admin area
        Done -Default plan is free

Step 11
Done -Add Pagination to leads page
Done -Add pagination to clients page
Done -Search (leads)
Done -Search (clients)

Step 12
Done -Start implementing plans limitations
Done -Make it possible to subscribe to a plan

Step 13
Done -install Stripe
    pip install stripe
Done-Start implementing stripe
   Done -Create Stripe account
   Done -GET API Keys
      Done -insert into settings.py
Done -Make public key available in the plans page
Done -Initialize stripe(in the frontend)


Step 14
Done -Add new fields to database
Done -Download and install Stripe CLI
   -https://stripe.com/docs/webhooks/test
Done-Finish Stripe implementation

Step 15
-Make it possible to cancel a plan
-Show plan end date in team page
-Make it possible to delete a lead
-Make it possible to delete a client
-only show leads, clients, and team in menu when authenticated 



