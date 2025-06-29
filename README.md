
# Care4Dogs
 


![Responsive images of website](staticfiles\images\responsive.webp)

## Table of content
* [Introduction](#introduction)
* [User experience](#user-experience)
* [Design](#design)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Introduction
**Care4Dogs** is a community-based web app where dog owners can support each other with dog care – whether it's for a weekend trip, workday, or unexpected situation. The platform allows users to post requests when they need help, and offer assistance to others when they have the time and flexibility.

The goal is to make it easier for dog owners to connect locally, build trust, and create a network where help goes both ways – based on shared love for dogs and mutual support.

This app was created as a full-stack Django project with user authentication, content management, and responsive design for desktop, tablet, and mobile.

## User experience

### **Visitor**
#### User Story 1
**As a visitor**, I can read blog posts without an account so that I can learn from others' experiences
-  Posts are visible without login
- Each post displays title, author, date, and content
- Users are prompted to register when attempting to comment or like

#### User Story 2
**As a visitor,** I can view how the platform works** so that I can decide whether I want to join

- A public “How It Works” page exists
- Page explains the concept of mutual dog care with examples
- Call-to-action buttons to register or explore more

#### User Story 3
**As a visitor,** I can sign up for an account so that I can access full functionality of the community

- Sign-up form includes fields for name, email, password
- Confirmation email is sent after registration

### **Registered User**

#### User Story 4
**As a dog owner,** I can post a request for dog-sitting help so that I can find someone to care for my dog when I need it

- Post includes location, date(s), and a description
- Other users can view and respond to the request
- User can edit or delete the request

#### User Story 6
**As a dog owner,** I can offer to help others with their dogs so that I can support the community and build trust

- Users can respond to help requests
- Users can like posts as a way to show support

#### User Story 7
**As a registered user,** I can comment on blog posts so that I can join the conversation

- Comments appear in chronological order
- Only logged-in users can comment

#### User Story 8
**As the author of a post,** I can see edit and delete buttons on my own posts so that I can manage and update my content when needed

- Edit and delete buttons are only visible to the post author
- Users can edit or delete their own posts at any time
- Changes are immediately reflected on the platform

### **Admin user**

#### User Story 9
**As an admin,** I can view all posts so that I can monitor the content shared on the platform

- Admin has access to a dashboard with all user posts
- Posts are listed regardless of privacy settings or ownership

#### User Story 11
**As an admin,** I can delete inappropriate or harmful content so that the platform remains safe and respectful

- Admin can delete any post
- A confirmation prompt appears before deletion
- Deleted posts are removed immediately from public view


## Design


### Wireframes
The initial wireframes for the project were created using [Whimsical](https://whimsical.com/) during the early planning stages. They served as a visual guide to outline the basic structure and user flow of the platform.

Please note that some essential features, such as the log in functionality, are not represented in the wireframes. These were added later in the development process as the scope and requirements of the application became clearer.

As a result, the final design of the application has evolved significantly. The current appearance and layout differ from the original wireframes, reflecting both design decisions and functionality improvements made along the way.

*Wireframe laptop*
![Wireframe laptop homepage](staticfiles\images\wireframe-cp1.webp)
![Wirefram laptop post list](staticfiles\images\wireframe-cp2.webp)
![Wirefram laptop form](staticfiles\images\wireframe-cp3.webp)
*Wireframe tablet*
![Wirefram tablet homepage](staticfiles\images\wireframe-tab1.webp)
![Wirefram tablet post list](staticfiles\images\wireframe-tab2.webp)
![Wirefram tablet form](staticfiles\images\wireframe-tab3.webp)
*Wireframe mobile*
![Wirefram tablet form](staticfiles\images\wireframe-mob1.webp)

### Fonts and color theme

The color theme for the application was inspired by an image selected for the homepage. Using a color picker tool [Image color picker](https://imagecolorpicker.com/), a palette was extracted directly from the image to ensure visual harmony. From this palette, five core colors were chosen to represent the app’s visual style throughout the design. These colors are consistently used for backgrounds, buttons, highlights, and text to give the app a cohesive and friendly design.

Some exceptions to the color palette were made intentionally for critical actions. For example, delete buttons and confirmation prompts use stronger, more contrasting colors. This is to clearly signal caution and help prevent users from accidentally deleting content.

*Original image*
![Original image](staticfiles\images\welcome.jpg)
*Extracted palette* 
![Extracted palette](staticfiles\images\colorpicker.jpg)
*Final selected colors*
![Final selected colors](staticfiles\images\colorpalette.jpg)

1.  Golden brown #a08653
2.  Light beige #e1dad4 
3.  Darkbrown  #332415 
4.  Chestnut #663115
5.  Greyish blue #4a647a 

The project uses two fonts: **Nunito** as the primary font for body text, and **Raleway** as the secondary font, mainly used for headings. This combination makes the text easy to read and gives the design a clean and modern look.
### Images
All images in the project were downloaded from [Freepik](https://www.freepik.com). To make the site load faster, the images were resized and converted to `.webp` format using [CloudConvert](https://cloudconvert.com). This helps keep the file sizes small without losing too much quality, which makes the app quicker to load – especially on slower connections or mobile devices.

A simple logo was created with the help of [ChatGPT](https://chatgpt.com), based on the app’s concept and chosen color theme. A version of the logo was also used to generate the site’s favicon, using [Favicon.io](https://favicon.io), to give the app a clear visual identity in browser tabs.

![Logo](staticfiles\images\logo.webp)



## Features
### For all visitors
- Browse all dog care posts without logging in
- View post details including title, content, user, date, and location
- Access the “How it works” page to understand how the platform functions

### For registered users
- Create an account with username, email and password
- Log in to access full functionality
- Post requests when you need help with dog care
- Create a post to offer dog care and support to other users
- Edit or delete your own posts
- Like posts to show support
### For admin
- View and manage all posts and user accounts
- Delete inappropriate or harmful content


### Future features
- Add optional user profile fields, including dog name, breed, and location
- Let users update their profile information after registration
- Enable private messaging between users
- Allow users to confirm when dog care help has been agreed
- Let admin feature selected posts on the homepage
- Allow users to rate and review their dog care experience
## Technologies Used
The project was built using the following tools, technologies, and resources:
### Languages & Markup
- Python
- HTML5
- CSS3
- JavaScript

### Frameworks & Libraries
- Django
- Bootstrap 5
- Font Awesome

### Tools & Services
- Git & GitHub – for version control and hosting
- Heroku – for deployment
- Cloudinary – for image hosting
- PostgreSQL – production database
- SQLite – development database
- Google Fonts – for typography (Nunito & Raleway)
- VS Code – code editor

### Design & Content Tools
- Whimsical – for early wireframes
- Freepik – for images
- Colorpicker – to extract colors from images
- CloudConvert – to convert and compress images to `.webp`
- Favicon.io – for favicon generation
- Am I Responsive – to generate device preview image
- ChatGPT – for planning, documentation support, and structure

## Testing
### Validation

 
### Responsiveness


### User stories


### Manual testing


### Bugs


### Unfixed bugs


## Deployment

This Django project was deployed using [Heroku](https://www.heroku.com/) with GitHub integration for continuous deployment. Below is an overview of the steps taken to get the app live:

### 1. Create the Heroku App
I logged into my Heroku dashboard and created a new app by clicking **"New" > "Create new app"**. I chose a unique app name and selected the appropriate region (Europe).

### 2. Connect to GitHub
Under the **"Deploy"** tab in Heroku, I connected my GitHub account and selected the repository for this project.

### 3. Manual Deployment from GitHub
Instead of automatic deployment, I use manual deployment through the Heroku dashboard. After pushing changes to the `main` branch on GitHub, I go to the **"Deploy"** tab in Heroku and click **"Deploy Branch"** to publish the latest version of the app.


### 4. Set Environment Variables
In the **"Settings"** tab, under **"Config Vars"**, I added the necessary environment variables:

- `SECRET_KEY` – the Django secret key  
- `DATABASE_URL` – connection string for the production database  
- `CLOUDINARY_URL` – used for image uploads and hosting  
- `DEVELOPMENT` – set to control whether `DEBUG` mode is active

These help manage security, image hosting, and correct configuration between local and production environments.

### 5. Buildpacks
In the same **"Settings"** tab, I added the Python buildpack (`heroku/python`) to make sure Django would run properly.

### 6. Static Files
Heroku automatically runs `python manage.py collectstatic` on each deployment to collect all static files (CSS, JavaScript, etc.). This ensures they are served correctly in production.

### 7. Test the Live App
Finally, I clicked **"Open app"** in Heroku to confirm that the site was deployed and functioning correctly.


## Version Control

Git was used throughout the development process to manage code versions and track progress. The project is hosted on GitHub, where the main branch contains the latest production-ready code.

### Common Git Commands Used
- `git add .` – Adds all changes to the staging area
- `git commit -m "message"` – Saves the changes with a message
- `git push` – Uploads commits to GitHub

For most of the project, deployment to Heroku was done manually via the Heroku dashboard. However, during a period when the Heroku interface was temporarily unavailable, I used `git push heroku main` to deploy directly from the terminal.

Because of this, a few commits were pushed only to Heroku and not to GitHub, which may cause a slight difference between the two commit histories.

### Deployment


### How to clone the repository


### How to fork the repository


## Credits
### Code





Other web development learning resources,

* [W3 Schools](https://www.w3schools.com/)
* [Stack Overflow](https://stackoverflow.com/questions)

### Content


### Acknowledgements

