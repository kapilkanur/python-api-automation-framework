# Python based REST API automation framework

## Setting up the application under test

The AUT is [Swagger Petstore](https://petstore3.swagger.io). The test suite in the framework would cover user, store, and pet endpoint functionalities. 
To avoid output that is unreliable, host the website locally, you can do so by following the instructions in the [README](https://github.com/swagger-api/swagger-petstore/blob/master/README.md).

## Library structure

### Model
The model package contains classes that represent various system entities. These classes contain the actions that can be carried out on an entity.

<img width="1086" alt="Screenshot 2023-01-18 at 8 23 18 AM" src="https://user-images.githubusercontent.com/36999492/213071779-019eb016-855e-44a1-8ee9-aefbee774975.png">


### Endpoints
The endpoints package contains classes that contains various API endpoints of the application.

<img width="930" alt="Screenshot 2023-01-18 at 8 15 27 AM" src="https://user-images.githubusercontent.com/36999492/213071798-d2c38f9b-40da-4fd6-91bc-469b3f7f3fc5.png">
