FROM python:3.7.6

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Bundle app source
COPY . /usr/src/app
RUN rm /usr/src/app/Jenkinsfile
RUN rm /usr/src/app/test.py

EXPOSE 8000
CMD [ "python", "./app.py" ]
