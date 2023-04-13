# TITBIT

![Welcome to Titbit](documentation/##.png)

![Titbit](documentation/###.png)

Titbit is  a free social networking site where users broadcast short posts, where each user can create his own post and also like and comment on other users' posts.

Link to deployed site: [Titbit](https://titbit1.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/luandretta/titbit?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/luandretta/titbit?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/luandretta/titbit?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/luandretta/titbit?style=for-the-badge)

## CONTENTS

* [User Experience](#user-experience)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  * [Database Schema & User Journey](#database-schema--user-journey)
    * [User Journey](#user-journey)
    * [First Draft Database Schema](#first-draft-database-schema)
    * [Final Database Schema](#final-database-schema)

* [Features](#features)
  * [Elements Fount on Each Page](#elements-found-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Databases Used](#databases-used)
  * [Frameworks Used](#frameworks-used)
  * [Libraries & Packages Used](#libraries--packages-used)
  * [Programs Used](#programs-used)
    * [Error Handling](#error-handling)
    * [Defensive Programming](#defensive-programming)
    * [Database Migration to ElephantSQL](#database-migration-to-elephantsql)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)
  
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

- - -

## User Experience

### Project Goals



### User Stories

#### __Persona__

The target audience for Titbit are:
* over 18 years;
* titbit lovers all around the world;
* would like to stay informed;
* would like to promote courses;
* would like to share informations or their thoughts on social media;
* would like to influence people;
* wants to make jokes;
* would like to engage on society.


#### __First Time Visitor Goals__

As a first time user of the site I want to be able to:

* Understand what the site is for and how to navigate the site.
* Register for an account.


#### __Returning Visitor Goals__

As a returning registered user of the site I want to be able to:

* Log in to my account.
* Read the new posts.
* Create, edit, delete and view my posts.
* Create, edit, delete and view my comments.
* Like and dislike posts.
* Reset my password.
* Change my password.
* Follow others users.
* Be followed.

#### __Admin User__

As an administrator for the site I want to be able to:

* Remove any content that could be offensive.
* Delete or block users who not respect the rules.

### Agile
The Project Boards on GitHub was used to help to organize and prioritize the tasks.
The Kanban, as an agile project management tool, helped to visualize the tasks and limit the work in progress (WIP) by moving cards between the To do, In progress, and Done columns.

#### Burndown Chart

#### User Story Planning



- - -

## Design

### Colour Scheme

I have taken inspiration from the header image for the colour palette and chosen colours that complement each other.

![Colour Scheme for Titbit](documentation/###.png)

### Typography



I have used [Montserrat](https://fonts.google.com/specimen/Montserrat?query=montserrat&category=Sans+Serif) for the body text on the site. Monserrat is a sans-serif font which allows it to be legible and is a great choice for accessibility.

![Montserrat Font](documentation/montserrat.png)

### Imagery



### Wireframes

Wireframes were created for mobile, tablet and desktop using Balsamiq.

#### __Home Page__

![Home Page](documentation/wireframes/home.png)

#### __Register Page__

![Register Page](documentation/wireframes/register.png)

#### __Login Page__

![Login Page](documentation/wireframes/login.png)

#### __Profile Page__

![Profile Page](documentation/wireframes/profile.png)


#### __Error Page__

![Error Page](documentation/wireframes/error.png)

### Database Schema & User Journey

#### __User Journey__

![User Journey](documentation/user-journey.png)



- - -

## Features

The website is comprised of 12 pages which are extended from a base template.

* Home page
* Login page
* Register page
* Profile page
* Error page

### Elements found on each page

* Favicon 

  ![Titbit favicon](documentation/favicon.png)

* Navbar - The Navbar is displayed on all pages of the website and allows users to navigate the site with ease. The navbar is comprised of a logo, the sites name, links to navigate the site and a search bar. The links on the navbar will vary depending on whether a user is logged into their account.

  __User logged in Navbar__
  
  ![User logged in Navbar](documentation/logged-in-navbar.png)

  __User not logged in Navbar__

  ![User not logged in Navbar](documentation/not-loggedin-navbar.png)

* Footer - A footer is displayed on all pages of the website and contains the copyright year, this is updated to the current year using [JavaScript](bookworm/static/js/script.js).

  ![Footer](documentation/footer.png)

- - -

### Home Page

![Home Page](documentation/home-page.png)

### Login Page

![Log in Page](documentation/login-page.png)

### Register Page

![Register Page](documentation/register-page.png)

### Profile Page

![Profile Page](documentation/profile-page.png)

### News Page

![News Page](documentation/news-page.png)

### Error Page

![Error Page](documentation/error-page.png)

- - -

### Future Implementations

In future implementations I would like to:

* Add change and reset password functionality to the profile section.
* Give users the option to delete their account in the profile section.
* Allow admin to be able to delete posts that contain offensive material.
* Prepopulate the login fields after a user registers on the site and is redirected to the login page - this is good UX as we shouldn't expect a user to fill in the form with information we already have. 

### Accessibility

I have been mindful during coding to ensure that the website is as accessible friendly as possible. This has been have achieved by:

* Using semantic HTML.
* Using descriptive alt attributes on images on the site.
* Providing information for screen readers where there are icons used and no text.
* Ensuring that there is a sufficient colour contrast throughout the site.

- - -

## Technologies Used

### Languages Used

HTML, CSS, Javascript, Python

### Databases Used

[ElephantSQL](https://www.elephantsql.com/) - See [Database Migration to ElephantSQL](#database-migration-to-elephantsql) section for more information.

[Cloudinary]

### Frameworks Used

[Flask](https://pypi.org/project/Flask/) - A micro framework.

[Bootstrap](https://getbootstrap.com/) - version 5.2.0 - CSS Framework.

### Libraries & Packages Used


### Programs Used

[Pip](https://pypi.org/project/pip/) - Tool for installing python packages.

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine.

[Balsamiq](https://balsamiq.com/) - Used to create wireframes.

[Git](https://git-scm.com/) - For version control.

[Github](https://github.com/) - To save and store the files for the website.

[Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

[Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot and test features, solve issues with responsiveness and styling.

[Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.

[Shields.io](https://shields.io/) To add badges to the README.


### Flask Blueprints

I wanted to push myself a little with this project and decided that I would like to use Flask Blueprints. Flask Blueprints are a way of logically storing and organising similar routes of the app in their own section, rather than having one large file with all the routes of the app.


### Error Handling

While researching the best way to handle errors in a Flask application using blueprints I came across the following [article](https://nrodrig1.medium.com/flask-blueprints-error-handling-and-config-file-example-d1a031070763). I really liked how this solution allowed me to create a blueprint to custom handle a number of different errors, rather than just creating a single 404 error page.

### Defensive Programming


### Database Migration to ElephantSQL


- - -

## Deployment & Local Development

### Deployment

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.

2. Go to the repository for this project, [BookWorm](https://github.com/kera-cudmore/BookWorm).

3. Click the Fork button in the top right corner.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [BookWorm](https://github.com/kera-cudmore/BookWorm).

3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.

4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.

5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above):

    ```bash
    git clone { & THE LINK FROM STEP 3 }
    ```

6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).

7. Install the packages from the requirements.txt file by running the following command in the Terminal:

    ```bash
    pip3 install -r requirements.txt
    ```

- - -

## Testing

Please see [TESTING.md](TESTING.md) for all testing performed
- - -

## Credits

### Code Used

* [](https://) 

### Content

Content for this project was written by Lucimeri Andretta

### Media

* 

### Acknowledgments

I would like to acknowledge the following people who helped me along the way in completing this project:


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)