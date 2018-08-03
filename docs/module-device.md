# device module

This module is used to handle requests from the devices(pet-homes).

## Module pethome

### class Pethome

```python
def bootUp(request)
```

  - **input**: request(class) (```https://<server_url>/bootUp```)
  - **output**: UK(string)
  - **description**: This method handles the https requests that occur if pet-home is turned on. 
  If a request is received from Pet-Home, obtain the ```user_key``` and ```pet_count``` 
  from the corresponding module, generate and return the string ```UK```.
  
```python
def push(request)
```

  - **input**: request(class) (```https://<server_url>/push```)
  - **description**: This method is used when push requests are received from pet-homes. 
  When the user saves the request to pet home to the server, the pet home processes 
  the request and transmits the result over the url(```/push```). In the process, this method 
  is carried out and the push is finally sent to the user to inform them that 
  the task requested to Pet-Home has been completed.
  
```python
def sendRequest(request)
```

  - **input**: request(class) (```https://<server_url>/RQST```)
  - **output**: rq(string)
  - **description**: This method is used by Pet Home to ask if a chatbot server has work continuously. 
  If a user has asked a chatbot to do something, Pet Home will see, take it, and do the work. 
  This will be done by that method and the ```rq```(pet-home's works) will return the result.