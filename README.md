# alu-AirBnB_clone

## AirBnB Clone

### Introduction

This repository contains the codebase for the initial stage of a project to build a clone of the AirBnB website. We are creating a command interpreter to manage AirBnB objects, enabling us to perform actions such as creating, retrieving, updating, and deleting objects.

### Project Description

Welcome to the Airbnb project, your first step towards building a full-fledged web application - the Airbnb clone. This initial phase is crucial as it sets the foundation for subsequent projects involving HTML/CSS templating, database storage, API integration, and front-end development. The backend of this project is powered by Python, leveraging its object-oriented programming (OOP) capabilities.

### Description of the Console/Command Interpreter

The command interpreter/console serves as the interface of the application, resembling the Bash shell with a limited set of commands specifically designed for the Airbnb website. Developed with Python OOP programming, it allows users to interact with the backend effectively. Some available commands include:

* show
* create
* update
* destroy
* count

These commands enable users to manage objects within the project, such as creating new users or places, retrieving objects from files or databases, performing operations on objects, updating attributes, and destroying objects.

### Repository Contents by Project Task

| Tasks | Files | Description |
|-------|-------|-------------|
| 0     | AUTHORS | Project authors (Bridget Chimdinma and Afsa Umutoniwase) |
| 1     | console.py /models/engine/file_storage.py /models/user.py | Implement the user class dynamically in the console and file storage system |
| 2     | /tests | Unit tests for all class-defining modules |
| 3     | console.py /models/engine/file_storage.py | Updates console and file storage system dynamically |
| 4     | /models/base_model.py | Parent class for inheritance by all model classes |
| 5     | /models/engine/file_storage.py /models/__init__.py /models/base_model.py | Manages a persistent file storage system |
| 6     | /models/user.py /models/place.py /models/city.py /models/amenity.py /models/state.py /models/review.py | Dynamically implements more classes |
| 7     | /models/base_model.py | Adds functionality to recreate an instance from a dictionary |
| 8     | N/A | Code complies with Pep8 standards |
| 9     | console.py | Enhance console program with essential functionality: quitting, handling empty lines, and graceful handling of ^D (Ctrl + D) input |
| 10    | console.py | Console methods for create, destroy, show, and update data |

### Usage

#### How to Start It

To start the console, follow these steps:

1. Clone the repository:
```
git clone https://github.com/amuhirwa/alu-AirBnB_clone.git
```
After cloning the repository, you will have a folder called AirBnB_clone. In here, there will be several files that allow the program to work.

2. Navigate to the project directory:
```
cd alu-AirBnB_clone
```

3. Run the command interpreter:
```
python console.py 
```

### Available Commands and What They Do

| Command | Description | Usage |
|---------|-------------|-------|
| quit or EOF | Exits the program | By itself |
| help | Provides a text describing how to use a command | By itself --or-- help < command > |
| create | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`. Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. | create < class name > |
| show | Prints the string representation of an instance based on the class name and `id` | show < class name > < id > --or-- < class name >.show(< id >) |
| destroy | Deletes an instance based on the class name and `id` (saves the change into a JSON file). | destroy < class name > < id > --or-- < class name >.destroy() |
| all | Prints all string representation of all instances based or not on the class name. | By itself or all < class name > --or-- < class name >.all() |
| update | Updates an instance based on the class name and `id` by adding or updating attributes (saves the changes into a JSON file). | update < class name > < id > < attribute name > "< attribute value >" --or-- < class name >.update(< id >, < attribute name >, < attribute value >) --or-- < class name >.update(< id >, < dictionary representation >) |
| count | Retrieves the number of instances of a class. | < class name >.count() |
