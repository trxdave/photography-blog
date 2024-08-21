# Photography Blog

View the live project here [Photography Blog](https://photography-blog-5d35eeace3db.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/trxdave/photography-blog)](https://github.com/trxdave/photography-blog/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/trxdave/photography-blog)](https://github.com/trxdave/photography-blog/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/trxdave/photography-blog)](https://github.com/trxdave/photography-blog)

Am I Responsive
Here's deployed site: [Am I Responsive](https://ui.dev/amiresponsive?url=https://photography-blog-5d35eeace3db.herokuapp.com/)

![alt text](documentation/images/amiresponsive1.png)

## Introduction

Photography Blog is a dynamic web application created for photography enthusiasts who wish to showcase their work and connect with a community of like-minded individuals. This platform allows users to upload their photos, categorize them, and engage with others through comments and likes. Whether you’re an amateur photographer or a seasoned professional, the Photography Blog offers a space to share your visual stories with the world.

## Project Overview

Photography Blog is a web application designed for photographers to share their work with a community. Users can upload photos, categorize them, leave comments, and interact with others by liking photos. The project emphasizes a user-friendly interface with responsive design, making it accessible on both desktop and mobile devices.

## Developer Goals
The primary goals for the development of the Photography Blog are:

1. Create an Intuitive User Interface: Develop a user-friendly and responsive interface that allows users to easily navigate the site, upload photos, and interact with other users.
2. Implement Robust User Authentication: Ensure that user data is securely handled with proper authentication mechanisms, allowing users to manage their profiles and content.
3. Enable Content Management: Provide users with the ability to upload, edit, and delete their photos, as well as categorize them for better organization and discovery.
4. Foster Community Interaction: Encourage user engagement through features like comments and likes, creating a social environment around photography.
5. Ensure Mobile Responsiveness: Design the site to be fully responsive, ensuring a seamless experience on devices of all sizes, from desktops to smartphones.
6. Utilize Cloud Storage for Media: Integrate cloud storage solutions to efficiently manage and serve images, optimizing performance and scalability.
7. Provide Comprehensive Error Handling: Implement custom error pages to handle common HTTP errors gracefully, improving the user experience even when things go wrong.

## User Goals
For users, the Photography Blog aims to fulfill the following goals:

1. Easily Share Photography: Users should be able to effortlessly upload and categorize their photos, making them accessible to others.
2. Engage with the Community: Users should be able to interact with other photographers through comments and likes, building a sense of community.
3. Explore a Wide Range of Photography: The platform should provide an easy way to browse and discover photos across different categories, helping users to find inspiration and new connections.
4. Manage Personal Content: Users should have control over their own content, with the ability to edit or delete their photos and manage their profile settings.
5. Access from Any Device: Users should enjoy a consistent and intuitive experience across all devices, whether they are on a desktop or mobile device.
6. Search for Specific Content: The platform should offer a search feature that allows users to quickly find photos or posts that match their interests.
7. Secure and Private Experience: Users should feel confident that their personal information is secure, and that they have privacy controls over their content.

## Problem Statement
### Background
Photography is a powerful medium for storytelling, yet existing platforms often fail to provide photographers with the tailored experience they need. General social media sites overwhelm quality content with sheer volume, making it difficult for photographers to stand out and connect meaningfully with their audience.

### Problem
Photographers face several challenges on current platforms:

- Lack of Niche Communities: General platforms don’t offer specialized spaces for photographers.
- Content Overload: Quality work often gets lost in a sea of posts.
- Limited Content Control: Users need better tools to manage and showcase their work.
- Poor Engagement: Existing interaction tools are often inadequate for meaningful feedback.
- Mobile Responsiveness Issues: Many platforms fail to provide a consistent visual experience across devices.

### Requirements
To address these challenges, the Photography Blog must:

- Offer User-Friendly Design: Easy navigation and content management.
- Encourage Engagement: Features like comments, likes, and search to enhance interaction.
- Ensure Responsiveness: Consistent design across all devices.
- Provide Secure Authentication: Protect user data and content.
- Foster Community Building: Tools that promote connections among photographers.

### Target Audience
This platform is designed for:

- Amateur Photographers: Looking to share and improve their skills.
- Professional Photographers: Seeking to showcase their portfolios and connect with peers.
- Photography Enthusiasts: Interested in exploring and engaging with visual content.
- Content Creators: Searching for a dedicated space to share high-quality photography.
- Art Directors & Agencies: Looking for new talent and inspiration.

## Entity-Relationship Diagram (ERD)
The Entity-Relationship Diagram (ERD) representing the relationships between the User, Category, Photo and Comment models.

- User to Photo: A one to many relationship where a user can upload many photos.
- Category to Photo: A one to many relationship where each photo belongs to one category.
- Photo to Comment: A one to many relationship where a photo can have many comments.
- User to Comment: A one to many relationship where a user can make many comments.
- User to Photo (Likes): A many to many relationship where users can like many photos, and each photo can be liked by many users.

![alt text](<documentation/erd/database-erd-photography-blog.png>)

# Learning Outcomes
1. ## Django Framework Proficiency:

- Develop a strong command of Django, a high-level Python web framework, by understanding its architecture, core components, and best practices for building robust, scalable web applications.

2. ## Bootstrap Integration:

- The integration of Bootstrap into Django projects to create responsive, mobile-first web designs efficiently, enhancing both the aesthetic appeal and user experience.

3. ## Python Programming Skills:

- Improve Python programming skills, with a focus on writing clean, efficient, and maintainable code that seamlessly integrates with Django’s architecture.

4. ## Image Handling with Pillow and Cloudinary:

- Learn to install and use Pillow, a powerful Python Imaging Library, to handle image processing tasks like uploading and resizing.
- Gain proficiency in integrating Cloudinary, a cloud-based service, to efficiently manage image storage, processing, and delivery. Leverage its APIs for advanced image optimization and manipulation.

5. ## CRUD Operations:

- The implementation of Create, Read, Update, and Delete (CRUD) operations in Django, enabling full management of data models and enhancing dynamic content interaction.
- Learn to build views and templates to handle these operations efficiently and securely.

6. ## User Authentication and Authorization:

- Gain expertise in implementing user authentication and authorization mechanisms in Django, ensuring secure access control for different parts of the application.
- Learn to integrate Django’s built-in authentication system to manage user login, registration, password management, and permission settings.

7. ## Template Rendering and Static Files Management:

- Understand Django’s template engine and how to create dynamic HTML templates that render data seamlessly from the backend.
- Learn to manage static files (CSS, JavaScript, images) in Django, ensuring efficient loading and organisation, particularly in production environments.

8. ## Javascript Integration and Engancement
- Develop JavaScript skills to enhance interactivity and user experience in Django applications.
- Learn to write custom JavaScript code for dynamic features such as search bars, toggle and dropdown.

# User Experience (UX)

The goal of this project is to create a seamless and enjoyable user experience for amateur photographers. The blog is designed to be intuitive, visually appealing, and functional, ensuring users can easily navigate the site, upload their work, and engage with the community.

# User Stories
1. As a Site User I can view a paginated list of posts so that easily select a post to view.
2. As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral.
3. As a Site User, I want to log in, so that I can access my account and manage my posts.
4. As a Site User, I want to upload photos, so that I can share my work with others.
5. As a Site User, I want to edit or delete my posts, so that I can manage my portfolio.
6. As a Site User, I want to comment on posts, so that I can provide feedback and engage with the community.
7. As a Site User, I want to log out, so that I can securely leave the site.

and more. [Link to the Kanban board here](https://github.com/users/trxdave/projects/6)

# Development Plan

This project was organized and executed using Agile methodology. A Kanban board within GitHub Projects was utilized to track progress and manage tasks, ensuring a structured and iterative development process. [Link to the Kanban board here](https://github.com/users/trxdave/projects/6)

![alt text](documentation/images/list.png)

# Features

## User Authentication
- Sign Up: New users can create an account.
- Login/Logout: Users can log in and out securely.
- Profile Management: Users can manage their profile and view their uploaded photos.

## Photo Management
- Upload Photos: Users can upload photos with titles, descriptions, and categorise them.
- Edit/Delete Photos: Users can edit or delete their photos.
- Photo Gallery: Users can browse through all photos uploaded by others.
- Like Photos: Users can like or unlike Photos.
- View Photo Details: Clicking on a photo displays a detailed view with the photo, title, description, likes, and comments.

## Comments
- Comment on Photos: Users can leave comments on photos.
- Delete Comments: Users can delete their comments.

## Search Functionality
- Search Bar: Users can search for photos by title or content directly from the navbar.

## Pagination
- Paginated Views: The photo gallery and comments are paginated for easy navigation.

## Responsive Design
- Mobile Friendly: The site is fully responsive, ensuring a seamless experience on mobile devices.

## Error Handling
- Custom Error Pages: The site includes custom error pages for 404, 500, 403 and 400 errors.

# Model Design

## Design
The design of the Photography Blog is modern and minimalist, with a focus on showcasing high-quality images. The layout is clean and simple, with ample whitespace to create a visually appealing experience for users. The color scheme is a combination of neutral tones, with accents of blue to evoke a sense of creativity and inspiration.

### base.html
- Navigation Bar: The navigation bar is placed at the top of the page, providing easy access to the main sections of the blog, including Home, Blog, About, Contact and user-specific options like My Photo List and Logout.

- Responsive Bahavior:
    - The navigation bar collapses into a hamburger menu on smaller screens.
    - It uses Bootstrap's responsive classes to ensure proper alignment and spacing.

![alt text](documentation/images/header.png)

- Header Image
- The header image spans the full width of the screen and adjusts its height based on the viewport. It serves as a visually engaging introduction to the site.

- Implementation:
    - The image is set as a background image in the CSS, using the background-size: cover property to maintain aspect ratio and cover the container.
    - The header image is responsive and adapts to different screen sizes without losing its aspect ratio.

![alt text](documentation/images/header-image.jpg)

- Welcome Section:
    - The homepage of the Photography Blog features a prominent welcome section designed to engage visitors immediately. This section includes a welcoming message, a visually appealing lens image, and a call-to-action button inviting users to explore the blog.

- Lens Image:
    - The welcome section includes a high-quality image of a camera lens, symbolizing the focus of the blog—photography.
    - Placement and Sizing: The image is placed below the welcome message and is responsive to screen size. It is designed to scale appropriately on mobile devices, tablets, and desktops, maintaining its visual impact without overwhelming the text.

- Action Button:
    - The button text reads "Explore My Blog," encouragaing users to dive deeper into the content.

![alt text](documentation/images/welcome.png)

- Footer: 
    - The footer is kept minimal and clean, with a dark background and white text. It includes social media icons and is centered for symmetry.
    - The footer's layout adjusts to ensure all elements remain accessible and visually appealing on all screen sizes.

![alt text](documentation/images/footer.png)

### blog.html
- The blog page showcases a collection of photography posts, organized into categories like Landscape, Portrait, Wildlife, Street, and Macro.

- Layout:
    - Category Navigation: A horizontal navigation bar at the top allows users to filter photos by category. The active category is highlighted for easy identification.
    - Photo Grid: Posts are displayed in a responsive grid layout, ensuring that images adjust smoothly across different screen sizes. Each photo is accompanied by a title and a short description.

- Responsive Design:
    - Mobile: The grid adjusts to a single column, ensuring photos and text are easily viewable.
    - Tablet and Desktop: The grid expands to multiple columns, providing a balanced and visually appealing display of content.

- Interactive Elements:
    - Photo Links: Each photo links to a detailed view where users can see the full post, read comments, and interact with the content.
    - Pagination: Users can navigate through multiple pages of posts with easy-to-use pagination controls at the bottom.
    
![alt text](documentation/images/blog1.png)
![alt text](documentation/images/blog2.png)

### Category Pages: Landscape, Portrait, Wildlife, Street, Macro

- Each category page presents a curated selection of photography posts focused on a specific theme, allowing users to explore content based on their interests.

- Layout:
    - Category-Specific Navigation: Users can switch between different categories using the navigation bar at the top. The current category is prominently highlighted.
    - Photo Display: Similar to the blog page, photos are displayed in a responsive grid layout with titles and short descriptions. Each image represents a unique perspective within the chosen category.

- Responsive Design:
    - Mobile: The grid adapts to a single column for optimal viewing on smaller screens.
    - Tablet and Desktop: Multiple columns are used to display photos, ensuring a balanced and organized presentation across devices.

- Interactive Elements:
    - Photo Links: Clicking on a photo takes the user to a detailed view, where they can explore the full post, read and leave comments, and interact with the content.
    - Pagination: For categories with a large number of posts, pagination controls are provided to navigate through multiple pages.

- Category-Specific Content:
    - Landscape: Focuses on natural scenery, capturing the beauty of the outdoors.
    - Portrait: Highlights individual and group portraits, showcasing emotions and expressions.
    - Wildlife: Features photography of animals and nature, emphasizing the diversity of wildlife.
    - Street: Captures the essence of urban life, with photos taken in streets and public places.
    - Macro: Delves into the details of small subjects, offering close-up views that reveal intricate details.

- Photo Management Features:
    - View Photos: Every user, whether logged in or not, can view all photos uploaded by any user. Each photo can be viewed in detail by clicking the "View" button, which redirects to a detailed view of the photo along with its description and any associated comments.
    - Edit Photos: Users who have uploaded photos have the option to edit them. When logged in, if a user views their own photos, they will see an "Edit" button alongside the photo. This button allows them to modify the photo's details, such as the title, description, or the photo itself.
    - Delete Photos: Similarly, users have the ability to delete their own photos. The "Delete" button appears next to photos owned by the logged-in user. Upon clicking, the user is prompted to confirm the deletion, ensuring that photos are not accidentally removed.

### landscape.html -
![alt text](documentation/images/landscape1.png)
### portrait.html -
![alt text](documentation/images/portrait1.png)
### wildlife.html -
![alt text](documentation/images/wildlife1.png)
### street.html -
![alt text](documentation/images/street1.png)
### macro.html -
![alt text](documentation/images/macro1.png)

### Add Photo Page -

- The "Add Photo" page is an essential feature of the Photography Blog, allowing users to contribute their own photography to the site. This page is only accessible to logged-in users. The key features of the "Add Photo" page include:

- Photo Upload: Users can easily upload their photos by selecting a file from their device. The photo will be stored and displayed on the blog, categorized according to the user's choice.

- Title and Description: Along with the photo, users are required to provide a title and a description. The title helps in identifying the photo, while the description allows the user to share the story or context behind the image.

- Category Selection: Users can categorize their photos by choosing from predefined categories such as Landscape, Portrait, Wildlife, Street, and Macro. This helps in organizing the photos within the blog and aids in easy navigation for viewers.

- Form Validation: The form on the "Add Photo" page includes validation to ensure all required fields are filled out correctly. If any issues are detected, the user is prompted to correct them before submission.

![alt text](documentation/images/addphoto1.png)

- Success Message: After successfully uploading a photo, users are redirected to a success page, and a success message is displayed. This confirms that their photo has been added to the blog and is visible to other users.

![alt text](documentation/images/photo-success-deleted.png)

### My Photo List Page

- The "My Photo List" page is a personalized feature for logged-in users, providing them with a dedicated space to manage their uploaded photos. This page displays all the photos a user has uploaded to the Photography Blog. The key features of the "My Photo List" page include:

- Personal Photo Gallery: Users can view a gallery of all the photos they have uploaded. Each photo is displayed with its title and a brief description, offering a quick overview of the user's contributions to the blog.

- View, Edit, Delete Options: For each photo in the gallery, users have the following options:

- View: Opens the detailed view of the photo, allowing the user to see it in full size along with all associated comments and likes.
- Edit: Allows the user to modify the title, description, or even replace the photo. This is useful for updating content or correcting any mistakes.
- Delete: Provides the option to remove the photo from the blog. A confirmation prompt ensures that users do not accidentally delete their content.
- Pagination: The photo list is paginated to ensure that the page remains easy to navigate, even for users with a large number of uploads. Users can easily navigate between pages to view all their photos.

- Responsive Design: The "My Photo List" page is designed to be fully responsive, ensuring a seamless experience across different devices, including desktops, tablets, and mobile phones.

This page serves as a personal management tool, giving users full control over their uploaded content on the Photography Blog. It encourages users to maintain and curate their gallery, contributing to the overall quality and organization of the site.

![alt text](documentation/images/photolist1.png)
![alt text](documentation/images/photolist2.png)
![alt text](documentation/images/photolist3.png)

### View Page
The View Page displays detailed information about a specific photo, including its title, description, and the photographer's username. Key features include:

- Photo Display: Large view of the image with detailed information below.
- User Interactions: Authenticated users can comment, like, and view the photo’s popularity.
- Owner Controls: If the user owns the photo, "Edit" and "Delete" buttons are available.
- Responsive Design: The page is fully responsive, ensuring optimal display across all device sizes.

![alt text](documentation/images/view1.png)
![alt text](documentation/images/view2.png)

### Edit Page
The Edit Page allows users to modify the details of their uploaded photos. Key features include:

- Form for Editing: Users can update the title, description, and category of the photo using a pre-filled form.
- Image Update: Option to change the photo if necessary.
- User Authentication: Only the photo's owner can access and edit the photo.
- Success Messages: After successfully updating the photo, the user is redirected with a confirmation message.
- Responsive Design: The form layout adjusts seamlessly across all device sizes, ensuring a smooth editing experience.

![alt text](documentation/images/edit.png)

### Delete Photo
The Delete Page allows users to permanently remove their uploaded photos. Key features include:

- Confirmation Prompt: Users are asked to confirm their decision to delete a photo to prevent accidental deletions.
- User Authentication: Only the owner of the photo has access to delete it, ensuring security and control.
- Success Messages: Upon successful deletion, users are redirected to the blog page with a confirmation message.
- Responsive Design: The confirmation layout is optimized for all device sizes, providing a consistent user experience.

![alt text](documentation/images/deletephoto.png)
![alt text](documentation/images/deletephoto1.png)

### About Us
The About Us page provides visitors with insights into the mission and vision of the Photography Blog. Key elements include:

- Introduction: A brief overview of the blog's purpose, highlighting its role in inspiring and educating photography enthusiasts.
- Mission Statement: Details on how the blog aims to connect photographers of all levels, offering tutorials, gear reviews, and inspiring photo galleries.
- Community Focus: Emphasis on building a community where photographers can share their experiences, engage in discussions, and showcase their work.
- Responsive Design: The page is fully responsive, ensuring readability and visual appeal across all devices.

![alt text](documentation/images/aboutus1.png)
![alt text](documentation/images/aboutus2.png)

### Contact Us
The Contact Us page is designed to facilitate communication between visitors and the Photography Blog team. Key features include:

- Contact Form: A straightforward form that allows users to submit inquiries, feedback, or requests. The form includes fields for name, email, and message, ensuring that the team can respond effectively.
- Success Message: Upon successful submission, users receive a confirmation message, assuring them that their message has been received.
- Responsive Design: The page is fully responsive, ensuring that the form is easy to use on all devices, from desktops to mobile phones.
- Security: The form includes validation and protection against spam, ensuring that all submissions are genuine and relevant.

![alt text](documentation/images/contactus.png)

### Sign Up
The Sign Up page allows new users to create an account on the Photography Blog. It includes a simple and user-friendly form where users can enter their desired username, email, and password. Upon successful registration, users are automatically logged in and redirected to the homepage. A success message is displayed to welcome the new user.

- User Registration: Users can sign up by providing a username, email, and password.
- Automatic Login: After registration, users are automatically logged in.
- Success Feedback: A confirmation message is shown to the user upon successful registration.
- Form Validation: The form includes validation to ensure all required fields are filled out correctly.

![alt text](documentation/images/signup.png)

### Login
The Login page provides a secure way for returning users to access their accounts on the Photography Blog. The page features a straightforward form where users can enter their username and password. After a successful login, users are redirected to the homepage.

- User Authentication: Users can log in with their registered username and password.
- Redirect on Success: After logging in, users are redirected to the homepage.
- Error Handling: If login credentials are incorrect, an error message is shown, prompting the user to try again.

![alt text](documentation/images/login.png)

### Error Page
The Photography Blog includes custom error pages to enhance user experience when something goes wrong. These pages ensure that even in the case of errors, users receive clear and helpful feedback. The custom error pages include:

- 400 Bad Request: This page appears when the server cannot process the request due to a client error, such as a malformed request syntax. It provides a simple, clear explanation and a link to navigate back to the homepage.

- 403 Forbidden: This page is shown when a user tries to access a resource they do not have permission to view. It clearly explains the issue and encourages the user to contact the site administrator if they believe this is an error.

- 404 Not Found: This page is displayed when a user attempts to access a page that doesn't exist. It provides a friendly message, suggesting that the user may have mistyped the URL or clicked on a broken link. The page includes a button to redirect users back to the homepage.

- 500 Internal Server Error: In the event of a server issue, this page informs the user that something went wrong on the server side. It suggests trying again later and includes a link to return to the homepage.

![400 Bad Request](documentation/images/400-bad-request.png)
![403 Forbidden](documentation/images/403-forbidden.png)
![404 Not Found](documentation/images/404-not-found.jpg)
![500 Internal Server Error](documentation/images/500-internal-server-error.png)

## Design Choices
The design choices were influenced by the need to create a platform that is easy to navigate and visually appealing. The use of a minimalist layout and neutral color scheme allows the focus to be on the photography, while the accents of blue add a touch of personality to the design.

## Colours
The colors used in the design are:

- Primary Text Color: #333 - Used for the main text across the website.
- Background Color: #f9f9f9 - Used for the overall background of the site and form backgrounds.
- Header Background Color: #333 - Used for the header and other key areas, providing a dark contrast.
- Button Primary Color: #4CAF50 - Used for primary action buttons, such as submit and upload.
- Button Hover Color: #3e8e41 - The hover state for primary buttons, creating an interactive feel.
- Alert Success Background: #dff0d8 - Used for success messages, like after form submissions.
- Alert Success Text: #3c763d - Text color for success alerts.
- Alert Danger Background: #f2dede - Used for error or danger messages.
- Alert Danger Text: #a94442 - Text color for error alerts.
- Footer Background Color: #333 - Provides a dark footer with contrasting white text.
- Footer Text and Icon Color: #fff - Ensures good readability against the dark background.

![alt text](documentation/images/color.png)

## Fonts
The fonts used in your project are:

Arial, sans-serif: This is the main font used throughout your CSS for body text and headings. It's a widely used, clean, and highly readable font that is supported across all browsers and devices.

# Wireframes

- Wireframes were created to visualize the layout and design of the photography blog.

## Desktop Wireframes

| **Page** | **Wireframes** | **Pass** |
--- | --- | :---: |
| About Us | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/aboutus.png)</details>| :white_check_mark:|
| Add Photo | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/addphoto.png)</details>| :white_check_mark:|
| Blog | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/blog.png)</details>| :white_check_mark:|
| Contact Us | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/contactus.png)</details>| :white_check_mark:|
| Homepage | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/homepage.png)</details>| :white_check_mark:|
| Landscape | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/landscape.png)</details>| :white_check_mark:|
| Login | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/login.png)</details>| :white_check_mark:|
| Macro | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/macro.png)</details>| :white_check_mark:|
| Photo List | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/photolist.png)</details>| :white_check_mark:|
| Portrait | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/portrait.png)</details>| :white_check_mark:|
| Sign Up | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/signup.png)</details>| :white_check_mark:|
| Street | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/street.png)</details>| :white_check_mark:|
| Wildlife | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/desktop/wildlife.png)</details>| :white_check_mark:|

