# Item-Catalog
Create a restaurant menu app where users can add, edit, and delete restaurants and menu items in the restaurants.
## Setup and run the project
### Prerequisites
* Python 2.7
* Vagrant
* VirtualBox

### How to Run
1. Install VirtualBox and Vagrant
2. Clone this repo and also the vagrant file from https://github.com/udacity/fullstack-nanodegree-vm
3. Unzip and place the vagrant file and full-stack-p2 folder in your Vagrant directory
4. Launch Vagrant
```
$ vagrant up 
```
5. Login to Vagrant
```
$ vagrant ssh
```
6. Change directory to `/vagrant`
```
$ cd /vagrant
```
7. Initialize the database
```
$ python database_setup.py
```
8. Populate the database with some initial data
```
$ python populate.py
```
9. Launch application
```
$ python projectlogin.py
```
10. Open the browser and go to http://localhost:5000

### JSON endpoints
#### Returns JSON of all restaurants

```
/restaurants/JSON
```
#### Returns JSON of specific menu item

```
/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON
```
#### Returns JSON of menu

```
/restaurants/<int:restaurant_id>/menu/JSON
```
# full-stack-p2
