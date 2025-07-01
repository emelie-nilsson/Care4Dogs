# Testing

## Table of content
- [ User Stories](#-user-stories)
- [ Manual Testing](#-manual-testing)
- [ Validation testing](#validation-testing)
- [ Automated Testing](#automated-testing)
- [ Bugs](#-bugs)



### User Stories

Below are the user stories with their corresponding test validation steps.

---


#### User Story 1  
**As a visitor, I can read blog posts without an account so that I can learn from others' experiences**

| Acceptance Criteria                                           | Steps to Test                                            | Expected Outcome                                                   | Pass/Fail | Screenshot |
|---------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|-----------|------------|
| Posts are visible without login                               | Visit the blog page while logged out                      | Posts are displayed publicly                                        |  Pass ✅        |   ![blog post page](static\images\userstory1a.jpg)         |
| Each post displays title, author, date, and content           | View individual post page                                 | Title, author, date, and content are shown                          |  Pass ✅        | ![post](static\images\userstory1b.jpg)           |
| Users are prompted to register when attempting to comment or like | Try to comment or like a post while logged out            | Redirected to login/register or shown prompt                        |  Pass ✅        |  ![login form](static\images\userstory1c.jpg)          |

---

#### User Story 2  
**As a visitor, I can view how the platform works so that I can decide whether I want to join**

| Acceptance Criteria                                           | Steps to Test                                            | Expected Outcome                                                   | Pass/Fail | Screenshot |
|---------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|-----------|------------|
| A public “How It Works” page exists                           | Navigate to "How It Works" page                           | Page is accessible without login                                    |   Pass ✅       |      ![how it work section](static\images\userstory2a.png)      |
| Page explains the concept of mutual dog care with examples    | Read the content on the page                              | Explanation includes examples of how care exchange works           | Pass ✅         |  ![introduction](static\images\userstory2b.png)          |
| Call-to-action buttons to register or explore more            | Look for call-to-action buttons                           | Buttons are clearly visible and link to signup or explore sections |    Pass ✅      |      ![sign up](static\images\userstory2c.png)       |

---

#### User Story 3  
**As a visitor, I can sign up for an account so that I can access full functionality of the community**

| Acceptance Criteria                                           | Steps to Test                                            | Expected Outcome                                                   | Pass/Fail | Screenshot |
|---------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|-----------|------------|
| Sign-up form includes fields for name, email, password        | Go to registration page                                   | All fields are present and required                                | Pass ✅         |    ![signup form](static\images\userstory3a.png)        |
| Confirmation  after registration                 | Look for your name on the page                           | View username on top of the page                    |   Pass ✅       |      ![welcome name](static\images\userstory3b.png)       |

---

#### User Story 4  
**As a dog owner, I can post a request for dog-sitting help so that I can find someone to care for my dog when I need it**

| Acceptance Criteria                                           | Steps to Test                                            | Expected Outcome                                                   | Pass/Fail | Screenshot |
|---------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|-----------|------------|
| Post includes location, date(s), and a description            | Fill out new request form                                 | All fields are available and can be submitted                      | Pass ✅         |   ![Post form](static\images\userstory4b.png)        |
| Other users can view and respond to the request               | Log in with another user and view posts                   | Request is visible and interaction options are available           |   Pass ✅       |    ![Comment section](static\images\userstory4c.png)        |
| User can edit or delete the request                           | Open own post                                             | Edit and delete buttons are visible                                | Pass ✅         |  ![Edit and Delete](static\images\userstory4d.png)          |

---

#### User Story 5  
**As a dog owner, I can offer to help others with their dogs so that I can support the community and build trust**

| Acceptance Criteria                                           | Steps to Test                                            | Expected Outcome                                                   | Pass/Fail | Screenshot |
|---------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|-----------|------------|
| Users can respond to help requests                            | Click on another user’s post                              | Option to comment, message, or connect is shown                    |   Pass ✅       |   ![Responsed comment](static\images\userstory5a.png)         |
| Users can like posts as a way to show support                 | Click like on a post                                      | Like is registered and visually updated                            |Pass ✅          | ![Like counter](static\images\userstory5b.png)           |

---

#### User Story 6  
**As a registered user, I can comment on blog posts so that I can join the conversation**

| Acceptance Criteria                                           | Steps to Test                                            | Expected Outcome                                                   | Pass/Fail | Screenshot |
|---------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|-----------|------------|
| Comments appear in reverse chronological order                        | View comments on a post                                   | Comments are listed with the newest at the top                           |   Pass ✅       |   ![Comments with dates](static\images\userstory6a.png)         |
| Only logged-in users can comment                              | Attempt to comment while logged out                       | Redirected to login or shown prompt                                | Pass ✅         |   ![Log in to comment](static\images\userstory6b.png)         |

---

#### User Story 7  
**As the author of a post, I can see edit and delete buttons on my own posts so that I can manage and update my content when needed**

| Acceptance Criteria                                           | Steps to Test                                            | Expected Outcome                                                   | Pass/Fail | Screenshot |
|---------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|-----------|------------|
| Edit and delete buttons are only visible to the post author   | Log in as another user and view someone else's post       | No edit or delete options shown                                    |  Pass ✅        |  ![Compare posts](static\images\userstory7a.png)          |
| Users can edit or delete their own posts at any time          | Log in as author, open own post                           | Edit and delete options are shown                                  |  Pass ✅        |        ![Like counter](static\images\userstory7b.png)    |
| Changes are immediately reflected on the platform             | Edit content and save                                     | Updated content appears instantly                                  | Pass ✅         |    ![Update time](static\images\userstory7c.png)        |

---

#### User Story 8  
**As an admin, I can view all posts so that I can monitor the content shared on the platform**

| Acceptance Criteria                                           | Steps to Test                                            | Expected Outcome                                                   | Pass/Fail | Screenshot |
|---------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|-----------|------------|
| Admin has access to a dashboard with all user posts           | Log in as admin and access admin dashboard                | All user posts are visible                                         | Pass ✅         |  ![Admin dashboard](static\images\userstory8.png)          |


---

#### User Story 9  
**As an admin, I can delete inappropriate or harmful content so that the platform remains safe and respectful**

| Acceptance Criteria                                           | Steps to Test                                            | Expected Outcome                                                   | Pass/Fail | Screenshot |
|---------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|-----------|------------|
| Admin can delete any post                                     | Log in as admin and delete any user’s post                | Post is removed                         |   Pass ✅        |     ![Confirmation of deleted post](static\images\userstory9a.png)       |
| A confirmation message appears before a post gets deleted                | Click delete on a post                                    | Prompt confirms the action                                        |   Pass ✅        |  ![Confirmation before delete](static\images\userstory9b.png)           |
| Deleted posts are removed immediately from public view        | Confirm deletion                                          | Post no longer visible to any user                                |  Pass ✅         |  ![Post deleted](static\images\userstory9c.png)           |


## Manual Testing

### Responsive Design Testing

The application was tested across multiple screen sizes, with Chrome DevTools, and with [Am I Responsive](http://ami.responsivedesign.is/).

✅ Confirmed that all pages display as intended on:
- Mobile (e.g. Samsung Galaxy A51, Iphone 15)
- Tablet (e.g. iPad)
- Laptop (e.g. Asus Vivobook)
- Desktop (1080p screen)

All elements (cards, buttons, forms) stack or resize as expected for readability and usability.

*Asus Vivobook*  
![Top homepage](static\images\asus.vivobook1.png)
![Top post list](static\images\asus.vivobook2.png)
![Log in](static\images\asus.vivobook3.png)

*Samsung Galaxy A51*  
![Post list](static\images\samsung1.jpg)
![Post details](static\images\samsung2.jpg)
![Logged out](static\images\samsung3.jpg)

---

### Browser Compatibility

The site was tested and works as expected in the following browsers:

| Browser         | Result |
|-----------------|--------|
| Google Chrome   |✅ Pass |
| Mozilla Firefox |✅ Pass |
| Microsoft Edge  |✅ Pass |
| Safari          |✅ Pass |

There were no styling or functionality issues detected in these browsers.

---

### Validation testing
#### HTML

The live rendered pages were validated using the [W3C HTML Validator](https://validator.w3.org/) by entering the public URLs.  
✅ No critical errors found. This approach avoids false errors caused by Django template syntax (e.g., `{% %}` tags).

*Homepage*  
![HTML Validation Homepage](static\images\validator.index.png)

*Post list*  
![HTML Validation Post list](static\images\validator.postlist.png)

*Post details*  
![HTML Validation Post details](static\images\validator.postdetails.png)  
During HTML validation, a warning appeared regarding the `<hr>` tag and the trailing slash (`/`). However, inspection in browser DevTools shows the tag is rendered correctly as `<hr>` without a trailing slash.

This indicates that the warning is a false positive and does not affect the rendered page.

![DevTools Screenshot of `<hr>` tag](static\images\validator.devtools.png)


*Log in*  
![HTML Validation Post list](static\images\validator.login.png)

*Sign up*  
![HTML Validation Post list](static\images\validator.signup.png)

#### CSS Validation

The main stylesheet (`base.css`) was tested using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).  
✅ Passed without errors.

![CSS Validation Screenshot](static\images\validator.css.png)

---
### Lighthouse Performance Testing

The Care4Dogs homepage was tested with Google Lighthouse, achieving high scores across key categories including Performance, Accessibility, Best Practices, and SEO.

![Lighthouse Performance](static\images\lighthouse.png)

## Automated Testing

### Form Validation Tests

These automated tests ensure that key form validation logic works as expected. All tests were written using Django’s TestCase framework and can be run with `python manage.py test`.

#### ✅ CommentForm

| Test Name           | Purpose                                  | Result |
|---------------------|-------------------------------------------|--------|
| test_form_is_valid  | Checks that the comment form validates when content is provided | ✅ Passes |

#### ✅ DogCarePostForm

| Test Name                     | Purpose                                                                 | Result |
|-------------------------------|-------------------------------------------------------------------------|--------|
| test_valid_form               | Ensures form passes with all required fields                           | ✅ Passes |
| test_missing_title            | Ensures form fails if title is empty                                   | ✅ Passes |
| test_missing_dates            | Ensures form fails if date_from or date_to are missing                 | ✅ Passes |
| test_date_to_before_date_from| Ensures form fails if end date is before start date, using custom clean() | ✅ Passes |

---

> All form validation tests passed successfully as of `2025-06-30`. The forms now include custom validation logic for date order.

---

### View Tests
![View testing](static\images\test_views.png)

The image shows how a test user and a test post are created, including an empty image file.

Purpose: To verify that the views work correctly without triggering Cloudinary errors.

✅ Result: All view tests passed:
- The post list view loads successfully.
- Login is required to access the post creation view.



## Bugs

### ❗ Known Issue: Mixed Content Warning

During testing, a mixed content warning appeared in the browser console:
![Warning](static\images\warning.png)

According to common troubleshooting resources, this may occur when external resources (such as images from Cloudinary) are returned with `http://` URLs instead of `https://`. Modern browsers typically upgrade these requests automatically, so images still display correctly and securely.

This does not currently affect the functionality or security of the live application. The issue is likely caused by how Cloudinary returns image URLs during post creation.

 An attempt was made to explicitly configure Cloudinary to return `https://` URLs. However, this resulted in a crash of the deployed app, likely due to conflicts in authentication or environment configuration (related to Heroku + MFA access tokens). Therefore, the change was reverted to restore app functionality.

The warning has no visible impact and may be revisited in a future update or production refinement.

### Other Bugs & Issues Encountered

Throughout development, a number of  bugs were identified and resolved. Here are some examples:

- **Post images not displaying correctly**  
    - The Cloudinary image didn’t appear on cards due to missing `.url` in the template.  
  ✅ Fixed by updating `{{ post.image }}` to `{{ post.image.url }}`.


- **No confirmation before deleting a post**  
    - Initially, clicking "Delete" removed a post without warning.  
  ✅ Solved by adding a simple `onclick="return confirm(...);"` inline in the template.

- **Footer not sticking to the bottom**  
    -  The footer floated mid-page when content was short.  
  ✅ Resolved by using `flex` layout on `body` and `main { flex: 1; }`.

- **Validation errors due to void elements**  
    -  HTML Validator flagged trailing slashes  as problematic.  
    ✅ All void elements were changed to the correct format.  
ℹ️ Some slashes might still show up online, added automatically by services like Cloudinary.

- **Comment form overlapping with footer**  
    - On mobile, the form overlapped with the footer.  
  ✅ Fixed with proper spacing and layout tweaks.

- **Heroku login blocked by MFA**  
    - Could not access logs or deploy due to Multi-Factor Authentication issues.  
  ✅ Contacted Heroku support and temporarily switched settings to restore access.