## Mobile Wireframes

| **Page** | **Wireframes** | **Pass** |
--- | --- | :---: |
| About Us | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/aboutmobile.png)</details>| :white_check_mark:|
| Add Photo | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/addphotomobile.png)</details>| :white_check_mark:|
| Blog | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/blogmobile.png)</details>| :white_check_mark:|
| Contact Us | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/contactusmobile.png)</details>| :white_check_mark:|
| Homepage | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/homepagemobile.png)</details>| :white_check_mark:|
| Landscape | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/landscapemobile.png)</details>| :white_check_mark:|
| Login | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/loginmobile.png)</details>| :white_check_mark:|
| Macro | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/macromobile.png)</details>| :white_check_mark:|
| Photo List | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/photolistmobile.png)</details>| :white_check_mark:|
| Portrait | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/portraitmobile.png)</details>| :white_check_mark:|
| Sign Up | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/signupmobile.png)</details>| :white_check_mark:|
| Street | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/streetmobile.png)</details>| :white_check_mark:|
| Wildlife | <details><summary>Screenshot of result</summary>![Result](documentation/wireframes/mobile/wildlifemobile.png)</details>| :white_check_mark:|

# Testing

## Validator Testing

### HTML Validation
ll pages were validated, and the code was pasted in. A filter was applied to remove issues related to the Django templating system. 

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|base| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/base.png)</details>| :white_check_mark:|
|about| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/about.png)</details>| :white_check_mark:|
|add photo | No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/add-photo.png)</details>| :white_check_mark:|
|blog| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/blog1.png)</details>| :white_check_mark:|
|confirm delete| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/confirm-delete.png)</details>| :white_check_mark:|
|contact| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/contact.png)</details>| :white_check_mark:|
|edit photo| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/edit-photo.png)</details>| :white_check_mark:|
|homepage| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/homepage.png)</details>| :white_check_mark:|
|landscape| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/landscape1.png)</details>| :white_check_mark:|
|marco| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/macro1.png)</details>| :white_check_mark:|
|photo detail| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/photo-detail1.png) ![Result](documentation/validator/photo-detail2.png)</details>| :white_check_mark:|
|photo list| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/photo-list1.png) ![Result](documentation/validator/photo-list2.png)</details>| :white_check_mark:|
|portrait| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/portrait1.png)</details>| :white_check_mark:|
|search results| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/search-results.png)</details>| :white_check_mark:|
|street| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/validator/street1.png)</details>| :white_check_mark:|
|wildlife| No errors | <details><summary>Screenshot of result</summary>![Result]() ![Result](documentation/validator/wildlife1.png)</details>| :white_check_mark:|

