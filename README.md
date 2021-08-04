# Book Review, a review and recommendation site for books.

![The Markup from responsive design](static/readme-resources/markup.jpg)


## Milestone project 3 (Code Institute)

This is a simple website where you can upload details of books, and allow users to write comments about any book and upvote it..

**[View the repository on GitHub](https://github.com/manell0/MileStone-3-Book-Review)**

**[View The Cryptopedia on Heroku](http://milestone-3-book-review.herokuapp.com/get_books)**

- For testing, please use the following login information:
   - Username: admin / Password: admin
      - For admin privileged pages 
   - For regular users. Just register an account
## Table of contents

1. [Introduction](#introduction)
2. [UX](#ux)
   1. [Ideal User Demographic](#Ideal-User-Demographic)
   2. [User Stories](#User-Stories)
   3. [Development Planes](#Development-Planes)
   4. [Design](#Design)
3. [Features](#Features)
   1. [Design Features](#Design-Features)
   2. [Existing Features](#Existing-Features)
   3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
   1. [Main Languages Used](#Main-Languages-Used)
6. [Testing](#Testing)
   - [Go to the Testing file](testing.md)
7. [Deployment](#Deployment)
   1. [Deploying on GitHub Pages](#Deploying-on-GitHub-Pages)
   2. [Forking the Repository](#Forking-the-Repository)
   3. [Creating a Clone](#Creating-a-Clone)
8. [Credits](#Credits)
   1. [Content](#Content)
   2. [Media](#Media)
   3. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)

# Introduction

- This small website was designed mainly for people who like and reads books. People who want to find inspiration for new books.


- The focus of the website is to create an easy way to reach people who want to find new books. To make the site more attractive, we add a rating comment section.


- The simplicity and small scale of the website is an important aspect to achieve an interest in bookmarking the return page.

- If you like simple book review sites, you have gone to enjoy this one.


- This is the third of four Milestone projects that the developer must complete during his Full-Stack web development program at The Code Institute.

- The most important requirements were to build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records (CRUD). [**HTML5**](https://en.wikipedia.org/wiki/HTML5),  [**CSS3**](https://en.wikipedia.org/wiki/CSS), [**JavaScript**](https://en.wikipedia.org/wiki/javascript), [**Flask**](https://flask.palletsprojects.com/en/2.0.x/) and [**MongoDB**](https://www.mongodb.com/).

[Back to the top](#table-of-contents)

# UX

## Ideal User Demographic

### The ideal user of this website is

- People who like to read books.
- People who want to find new books to read.
- Users who like book reviews.
- People who simply want to spend some time in a developing and fun way.

## User Stories

### New/Potential Fans Goals:

1. As a new user, I want to be able to easily find new books.

2. As a new user, I want to be able to find out how this book review site works and what it is about.

3. As a new user, I want to be able to rate the books.

4. As a new user, I want to be able to write a review.

5. As a new user, I want to be able to register an account.

6. As a new user, I want to be able to add books.

7. As a new user, I want to be able to log out from the site.

### Current Fans Goals:

1. As a current user, I want to navigate to high rated books.

2. As a current user, I want to navigate to my added books

## Development Planes

| **_[Strategy](#Strategy)_** | **_[Scope](#Scope)_** | **_[Structure](#Structure)_** | **_[Skeleton](#Skeleton)_** | **_[Surface](#Surface)_** |
| --------------------------- | --------------------- | ----------------------------- | --------------------------- | ------------------------- |

### Strategy

With these goals in mind, a strategy table was created to determine the trade-off between importance and viability with the following results:

**_[Link to Strategy Trade-off as PDF](static/readme-resources/strategy-trade-off.pdf)_**

![Spreadsheet Strategy](static/readme-resources/strategy-trade-off.jpg)

### Scope

- The site is for people who like books and want to find new books to read.

- Users who find this website are most certainly one who is looking for just and precisely for a book review and recommendation site.

#### A scope was defined into two categories:

- ##### Content Requirements

  - The user will be looking for:
    - Information about the books and the possibility to rate them.
    - A quick way to find high rated books.

- ##### Functionality Requirements
  - The user will be able to:
    - Easily navigate through the site to find the information they want.
    - Easily find, add books and give a description and summary of the books.

### Structure

The information architecture was organized in a hierarchical tree structure to ensure that users could navigate through the site with ease and efficiency, with the following results:

![Hierarchical tree structure](static/readme-resources/Structure.jpg)

### Skeleton

Wireframe mockup was created in a Figma Workspace with providing a positive user experience in mind:

**_[Link to Figma Wireframes as PDF](static/readme-resources/wireframe.pdf)_**

![Wireframes screenShot as PDF](static/readme-resources/Wireframe.jpg)
[Back to the top](#table-of-contents)

### Surface

[Markup from: ami.responsive design.is](http://ami.responsivedesign.is/)

![The Markup from responsive design](static/readme-resources/markup.jpg)

## Design

### Color Scheme

The main colors used throughout the website are teal, creamy white and little brown for headers.



The chosen color scheme is chosen to get a clear and nice view to integrate with.

- I find the color combination on-site [COLORS](https://coolors.co/)

### Typography

Font font-family: Roboto is used throughout the website with Sans Serif as the fallback font in case of import failure.

- I use [Google fonts](https://fonts.google.com/) for my font used on the site

### Picture

- The images used on the page are copied link addresses found via Google.

- The images provide a static alternative text to use if the element cannot be reproduced.

  [Back to the top](#table-of-contents)

# Features

### Design Features

Each page on the website has a consistent, responsive navigation system through a navigation bar on the top of the site.


### Existing Features

#### The website consists of four main pages (Home, users books, Add book, Log Out/ Log In and register) and Manage Categories only for Admin (Login: Username = admin, and password = admin).

- ### Start Page (Home):
  - Navbar on top of the Home page is the same across the whole site.
   - Home goes to the start page.
   - Users Books goes to the owner's books page for editing and deletion.
   - Add Book goes to add_book form.
   - Manage Categories (Only for admin) goes to the page where admin can add and delete categories(LogIn: Username = admin, and password = admin).
   - Log In / Log Out page for log in and log out.
   - Register for new user to register.
   
   
  - At the top of the page, we find our navbar which turns into a burger for smaller screen sizes..
    - At the top of the page is a search box.
    - In the center of the page we have the Users' posted books that are clickable for expansion for more information.
    
- ### User Owners books:
  - Here, the user can edit and delete their uploaded books.
  - In the expandable field we find two (green for edit and red for delete) icons/buttons:
    - The first button is the green edit button:
      - Are used if you want to edit your own books.
    - The second button is the delete button:
      - Are used to immediately delete the selected book .
    

- ### 404 page (404.html):
  - Not done yet due to lack of time. &#129324;

## Features to Implement in the future

- When deleting a book or category, make sure that it is verified. Instead of the book being removed immediately without verification.


[Back to the top](#table-of-contents)

# Issues and Bugs

- Problems getting verification for book removal to work. Ended up lacking time, so I had to put that feature on future implement.


- Problems with my javascript code appearing with 8 spaces when looking in GitHub. Apparently can not be changed.

  - Solution: You can append ?ts=2 or ?ts=4 to the URL to change the tab-size.

# Technologies Used

### Main Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/Javascript)

- [Python](https://www.python.org/)

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

- [MongoDB](https://www.mongodb.com/)

### Frameworks, Libraries & Programs Used

- [Materialize](https://materializecss.com/)

- [Google fonts](https://fonts.google.com/)

- [jQuery](https://jquery.com/)

- [Font Awesome icons](https://fontawesome.com/icons?d=gallery&p=2&m=free)

[Back to the top](#table-of-contents)

# Testing

[Testing information can be found in this separate testing file](testing.md)

# Deployment

- This project was developed using Gitpod, committed to git, and pushed to GitHub using the bash in Gitpod.
- Some updates were done directly in edit mode on GitHub.

## Deploying on GitHub Pages

To deploy this page to GitHub Pages from its GitHub repository, the following steps should have taken:

1. Log into [GitHub or create an account](https://github.com/).
2. Locate the GitHub Repository.
3. At the top of the repository, select Settings from the menu items.
4. Scroll down the Settings page to the "GitHub Pages" section.
5. Under "Source" click the drop-down menu labeled "None" and select "Master Branch".
6. Upon selection, the page will automatically refresh meaning that the website is now deployed.
7. Scroll back down to the "GitHub Pages" section to retrieve the deployed link.
8. At the time of submitting this Milestone project the Development Branch and Master Branch are identical.

## Forking the Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub or create an account](https://github.com/).
2. Locate the GitHub Repository.
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

## Creating a Clone

How to run this project locally:

1. Install the GitPod Browser Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub or create an account](https://github.com/).
4. Locate the GitHub Repository.
5. Click the green "GitPod" button in the top right corner of the repository. This will trigger a new GitPod workspace to be created from the code in GitHub where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log in to GitHub or create an account.
2. Locate the GitHub Repository.
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.

```
git clone https://github.com/USERNAME/REPOSITORY

```

8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [**_here_**](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)


## Local Deployment: 
This project was developed using Gitpod as the chosen IDE and GitHub as a remote repository. The Project's source files were regularly pushed to the GitHub repository [Book Review repository](https://github.com/manell0/MileStone-3-Book-Review) via the master branch.

To reproduce this project within a local deployement, use the following steps and requirements:

1. Have the following installed in your IDE of choice:
   - Git (for version control)

   - pip (package installer for Python; pip3 was used at the time of production: Juli 2021)

   - Python3 (the programming language used to produce the backend logic of this project) using the following command:
      - pip3 install dnspython

- Flask (the library used to add special features and functionalities to this Python application) using the following command:
      - pip3 install flask

2. Create an account with MongoDB, following the MongoDB instructions for the creation of a Cluster and Collections, and connect your database server with your Flask application:

   - From your MongoDB cluster dashboard >> click on CONNECT >> choose "Connect your application" >> Driver: Python and Version: your python version.

   - Register your MONGO_URI credentials inside your env.py file withing your project, by using the follwoing commands:
      - touch .gitignore
      - touch env.py
      
   - Connect your MongoDB data to your Flask app using the following command:
      - pip3 install flask-pymongo
   
   - Add the environment variables to your env.py file:
      ```
      import os

      os.environ.setdefault("MONGO_URI", "your_mongodb_credential_data")
      os.environ.setdefault("MONGO_DBNAME", "your_mongodb_name")
      os.environ.setdefault("IP", "0.0.0.0")
      os.environ.setdefault("PORT", "5000")
      os.environ.setdefault("SECRET_KEY", "your_secret_key")
      ```
3. Install additional packages:
   - pip3 install flask-paginate

4. Update the requirements.txt file using the following command:
   - pip3 freeze > requirements.txt

5. These files were added, commited and pushed to github using the commands git add git commit git push .

## Heroku Deployment: 
The Project's source file was also pushed to Heroku via the heroku master branch. To deploy this app to a Heroku app use the following steps:

1. A requirements.txt file was created using the terminal command pip3 freeze > requirements.txt.

2. A Procfile was created using the terminal command echo web: python app.py > Procfile.

3. A new app was created for the Cryptopedia on Heroku dashboard, by clicking the "New" button and setting the region to Europe. It is necessary to open an account with Heroku and start a new app installation inside your heroku dashboard.

4. New app configurations including environament variables were added on "Settings" > "Reveal Config Vars" inside the Heroku dashboard:
   ```
   - IP: 0.0.0.0
   - PORT: 5000
   - SECRET_KEY: your_secret_key
   - MONGO_URI: your_mongodb_credential_data
   - MONGO_DBNAME: your_mongodb_name
   ```
5. From the Heroku dashboard the app was deployed using the "Deploy button" and connected to the gihub master branch for automatic deployments.

6. These files were added, commited and pushed to github using the commands git add git commit git push .

7. The web app is now successfully deployed.







[Back to the top](#table-of-contents)

# Credits

- I have used [Rebecca Tracey-Timoneys](https://github.com/rebeccatraceyt) README file [KryanLive](https://github.com/rebeccatraceyt/KryanLive/blob/master/README.md) as a guide/template for this README file.

- I have used [Kes Cardoso](https://github.com/kescardoso) Deployment for Heroku as inspiration on this README.md.

- I have used tutor Tim Nelson´s mini project (Task Manager) as a basis for my milestone project.
  [Tim Nelson´s mini project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/054c3813e82e4195b5a4d8cd8a99ebaa/)


## Content

## Media

- The images on the pages are copied (link address) is found on Google.


## Code

The developer consulted multiple sites to better understand the code they were trying to implement. For code that was copied and edited, the developer made sure to reference this with the code. The following sites were used on a more regular basis:

- [Stack Overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/) used a lot, and the Modal pop-up window came from there.
- [Materialize](https://materializecss.com/) used for my grid system throughout the site
- [MongoDB docs](https://docs.mongodb.com/manual/) used for better database understanding.
- [COLORS](https://coolors.co/)
- [Google fonts](https://fonts.google.com/) used for my fonts (Architects Daughter and Open Sans)

# Acknowledgements

- I would like to thank my mentor, Owonikoko Oluwaseun, for her help and guidance throughout this process.

  [Back to the top](#table-of-contents)
