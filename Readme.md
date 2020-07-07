# Python, Flask and Docker

### Guide to build and run docker container

	* Go in to the root directory

	* Build image `docker build -t flask-api:latest .` 
  
	* Run the container in detached mode and run on port 8000 
	
		`docker run -d -p 8000:8000 flask-api:latest`
  
	* API will be accessible on port 8000 if no other service is running in the same port. 
		
	* Try using curl `curl http://127.0.0.1:8000/`