### CSS Validation

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|styles.css | No errors |<details><summary>Screenshot of result</summary>![Result](documentation/validator/css-validation.png)</details>| :white_check_mark:|

## Python linter (PEP8)

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|admin.py| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/pep8/admin.png)</details>| :white_check_mark:|
|apps.py| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/pep8/apps.png)</details>| :white_check_mark:|
|forms.py| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/pep8/forms.png)</details>| :white_check_mark:|
|models.py| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/pep8/models.png)</details>| :white_check_mark:|
|url.py| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/pep8/urls.png)</details>| :white_check_mark:|
|views.py| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/pep8/views.png)</details>| :white_check_mark:|

## JShint

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|script.js| No errors | <details><summary>Screenshot of result</summary>![Result](documentation/js/jshint.png)</details>| :white_check_mark:|

## Accessibility

## PageSpeed Insights Accessibility Results
I used Google PageSpeed Insights to evaluate the accessibility of our website on both mobile and desktop platforms. PageSpeed Insights provides a score out of 100 for accessibility, which measures how well the content of the web pages is accessible to all users, including those with disabilities.

### Desktop Accessibility Scores

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|Homepages| 89 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/homepage-desktop.png)</details>| :white_check_mark:|
|Blog page| 84 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/blog-desktop.png)</details>| :white_check_mark:|
|Landscape page| 84 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/landscape-desktop.png)</details>| :white_check_mark:|
|Portrait page| 84 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/portrait-desktop.png)</details>| :white_check_mark:|
|Wildlife page| 88 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/wildlife-mobile.png)</details>| :white_check_mark:|
|Street page| 88 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/street-desktop.png)</details>| :white_check_mark:|
|Macro page| 84 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/macro-desktop.png)</details>| :white_check_mark:|
|About Us page| 89 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/aboutus-desktop.png)</details>| :white_check_mark:|
|Contact page| 88 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/contact-desktop.png)</details>| :white_check_mark:|
|Login page| 88 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/login-desktop.png)</details>| :white_check_mark:|
|Signup page| 88 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/signup-desktop.png)</details>| :white_check_mark:|


