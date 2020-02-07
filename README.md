# Web ToDo
The project let you organize your everyday tasks and avoid forgetting duties.
Now you can rest assured that you did what you had ToDo!

## Getting started
Easy hints how to cope with the application.

### Installation
To start using the application you should have installed: 

- Python (version 3.x). To do this type in terminal:

    `$ sudo apt-get update`
    
    `$ sudo apt-get install python3`
    
- Flask (version suitable for Python version). Check how to do this [here!](http://flask.pocoo.org/docs/0.10/installation/)

### Running
Now you have just to run main.py from main application directory.
Simply type in terminal:

`$ python3 main.py`

Now you have created local server, which you have to enter to start using the program. Just click the generated address and enjoy!

### Using

#### Adding
While run the main function of the application is adding new tasks to do. You can do this by clicking `Add new task`.
Then you have to specify the name of the task you want to add. Optionally, if the task has been already done, you can check the status to `done`.
After all click confirming button, what will save your task and redirect you to ToDo list.

#### Toggling done/undone
When you have at least one task on the list, you can change its state (done/undone) by clicking checkbox. When the task is complete its name will be also stricken through.

#### Editing
Another option is editing task, which had been already created. To apply changes you have to click pen button and follow the same steps as in adding task case.

#### Removing
To remove task you have to click cross button next to it. What is important, the task doesn't have to be done to be removed.

#### Using summary
This way you can add infinite number of tasks. Their content will be stored in database located in `models` directory.

## Files
The application consists of 3 main directories:
- models - includes database (`todo.db`) and backend Python files, which are responsible for all functions, 
- static - includes files, which are unchangeable during application work i.e. images or stylesheet files,
- templates - includes HTML files, which represent view of all necessary web pages.

The main application file is `main.py` located in main directory. This is application controller, which is responsible for communicating user activities coming from `views` to `database` through `models`.


## Built with
- Flask - micro web framework written in Python
- PyCharm - Python IDE
## Further development

There are plans of implementing:
- signing in feature
- adding task creation date and choosing deadline of the task
- improve layout of the page

## Authors
2017 Ⓒ Grzegorz Dubiel

## Acknowledgements
Special thanks for mentors of Codecool Kraków for given knowledge and patience.