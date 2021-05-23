# **Description** 

# **Airbnb Clone - The Console** 
The Console is the first project at Holberton School which focuses on teaching students how to build their very first web application.   This repository holds the first set of building blocks for a series of projects which will expand upon concepts like HTML/CSS templating, database storage, API, and front-end integration.  

# **The Console**

The challenge is to create a powerful command line interpreter which assists in the creation, management(serialization /deserialization), and storage(JSON) of instance objects of various class types.  These objects and their attributes will eventually be utilized to share information assigned to “HBNB listings” via a web application.  Our powerful file storage engine allows the console to create, update, destroy, save and reload object instances via command line arguments.

# **Usage**

The console’s command line interpreter works in interactive mode in this way:

```
AirBnB_clone$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) quit
AirBnB_clone$
```



The console’s command line interpreter works in non-interactive mode in this way:
```
AirBnb_clone$$ echo "create BaseModel" | ./console.py

(hbnb) 042d938e-c8e7-433e-883f-07508cd9306e
```
``` 
AirBnB_clone$ echo "help create" | ./console.py 

(hbnb)  Create a new instance object of specified class and print objects id.
```



### **Commands**
 
* **create** - create an object instance 
* **show** - print an object instance 
* **destroy** - delete and object instance 
* **all** - print all object instances of specified type
* **update** - updates relevant instance attributes of an object
* **quit** - exits the command line interpreter 
* **EOF** - exits the command line interpreter 
* **help** - prints command documentation

### **Create**
To create an instance of an object use **“create”**:

```
(hbnb) create User
```

### **Show**
To show an instance of an object use  **“show”** the _class type_ and _id_:

```
(hbnb) show BaseModel 6c47b07e-1e11-4fb3-b05c-8e4029c6a59c
```

### **Destroy**
To delete an instance of an object use **“destroy”** with _class type_ and _id_:

```
(hbnb) destroy State 68c7b07e-a411-4x93-b0z8-8e476tt6a47b
```

### **All**
To show all instance objects or all instances of a _class type_ use “all”:

```
(hbnb) all
```

**or**

```
(hbnb) all Amenity
```

### **Update**
To update an instance use **“update”** with _class type_ and _id_:

```
(hbnb) update BaseModel e41dec10-7c90-491e-b60f-cf976fe20381 email and_i_OOP@gmail.com
```

### **Quit/ EOF**
To exit the command line interpreter type **“quit”** or **“EOF”**:

### **Help**
To see a list of available commands use **“help”** or to learn about a given command use **“help <command>”**:

```
(hbnb) help
```

**or**

```
(hbnb) help destroy
```

### **Supported Classes**

* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### **Authors**

Grace Fallon - 2745@holbertonschool.com
Chris Vanndy - 2736@holbertonschool.com
