# Photography Blog

View the live project here [Photography Blog](https://photography-blog-5d35eeace3db.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/trxdave/photography-blog)](https://github.com/trxdave/photography-blog/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/trxdave/photography-blog)](https://github.com/trxdave/photography-blog/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/trxdave/photography-blog)](https://github.com/trxdave/photography-blog)

Am I Responsive
Here's deployed site: [Am I Responsive](https://ui.dev/amiresponsive?url=https://photography-blog-5d35eeace3db.herokuapp.com/)

## Introduction

Photography has the power to capture moments, tell stories, and evoke emotions. With the increasing popularity of social media platforms, photographers often find their work lost amidst the noise. This project aims to create a dedicated space where amateur photographers can showcase their work, share their experiences, and connect with like-minded individuals.

## Project Overview

For my fourth portfolio project, I have decided to create a photography blog. The purpose of this site is to provide a serene and focused environment where amateur photographers can display their work without the distractions and competitive nature of social media. This blog will serve as a platform for photographers to gain exposure, receive constructive feedback, and engage with a community that shares their passion.

## Developer Goals
1. Create a User-Friendly Interface: Design a clean, intuitive interface that allows users to easily navigate through the blog, view photography posts, and interact with the content.
2. Build a Responsive Website: Ensure that the blog is fully responsive and accessible on various devices, including desktops, tablets, and smartphones.
3. Implement Photography Showcase Features: Develop features that allow photographers to upload their work, add descriptions, and categorize their photos for better visibility.
4. Enable Community Interaction: Integrate functionality for comments, and likes.
5. Optimize Performance: Ensure the website loads quickly and efficiently, providing a smooth user experience even with high-resolution images.

## User Goals
1. Showcase Photography: Provide a platform for amateur photographers to display their work in a professional and aesthetically pleasing manner.
2. Receive Feedback: Allow users to receive constructive feedback and appreciation from the community, helping them to improve their skills.
3. Share Stories: Enable photographers to share the stories behind their photos, giving context and depth to their visual art.

This photography blog will not only serve as a portfolio for my development skills but also as a meaningful platform for the photography community to thrive and grow.

## Entity-Relationship Diagram (ERD)

![alt text](<documentation/erd/Database ER diagram Photography Blog.png>)

# Learning Outcomes
1. ## Django Framework Proficiency:

- Gain a deep understanding of Django, a high-level Python web framework, including its architecture, components, and how to effectively use it to build robust web applications.

2. ## Bootstrap Integration:

- Learn to integrate Bootstrap, a popular front-end framework, into a Django project to create responsive, mobile-first web designs with minimal effort.

3. ## Python Programming Skills:

- Enhance Python programming skills, focusing on writing clean, efficient, and maintainable code that integrates seamlessly with Django.

4. ## Image Handling with Pillow and Cloudinary:

- The installation and use of Pillow, a Python Imaging Library fork, to handle image processing tasks such as uploading and resizing.
- Integrate Cloudinary, a cloud-based image and video management service, for efficient storage, processing, and delivery of images, leveraging its APIs for image optimization and manipulation.

5. ## CRUD Operations:

- Full CRUD (Create, Read, Update, Delete) functionality, allowing users to create, view, update, and delete their photography posts.

6. ## User Authentication and Authorization:

- User authentication and authorization features in Django, providing secure login, registration, and user management functionalities. Include sign-up, logout, and login features to manage user sessions effectively.

7. ## Template Rendering and Static Files Management:

- Learn to use Django's template system to render dynamic content and manage static files like CSS, JavaScript, and images effectively.

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

# Development Plan

This project was organized and executed using Agile methodology. A Kanban board within GitHub Projects was utilized to facilitate this, with tasks and objectives managed through interconnected GitHub Issues. [Link to the Kanban board here]

# Features

## Login

- The standard login form template from Django is styled to match the look of the rest of the site. It requests a username and password, with an option to remember the login.

## Sign Up
- The standard signup form template from Django is styled to match the look of the rest of the site. It requests a username and a password that meets certain criteria.

## Sign In
- The standard sign-in form template from Django is styled to match the look of the rest of the site. It requests a username and password, with an option to remember the login.

## Log Out
- The standard logout form template from Django is styled to match the look of the rest of the site. It simply confirms that you want to log out.

# Model Design

## Design

### Colours




# Wireframes

- Wireframes were created to visualize the layout and design of the photography blog.

# Testing

## Validator Testing

- The project was tested using various validation tools to ensure code quality, performance, and accessibility standards were met.

## Performance and Accessibility

# Technologies Used

## Tools

## Frameworks - Libraries - Programs Used

# Future Plans

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

# Acknowledgements