### Mobile Accessibility Scores

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|Homepages| 100 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/homepage-mobile.png)</details>| :white_check_mark:|
|Blog page| 89 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/blog-mobile.png)</details>| :white_check_mark:|
|Landscape page| 89 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/landscape-mobile.png)</details>| :white_check_mark:|
|Portrait page| 89 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/portrait-mobile.png)</details>| :white_check_mark:|
|Wildlife page| 94 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/wildlife-mobile.png)</details>| :white_check_mark:|
|Street page| 94 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/street-mobile.png)</details>| :white_check_mark:|
|Macro page| 89 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/macro-mobile.png)</details>| :white_check_mark:|
|About Us page| 100 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/about-mobile.png)</details>| :white_check_mark:|
|Contact page| 100 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/contact-mobile.png)</details>| :white_check_mark:|
|Login page| 100 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/login-mobile.png)</details>| :white_check_mark:|
|Signup page| 100 | <details><summary>Screenshot of result</summary>![Result](documentation/accessibility/signup-mobile.png)</details>| :white_check_mark:|

### Key Accessibility Highlights

- Consistent High Scores: The accessibility scores are consistently high across both mobile and desktop platforms, indicating that the site is well-optimized for accessibility on different devices.

- Responsive Design: The website's design adapts well to both mobile and desktop screens, ensuring that content remains accessible and usable regardless of the device being used.

