# ML-Project-End-to-End
First Machine Learning End to End

```
https://github.com/avnyadav?tab=repositories
```

Creating Conda environment - 
```
conda create -p venv python==3.9 -y 
```
/// -p is for the project folder and -y is the YES answer to the question of Yes or No

Activating the Conda environment - 
```
conda activate venv/ 
```


Deactivating the Conda environment - 
```
 conda deactivate venv/ 
```

///Adding files to Git
'''
git add .                         - this command will add all the files from current directory to the git
git add <file_name>               - this command will add the specific file mentioned in this command to the github
git status                        -  to check the status of the files available in git and in local system
git commit -m 'Version comments'  - this command will create a new version 
git log                           - we will be able to see all the available versions
git push origin main              -  to send version/changes to github. here origin is the variable having URL for the github folder
if any file we dont want to upload to Github then we need to mention the file name in .gitignore file
```

to check remote url
```
git remote -v
```

Now, to setup the CI/CD pipeline in heroku we need 3 information
```
1. HEROKU_EMAIL = arbaz.soyeb.khan@gmail.com
2. HEROKU_API_KEY = 4e50e64a-a1c5-42c8-ad00-d3d195524d85     #should not be publicly shared...in Github use Secrets settings
3. HEROKU_APP_NAME = ml-regression-apptest
```
```
now we need to create Dockerfile which will have all the configurations of our application as a blueprint

We will create the .dockerignore file and include all the relevant files which we dont want to be saved on dockerimage like venv, git, gitignore,etc
```
Then we will include all the files in dockerfile 
 FROM python:3.9                              # to create a virtual environemnt in docker
  COPY . /app                                 # imclude all the files within /app folder
  WORKDIR /app                                # change the directory to /app
  RUN pip install -r requirements.txt         #run the requirements.txt file to get all the libraries
  EXPOSE $PORT                                # give the port from our environment variable 
  CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app   #use gunicorn library and launch our application for thee id address and port maintained

```


Build Docker Image
```
docker build -t <image_name in small letters>:<tagname mostly latest> .
```

To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000
```

TO check running containers in Docker
```
docker ps
```


To stop Docker container
```
docker stop <container_id>
```
gunicorn in Docker file - is a web server application which is used to deploy web applications of multiple language i.e. python, django,etc


To install the setup.py file 
```
python setup.py install or use pip install setup.py
```


In requirements.txt file, we added '-e .' which will check the setup.py file and also install all the packages built in our folder that has __init__.py file in it 