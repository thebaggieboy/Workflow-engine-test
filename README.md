# Workflow-engine-test

Honestly this was somewhat amusing and extremely confusing at first, unfortunately i came up with a fever on the second day and was totally
 unproductive!(no excuses intended), there after my workflow web server stopped working after the first trial. I was definitely initially lost in ambiguity. However i think i was able to patch something out.
Basically I’m creating a workflow engine that welcomes a user and sends an email within a specified time (1-5am) in the morning.

To get started 

Install a workflow framework 
The Workflow engine framework i used for this test was apache airflow

To install i used PyPi package 
- pip install apache-airflow (there’s a more detailed setup)

Architecture
- Write a workflow as a Directed acyclic graph(DAG) using Python 
- A node in the DAG represents a task 
- Conditional node returns a boolean 
- Schedule nodes to run at specific time.
- Create a task that welcomes new user 
- Create task for sending mail (send_mail)
- Create sensor that send email at a specific time(1.00-5.00)
- If tasks for sendmail at specific time is false do not send mail else send an email.
