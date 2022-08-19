Honestly this was somewhat amusing and extremely confusing at first, unfortunately i came up with a fever on the second day and was totally unproductive!(no excuses intended), there after my workflow web server stopped working after the first trial. I was definitely initially lost in ambiguity. However i think i was able to patch something out.
Here is the link to my repo 

Basically I’m creating a workflow engine that welcomes a user and sends an email within a specified time (1-5am) in the morning.

# To get started 

Install a workflow framework 
The Workflow engine framework i used for this test was apache airflow
I followed through with the documentation and immediately got started creating automated workflows.

To install i used PyPi package 
- pip install apache-airflow (there’s a more detailed setup)
- Switch from main branch to master
- Check airflow documentation in order to setup instance on your computer
- Start airflow web server 
- Login with provided username and password
- Access DAGS

# Architecture
- Write a workflow as a Directed acyclic graph(DAG) using Python 
- A node in the DAG represents a task 
- Conditional node returns a boolean 
- Schedule nodes to run at specific time.
- Create a task that welcomes new user 
- Create task for sending mail (send_mail)
- Create sensor that send email at a specific time(1.00-5.00)
- If tasks for sendmail at specific time is false do not send mail else send an email.

# Process
- Write a base executor class with python
- Write a base sensor class with python for checking time
- Write a trigger rule class for sending triggers based on conditional nodes

I ran into lots of issues regarding setting up a webserver locally with airflow, this may be due to depreciated dependencies or improper installation.
As a result i am still trying to actively fix it, however i am submitting my test based on a working implementation.
I hope you can run this program without any hiccups, cheers.
