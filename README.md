# Todooli

## Summary

1.  Database Schema Mapping
2.  About Todooli - The Online Task Management Tool
3.  Features
4.  Dependency Packages Installation Guide & Database Configuration Guide

- Packages
- Database Configuration

5.  Purpose and Initial Goal
6.  Achieving a Secure and User-Friendly Task Management Experience with Todooli
7.  Usefull link
8.  Design and User Experience
9.  Example User Account
10. GitHub

## Database Schema Mapping

![uml](https://user-images.githubusercontent.com/96482486/215269050-591ee74d-9ca2-4e19-9299-e17e0bed89e0.png)

## About Todooli - The Online Task Management Tool

Todooli is an online task management tool designed to help individuals and small businesses stay organized and on top of their tasks. With Todooli , users can create tasks, set deadlines, and track their progress in real time. It also provides a range of other features such as task reminders, and task notes. Todooli is easy to use and provides an intuitive interface that makes it simple to get started with task management. It will also integrates other services such as Google Calendar, Trello, and Slack, allowing users to sync their tasks across multiple platforms.

## Features

Todooli offers a range of powerful features to help you manage your tasks and stay organized:

- Task Management: Create, update, and manage your tasks with ease
- Profile Management: Update your profile information and settings for optimal use
- Tag Creation: Create custom tags to filter and categorize your tasks
- Performance Tracking: Track your progress and see your performance over time
- Article Section: Learn new tips and tricks to make the most of Todooli
- And much more!

## Dependency Packages Installation Guide & Database Configuration Guide

In this section, we will provide the steps necessary for installing the required packages for Todooli, as well as configuring the database.

### Packages

The following packages are included:

- crispy_form
- pillow
- django-recaptcha
- django-dotenv
- six

To install these packages, simply run the following command in the correct directory:

    pip install -r requirements.txt

To know, Todooli is using a custom Bootstrap

### Database Configuration

To set up the database for Todooli, follow these steps:

1. Run the following command to apply database migrations:

   - **python manage.py makemigrations**

2. Run the following command to apply the database migrations:

   - **python manage.py migrate**

3. Create a superuser to access the administrative interface of Todooli:
   To configure the database for Todooli, follow these steps:
   - **python manage.py createsuperuser**

## Purpose and Initial Goal

The Todooli project was created with the goal of providing individuals and small businesses with a user-friendly and intuitive task management tool. This project was also an opportunity for the developers to practice and showcase their skills in Django, a popular web framework. The initial objective was to create a functional task management tool that includes key features such as task creation and task tracking. The Todooli team aimed to create a tool that is both efficient and easy to use, helping users to stay organized and on top of their tasks.

## Achieving a Secure and User-Friendly Task Management Experience with Todooli

However, we also had a strong emphasis on creating a secure and safe platform for users. Our app ensures that each user only has access to their own data and data shared with them, making it a reliable tool for managing tasks and collaborating with team members.

One of the challenges with using profile images in the Todooli app is ensuring the images are properly formatted and sized. To solve this issue, Todooli has implemented image validation checks to ensure that only images of the correct format are uploaded. If a user updates their profile image, the previous image will be deleted to ensure efficient use of storage space. Todooli also resizes the images to ensure that they are optimized for display on the app. These steps help to ensure a smooth and seamless experience for users when uploading and updating their profile images.

## Usefull links

For a comprehensive guide on using Todooli, please follow these link:
https://on1zuma.pythonanywhere.com/article/use-it/

- Home Page: https://on1zuma.pythonanywhere.com
- My Profile: https://on1zuma.pythonanywhere.com/user/profile/
- Register: https://on1zuma.pythonanywhere.com/user/register/
- Login: https://on1zuma.pythonanywhere.com/user/login/

## Design and User Experience

Todooli's user interface and design were carefully crafted to provide a seamless and intuitive experience for users. Our team used Figma, a popular design platform, to create wireframes and models that were used to inform the design and styling of the website. This allowed us to create a visually appealing and user-friendly interface, making task management simple and enjoyable for our users.

**Figma link (Experimental Area for Different Styles) :[ Figma mockup ](https://www.figma.com/file/b8RfYMbwV21XCVWQGAJTM6/Ilonii?node-id=0%3A1&t=cl5h4CJSBJ7ocoXh-1)**

### Example User Account

- Username : Moli
- Password : http://127.0.0.1:8000/user/register/

## GitHub

**GitHub link :[ GitHub ](https://github.com/On1zuma/Todooli)**