- Color Contrast: All text elements meet the recommended contrast ratio, ensuring that text is easily readable against background colors on both mobile and desktop devices. This is crucial for users with visual impairments.

- Alt Text for Images: All images include descriptive alt attributes, allowing screen readers to convey the purpose of images to users who are visually impaired, on both mobile and desktop.

- Keyboard Navigation: The site is fully navigable using a keyboard, which is essential for users with motor disabilities who cannot use a mouse. Interactive elements like links, buttons, and forms are easily accessible via keyboard on both platforms.

- Form Labels: All forms, such as those on the Contact Us page, have associated labels, making it clear to screen reader users what information is required on both mobile and desktop.

- ARIA Landmarks: Appropriate ARIA (Accessible Rich Internet Applications) landmarks are used to help assistive technologies understand the structure of the page and navigate through sections effectively on both devices.

### Areas for Improvement

While the overall accessibility scores are high, there are a few areas where improvements could be made:

- Interactive Element States: Ensuring that all interactive elements, such as buttons and links, have visible focus states that are easy to identify when using a keyboard, especially on mobile where touch interactions are more common.

- Language Attributes: Ensuring that the lang attribute is correctly set on all pages to help screen readers determine the correct language of the content on both mobile and desktop.

- Form Validation: Enhancing client-side form validation with more descriptive error messages that are accessible to screen readers, particularly in mobile environments where screen space is limited.

