# portfolio-website
**0.3.2**

This website was built with the intention of showcasing some of my web development
skills and providing a "substitute" for my resume.

Technologies used:
* Backend: Python (libraries: flask, flask_mail, wtforms) 
* Frontend: TailwindCSS, Tailblocks, jQuery

To run this project you need Python 3.9 installed. Also, please check the 
requirements.txt to install the necessary Python libraries.

If you're looking to deploy your own website based on this project, you need
to change a couple of things. My website is deployed to PythonAnywhere, where
the following steps will help you with the process:
* create a Python 3.9 virtual environment on the hosting service that you wish 
and install libraries to satisfy the requirements
* import the files from the project (or clone from git repo)
* set up the source code location, your virtual environment location 
and the WSGI config file (the WSGI config can contain sensitive info that you
stored locally previously)
* if you store sensitive info in WSGI: you need to modify your app's configuration
as configparser is not needed anymore, the environmental variables can be reached
with ```os.getenv("INFO")``` code.
* upload your media files and modify the file paths
* set your app to run as it would in a production environment ```app.run(debug=False)```