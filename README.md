# Deploying Machine Learning models in Microsoft Azure

#### Referred https://www.youtube.com/watch?v=g687fRBNNGo&t=94s

### 1. Create a new Container Registry in Azure and create a new resource group within it.


### 2. Once created, go to your resouce and click on "Access Keys".


### 3. Enable admin user and save your login server and password locally as it will be needed for authentication later for deployment. Let's call it [LOGIN] and [PSSWD] for the sake of documentation.


### 4. Build the docker image using the following naming convention. Note: [APPLICATION_NAME] can be anything but it's recommended to use a name related to the project being implemented.

```
docker build -t [LOGIN]/[APPLICATION_NAME]:latest .
```

### 5. Login with your Azure login server that you locally saved earlier. Enter your resource group name under Username. Enter the password you saved earlier [PSSWD]. 
```
docker login [LOGIN]
```

### 6. Push the docker image to Microsoft Azure.
```
docker push [LOGIN]/[APPLICATION_NAME]:latest
```

### 7. Create an Azure Web App. If there is an error in creation, choose a different region.

### 8. Go to Deployment Center. Change the source to Github Actions and save.

