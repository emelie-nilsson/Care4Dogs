
# Care4Dogs
 
![Responsive images of website](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/responsive.webp)


## Table of content
* [Introduction](#introduction)
* [Agile Workflow & Prioritisation](#agile-workflow--prioritisation)
* [User experience](#user-experience)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Introduction
**Care4Dogs** is a community-based web app where dog owners can support each other with dog care – whether it's for a weekend trip, workday, or unexpected situation. The platform allows users to post requests when they need help, and offer assistance to others when they have the time and flexibility.

The goal is to make it easier for dog owners to connect locally, build trust, and create a network where help goes both ways – based on shared love for dogs and mutual support.

This app was created as a full-stack Django project with user authentication, content management, and responsive design for desktop, tablet, and mobile.

[Live Demo](https://care4dogs-60c9d8251c5f.herokuapp.com/)

## Agile Workflow & Prioritisation

During the development of *Care4Dogs*, the project followed an Agile-inspired process. Based on the assessment criteria, clear goals were defined early on and transformed into a list of **User Stories** (see [User Stories](#user-stories)).

Although GitHub Projects or issue tracking was not used, user stories were written manually and prioritised using the **MoSCoW method**.

The MoSCoW method was chosen as a simple yet effective way to prioritise functionality during a time-limited solo development process.

### Must Have  
These were the highest priority (User Stories 1–9) and made up the core of the application.  
They included:
- Full **CRUD** functionality (Create, Read, Update, Delete) for dog care posts  
- User authentication (sign up, log in, log out)  
- Viewing other users’ posts and post details  

✅ All of these features were completed and tested.

### Should Have  
These features would improve the experience but were not essential for core functionality.

**Example:**  
*As a user, I want to be able to update or delete my own comments, so I can manage what I’ve written.*

**Acceptance Criteria:**
- Only the author of a comment sees “Edit” and “Delete” options  
- Clicking “Edit” opens a form with the original comment  
- Clicking “Delete” removes the comment after confirmation  

### Would Have  
These were considered “nice to have” features that could be added in a future version.

**Example:**  
*As a user, I want to have a personal profile page with more information, so others can get to know me better before connecting.*

**Acceptance Criteria:**
- A profile page is accessible from the username  
- The user can edit bio, dog info, contact preferences, etc.

Due to time limitations, *Should Have* and *Would Have* stories were not implemented and are instead listed in the [Future Features](#future-features) section.


## User experience
The following user stories were defined based on the initial project goals. Stories 1–9 were considered *Must Have* and were prioritised for development and testing.

### **Visitor**
#### User Story 1
**As a visitor**, I can read blog posts without an account so that I can learn from others' experiences
-  Posts are visible without login
- Each post displays title, author, date, and content
- Users are prompted to register when attempting to comment or like

#### User Story 2
**As a visitor,** I can view how the platform works so that I can decide whether I want to join

- A public “How It Works” page exists
- Page explains the concept of mutual dog care
- Call-to-action buttons to register or explore more

#### User Story 3
**As a visitor,** I can sign up for an account so that I can access full functionality of the community

- Sign-up form includes fields for name, email, password
- Confirmation  after registration

### **Registered User**

#### User Story 4
**As a dog owner,** I can post a request for dog-sitting help so that I can find someone to care for my dog when I need it

- Post includes location, date(s), and a description
- Other users can view and respond to the request
- User can edit or delete the request

#### User Story 5
**As a dog owner,** I can offer to help others with their dogs so that I can support the community and build trust

- Users can respond to help requests
- Users can like posts as a way to show support

#### User Story 6
**As a registered user,** I can comment on blog posts so that I can join the conversation

- Comments appear in reverse chronological order
- Only logged-in users can comment

#### User Story 7
**As the author of a post,** I can see edit and delete buttons on my own posts so that I can manage and update my content when needed

- Edit and delete buttons are only visible to the post author
- Users can edit or delete their own posts at any time
- Changes are immediately reflected on the platform

### **Admin user**

#### User Story 8
**As an admin,** I can view all posts so that I can monitor the content shared on the platform

- Admin has access to a dashboard with all user posts

#### User Story 9
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
![Wireframe laptop homepage](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/wireframe-cp1.webp)

![Wireframe laptop post list](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/wireframe-cp2.webp)
![Wirefram laptop form](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/wireframe-cp3.webp)  
*Wireframe tablet*  

![Wireframe tab1](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/wireframe-tab1.webp)

![Wireframe tab2](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/wireframe-tab2.webp)

![Wireframe tab3](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/wireframe-tab3.webp)

*Wireframe mobile*  
![Wireframe mob1](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/wireframe-mob1.webp)


### Fonts and color theme

The color theme for the application was inspired by an image selected for the homepage. Using a color picker tool, [Image color picker](https://imagecolorpicker.com/), a palette was extracted directly from the image to ensure visual harmony. From this palette, five core colors were chosen to represent the app’s visual style throughout the design. These colors are consistently used for backgrounds, buttons, highlights, and text to give the app a cohesive and friendly design.

Some exceptions to the color palette were made intentionally for critical actions. For example, delete buttons and confirmation prompts use stronger, more contrasting colors. This is to clearly signal caution and help prevent users from accidentally deleting content.

*Original image*  
![Original image](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/welcome.jpg)  
*Extracted palette*   
![Extracted palette](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/colorpicker.jpg)  
*Final selected colors*  
![Final selected colors](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/colorpalette.jpg)

1.  Golden brown #a08653
2.  Light beige #e1dad4 
3.  Darkbrown  #332415 
4.  Chestnut #663115
5.  Greyish blue #4a647a 

The project uses two fonts: **Nunito** as the primary font for body text, and **Raleway** as the secondary font, mainly used for headings. This combination makes the text easy to read and gives the design a clean and modern look.
### Images
All images in the project were downloaded from [Freepik](https://www.freepik.com). To make the site load faster, the images were resized and converted to `.webp` format using [CloudConvert](https://cloudconvert.com). This helps keep the file sizes small without losing too much quality, which makes the app quicker to load – especially on slower connections or mobile devices.

A simple logo was created with the help of [ChatGPT](https://chatgpt.com), based on the app’s concept and chosen color theme. A version of the logo was also used to generate the site’s favicon, using [Favicon.io](https://favicon.io), to give the app a clear visual identity in browser tabs.

![Logo](https://github.com/emelie-nilsson/Care4Dogs/raw/main/static/images/logo.webp)



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

These features were considered desirable but were not essential for the core functionality. As time did not allow for their implementation, they are listed here as possible additions in a future version of *Care4Dogs*.

- Add optional user profile fields, including dog name, breed, and location *(Would Have)*
- Let users update their profile information after registration *(Would Have)*
- Enable private messaging between users *(Should Have)*
- Allow users to confirm when dog care help has been agreed *(Should Have)*
- Let admin feature selected posts on the homepage *(Would Have)*
- Allow users to rate and review their dog care experience *(Would Have)*

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
- ChatGPT – for planning and documentation support

## Testing

The application was tested using a combination of **manual** and **automated** methods to ensure that all key features work as intended. This included:

- ✅ **Form validation testing** for both comment and post forms  
- ✅ **View testing** to confirm correct page access and Cloudinary image handling  
- ✅ **Responsiveness testing** on mobile, tablet, and desktop  
- ✅ **Manual testing** of all critical user stories to verify real-world functionality

Automated tests were written using Django’s `TestCase` class and cover key logic such as date validation and form input handling. All tests passed successfully.

For a full breakdown of test cases, screenshots, and results, see the dedicated [TESTING.md](TESTING.md) file.


## Version Control

Git was used throughout the development process to manage code versions and track progress. The project is hosted on GitHub, where the main branch contains the latest production-ready code.

### Common Git Commands Used
- `git add .` – Adds all changes to the staging area
- `git commit -m "message"` – Saves the changes with a message
- `git push` – Uploads commits to GitHub

For most of the project, deployment to Heroku was done manually via the Heroku dashboard. However, during a period when the Heroku interface was temporarily unavailable, I used `git push heroku main` to deploy directly from the terminal.

Because of this, a few commits were pushed only to Heroku and not to GitHub, which may cause a slight difference between the two commit histories.

### Deployment


This Django project was deployed using [Heroku](https://www.heroku.com/) with GitHub integration for continuous deployment. Below is an overview of the steps taken to get the app live:

#### 1. Create the Heroku App
I logged into my Heroku dashboard and created a new app by clicking **"New" > "Create new app"**. I chose a unique app name and selected the appropriate region (Europe).

#### 2. Connect to GitHub
Under the **"Deploy"** tab in Heroku, I connected my GitHub account and selected the repository for this project.

#### 3. Manual Deployment from GitHub
Instead of automatic deployment, I use manual deployment through the Heroku dashboard. After pushing changes to the `main` branch on GitHub, I go to the **"Deploy"** tab in Heroku and click **"Deploy Branch"** to publish the latest version of the app.


#### 4. Set Environment Variables
In the **"Settings"** tab, under **"Config Vars"**, I added the necessary environment variables:

- `SECRET_KEY` – the Django secret key  
- `DATABASE_URL` – connection string for the production database  
- `CLOUDINARY_URL` – used for image uploads and hosting  

These help manage security, image hosting, and correct configuration between local and production environments.

#### 5. Buildpacks
In the same **"Settings"** tab, I added the Python buildpack (`heroku/python`) to make sure Django would run properly.

#### 6. Static Files
Heroku automatically runs `python manage.py collectstatic` on each deployment to collect all static files (CSS, JavaScript, etc.). This ensures they are served correctly in production.

#### 7. Test the Live App
Finally, I clicked **"Open app"** in Heroku to confirm that the site was deployed and functioning correctly.


### How to clone the repository
1. From the list of repositories, click the repository you want to clone. 
2. Click the green button **Code**.
3. Choose **HTTPS** followed by **Open with GitHub Desktop**.
4. Click **Choose** and navigate to a local directory where you want to clone the repository.
5. Click **Clone**

### How to fork the repository
1. From the list of repositories, click the repository you want to fork.
2. Click on the **Fork** button in upper right hand corner.

## Credits

### Code

This project was greatly supported by several outstanding YouTube channels known for their clear, practical, and project-based Django tutorials. These channels were invaluable for learning how to build real-world Django applications and best practices:

- **[Traversy Media](https://www.youtube.com/c/TraversyMedia)**  
- **[Dave Gray](https://www.youtube.com/watch?v=Rp5vd34d-z4&list=WL&index=34&t=1763s)**  
- **[Legion Script](https://www.youtube.com/watch?v=sMqDJovFO-Y&list=WL&index=35)**  
- **[Dee Mc](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)**  

### Other Helpful Resources

- The **[Code Institute’s LMS](https://codeinstitute.net/)**, providing structured learning materials with practical exercises.  
- **[Codecademy](https://www.codecademy.com/learn/learn-python-3)**, whose interactive Python lessons helped make learning the basics of coding both accessible and interesting. 
- The official **[Django Documentation](https://docs.djangoproject.com/en/stable/)**, an essential resource for understanding Django.  
- **[Real Python](https://realpython.com/)**, offering detailed and practical tutorials on Python and Django development.  
- The official **[Python Tutorial](https://docs.python.org/3/tutorial/)** from Python.org, providing a strong foundation in Python basics. 
- The **[Stack Overflow](https://stackoverflow.com/)** community. 

### Content
The content and ideas, including some descriptions in the dog care requests, were developed with assistance from ChatGPT, which helped brainstorm and write parts of the text.

### Acknowledgements

I want to warmly thank everyone who contributed in different ways during this project:

- My mentor Spencer, for valuable feedback and support during the final stages of the project.  
- Family and friends, who kindly took the time to test the app and provided helpful insights.  
- My brother, who patiently offered advice and guidance when I got stuck in the coding jungle.  
- The family’s own veterinarian, who generously helped with identifying and naming all the dog breeds.  
- ChatGPT, for assisting with brainstorming ideas and troubleshooting coding challenges.