- Skip Navigation Links: Adding "skip to content" links to allow keyboard users to bypass repetitive navigation menus and jump directly to the main content, which is especially helpful on mobile where screen size is smaller.

# Technologies Used

## Language Used:

- HTML: Used for structuring the content on the web pages. It forms the backbone of the project, ensuring that all elements are correctly placed and accessible.

- CSS: Used for styling the HTML elements, providing the visual appearance and layout of the web pages. CSS ensures the platform is visually appealing and user-friendly.

- JavaScript: Adds interactivity and dynamic behavior to the web pages. It enhances the user experience by allowing for real-time updates, form validations, and interactive elements.

- Python: a primary programming language for the backend of the project. It is used in conjunction with the Django framework to handle server-side logic, data processing, and integration with the database.

## Frameworks - Libraries - Programs Used:

1. Django
Purpose: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
Use Case: Used for building the backend, managing databases, handling user authentication, and rendering templates.

2. Bootstrap
Purpose: A popular front-end framework for developing responsive, mobile-first websites.
Use Case: Used for styling the website, creating responsive layouts, and ensuring a consistent design across devices.

3. Cloudinary API
Purpose: A cloud-based image and video management service.
Use Case: Used for handling image uploads, storage, and optimization, ensuring fast and reliable content delivery.

