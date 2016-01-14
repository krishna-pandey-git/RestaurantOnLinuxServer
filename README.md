# Linux Server Configuration

Original code for the website has been used from the below github repositoris which
has previously been submitted for the assessment by me. Refer to its README.md for
more detail.
https://github.com/krishna-pandey-git/Restaurant2
and then finalproject.py file has been renamed as __init__.py .

Place the FlaskApp folder in /var/www folder.
now we should have the folder structure like this.
/var/www/FlaskApp/FlaskApp/....

one extra file that present here is lotsofmenus.py.
Run this file with below command, But only after proper configuration of postgresql.
python lotsofmenus.py

# IP Address and SSH Port
52.27.12.106 -p 2200

# Complete URL
http://52.27.12.106

# Configuration Step:
	- Softwares installed
	  1. apache2
	  2. postgres
	  3. flask
	  4. oatuh
	  5. httplib2
	  6. libapache2-mod-wsgi
	  7. python-sqlalchemy
	  
	- Users created
	  1. grader user has been created and sudoer access has been given for ubuntu login
	  2. password login has been disable (actually it was already disabled)
	  3. catalog user has been created in postgres with password as catalog

# Host configuration
	1. Place the File FlaskApp.conf in /etc/apache2/sites-available/
	2. run command sudo a2ensite FlaskApp.conf 
		  
# Third party resources and help
	  1. configuration file FlaskApp.conf has been created with the help of below url
	     https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
	  2. postgres has been configured with the help of below url.
	     https://help.ubuntu.com/community/PostgreSQL

