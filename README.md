# Item Catalog

Item Catalog is an application that provides a list of items within a variety of categories, as well as provide a user the capability to register (via OAuth) in an authentication system.  After the user has registered, he/she will have the ability to post, edit and delete their own items.


### Installation
Item Catalog requires python and vagrant to run.

Make sure to download the submitted ```fullstack-nanodegree-vm.zip```  and extract onto local machine. 

Navigate to the fullstack-nanodegree-vm/vagrant/catalog directory.

```sh
$ cd fullstack-nanodegree-vm/vagrant/catalog/
```

Launch vagrant, ssh into it, and then go to vagrant folder.

```sh
$ vagrant up
$ vagrant ssh
$ cd /vagrant/catalog/
```

Create and populate the catalog database.

```sh
$ python database_setup.py
$ python database_populate.py
```

Run application.py and navigate to http://localhost:8000 in your browser.
```sh
python application.py
``` 
### Running the application
* You can now run the application on http://localhost:8000
* Feel free to **C**reate, **R**ead, **U**pdate, and **D**elete items in the catalog
* Enjoy!
 
### Example of endpoints for JSON

http://localhost:8000/catalog.JSON
http://localhost:8000/user.JSON
http://localhost:8000/catalog/1/items.JSON
http://localhost:8000/catalog/1/items/1.JSON

### NOTES and Citings:
I have borrowed Udacity's Restaurant project as a template for my Item Catalog project.  The URL for Udacity's Restaurant project can be found here: https://github.com/udacity/ud330/tree/master/Lesson4/step2