4. Pillow
Purpose: A Python Imaging Library that adds image processing capabilities to your Python interpreter.
Use Case: Used to manage and process image uploads, including resizing and format conversions.

5. JavaScript
Purpose: A programming language that enables dynamic content on web pages.
Use Case: Used for front-end interactions such as the search bar functionality, dropdowns, and form validations.

6. GitHub
Purpose: A platform for version control and collaborative development.
Use Case: Used to host the project repository, manage version control with Git, and collaborate through issues and pull requests.

7. JQuery
Purpose: A fast, small, and feature-rich JavaScript library.
Use Case: Used to simplify HTML document traversal and manipulation, event handling, and animation.

8. SQLite
Purpose: A lightweight, disk-based database that doesn’t require a separate server process.
Use Case: Used as the database for storing all application data during development.

9. Chrome DevTools
Purpose: A set of web developer tools built directly into the Google Chrome browser.
Use Case: Used for debugging JavaScript, analyzing runtime performance, and optimizing website responsiveness.

10. Balsamiq
Purpose: A wireframing tool that allows designers to create sketches of their web pages or applications.
Use Case: Used for creating wireframes and mockups to plan the layout and design of the website before development.

11. Responsive Design Mode
Purpose: A browser tool that allows developers to view their website on different screen sizes and resolutions.
Use Case: Used to test and ensure the website is responsive across a range of devices, including mobile phones and tablets.

