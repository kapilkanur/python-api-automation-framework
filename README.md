# Python based REST API automation framework

## Setting up the application under test

The AUT is [Swagger Petstore](https://petstore3.swagger.io). The test suite in the framework would cover user, store, and pet endpoint functionalities. 
To avoid output that is unreliable, host the website locally, you can do so by following the instructions in the [README](https://github.com/swagger-api/swagger-petstore/blob/master/README.md).

## Library structure
<img width="272" alt="structure" src="https://github.com/kapilkanur/python-api-automation-framework/assets/36999492/e654e5e4-1db3-4806-a827-95baa09513d9">


- **api_client** : The package contains API client related code to make requests and handle response.
- **data** : This package contains classes for every model entities. These classes would be used to store data.
- **endpoints** : The endpoints package contains classes that contains various API endpoints of the application.
- **model** : The model package contains classes that represent various system entities. These classes contain the actions that can be carried out on an entity.
- **tests** : The tests package contains all the test cases for various APIs of the application.
- **utilities** : This package holds utility files that are used across the test cases.
- **pipfile** : This file lists all the Python dependencies required to run the API automation project