12. Coolors.co
Purpose: An online tool for generating color palettes.
Use Case: Used to select and create the color scheme for the website, ensuring a visually appealing design.

13. StartBootstrap.com
Purpose: A website offering free and premium Bootstrap themes and templates.
Use Case: Used as a resource for finding Bootstrap templates and inspiration for the website’s design.

14. Heroku
Purpose: Used to deploy the Django application.
Use Case: Heroku is a cloud platform that lets companies build, deliver, monitor, and scale apps.

# Future Plans

1. Enhanced User Profiles
- Description: Develop detailed user profiles where photographers can showcase their portfolios and follow others.
- Objective: To create a more personalized and interactive community experience.

2. Advanced Search and Filtering
- Description: Implement advanced search options based on categories and tags to help users find specific content easily.
- Objective: To improve content discoverability and user experience.

3. Mobile App Development
- Description: Create a mobile app for Android and iOS to allow users to access and upload content on the go.
- Objective: To increase accessibility and engagement with a mobile-friendly solution.

4. Social Media Integration
- Description: Add features that allow users to share their photos directly to social media platforms like Instagram and Facebook.
- Objective: To broaden the reach of shared content and attract more users.

5. Photography Challenges
- Description: Organize photography challenges to engage the community and showcase talent.
- Objective: To increase user participation and foster a vibrant community atmosphere.

6. FAQ Page
- Description: Develop a comprehensive FAQ page to address common user queries and provide guidance on using the site.
- Objective: To enhance user support and reduce the need for direct inquiries by offering readily accessible information.

# Bugs

# Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

# Local Deployment #

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

# Credits
* [Man standing on rock formation](<documentation/images/hero-image.jpg>)
* [Black and silver DSLR lens](<documentation/images/lens.jpg>)
* [Nikon Camera](<documentation/images/nikon-camera.jpg>)
* [Inside out 'Bad Request' 400](<documentation/images/400.png>)
* [Inside out 'Forbidden' 403](<documentation/images/403.png>)
* [Inside out 'Not Found' 404](<documentation/images/404.png>)
* [Inside out 'Internal Server Error' 500](<documentation/images/500.png>)
* [Django Allauth](https://docs.allauth.org/en/latest/)
* [Django documentation](https://docs.djangoproject.com/en/5.0/)
* [Django Search Box](https://docs.djangoproject.com/en/5.0/search/?q=search+box)
* [Daisy's walkthrough](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=2)
* [Build a Photographer Personal Portfolio with Django 2020](https://www.youtube.com/watch?v=EBrm7h05vbg)
* [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
* [Cloudinary](https://cloudinary.com/)
* [Pexels](https://www.pexels.com/)
* [perplexity](https://www.perplexity.ai/)
* [Grammerly](https://app.grammarly.com/)


# Acknowledgements
* [Django](https://www.djangoproject.com/): For providing a robust and flexible web framework that made the development of this blog seamless.
* [Bootstrap](https://getbootstrap.com/): For the responsive grid system and pre-designed components that significantly enhanced the design and usability of the site.
* [Cloudinary](https://cloudinary.com/): For the powerful media management tools that made image handling in this project straightforward and efficient.
* [Gitpod](https://www.gitpod.io/): For offering a reliable online IDE that facilitated the development process.
* [Code Institute](https://codeinstitute.net/ie/): For providing the foundational knowledge and support necessary to undertake this project.
* [Stack Overflow](https://stackoverflow.com/): For the countless solutions and insights from the developer community.
* [W3Schools](https://www.w3schools.com/): For their comprehensive tutorials that served as a quick reference throughout development.
* [Hackathon](https://hackathon.codeinstitute.net/teams/445/): For the invaluable experience gained through participation, where I achieved 3rd place (Bronze). The challenges and teamwork during the event greatly contributed to my learning and growth as a developer.
* Thanks to Paul Thomas O'Riordan and Kristyna my Cohort Facilitator also Rory Patrick Sheridan my Code Institue Mentor, Tim Nelson second Mentor. 