
* To do: Add in responsive mock up
* To do: spell check through grammarly
* To do: Fix missing line spaces
* To do: Consider rename to ADHD Superpowers (from ADHD Superheros)

# ADHD Superstars

 ![Mockup of app across different screen sizes](assets/images/responsivemockup.png)

## Overview:

To create an app that encourages a positive mindset in the ADHD user by focusing on strengths and successes as well minimizing cognitive overload by narrowing focus on the top 3 most important tasks for the day. 

### Purpose: 

* What? 

1. ADHD is a neurotypical developmental disorder characterised by an impairment of executive function (mental processes used to managing day to day life and attaining goals). ADHD Ireland (https://adhdireland.ie/for-adults/adhd-in-adults/) share that adults with ADHD have problems in six major areas of executive functioning:

    * Activation – Problems with organization, prioritizing, and starting tasks.
    * Focus – Problems with sustaining focus and resisting distraction, especially with reading.
    * Effort – Problems with motivation, sustained effort, and persistence.
    * Emotion – Difficulty regulating emotions and managing stress.
    * Memory – Problems with short-term memory and memory retrieval.
    * Action – Problems with self-control and self-regulation.

* Why? 

1. Encourage a positive mindset at the start of the day - People with ADHD are neurodivergent individuals living in a neurotypical world. The world in general celebrates and rewards neurotypical traits which can leave ADHDers to dwell on their perceived weaknesses, shortcomings and failures. 

2. Optimise Daily Life while reducing cognitive overload - Apps recommended for people with ADHD are often focusing solely on organising their daily lives such as this ADHD app list here of calendars and to-do list apps but none are uniquely designed for ADHDers: https://www.additudemag.com/mobile-apps-for-adhd-minds/

* How? 

1. Focus on the positive - This app shifts the users focus on celebrating ADHD strengths and successes rather than dwelling on weaknesses and failings. 

2. Reduce cognitive overload - It uses the core function as a restrictive to-do list feature (top 3 daily priorities rather than an endless list of to-do items) to encourage hyperfocus while reminding the users of the amazing their amazing potential, key ADHD strengths and significant past successes/wins.

## UX

### User Stories

Agreed:

* As a user, I need to see a daily reminder of a ADHD superpower/strength.
* As a user, I need to see a daily reminder of advice tailored to ADHDers.

* As a user, I need to review my top 3 priorities from the yeserday day and confirm done/not done.
* As a user, I need a weekly % of my task completion (one week = 21 tasks, 16 done on the day = 76%). 
* As a user, I need a monthly % of my task completion (one month = 90 tasks, 79 done on the day = 86%).

* As a user, I need to document my top 3 win/successes from the yesterday day.
* As a user, I need to be reminded of random wins/successes from any previous day except yesterday.
* As a user, I need to set my top 3 priorities for the current day.

To be considered:

* As a user, I need to be require to document examples of how I used my ADHD superpower/strength.
* As a user, I need an email reminder midday of my top 3 priorities for today to help me refocus

### Process Map

#### Main Menu Flow:

 ![Process map of main menu](assets/images/mainmenu.png)

#### App Flow:

 ![Process map of app](assets/images/processmap.png)

### User Story Testing

To do: Add examples of user stories as features including screenshots

## Bugs

## Technologies

### Languages Used

* [Python](https://www.python.org/)

### Libraries and Programs Used

#### Programs Used

* [Git](https://www.atlassian.com/git) - used for branching, merging, and rewriting repository history.

* [GitHub](https://github.com/) - used a hosting service for Git repositories.

* [Gitpod](https://gitpod.io/) - used as a workspace for Git repositories.

* [Google Sheets](https://www.google.com/sheets/about/) - used to store user information (wins, strenghts, priorities).

* [Heroku](https://www.heroku.com/) - used to deploy project. 

* [Lucidchart](https://www.lucidchart.com/) - used to create flow charts. 

* [Am I responsive](http://ami.responsivedesign.is/) - used generate responsive mockup image at the top/beginning of the README.

* [Microsoft Photos](https://www.microsoft.com/en-us/p/microsoft-photos/9wzdncrfjbh4?) - used to resize images.

#### Libraries Used

* [Gspread](https://docs.gspread.org/en/v4.0.1/) - used API to enable python to access google sheets. 

* [Time](https://docs.python.org/3/library/time.html) - used create pauses (in seconds) between print statements. 

* [Os](https://docs.python.org/3/library/os.html) - used to create a function that clears screen for user. 

* [Datetime](https://docs.python.org/3/library/datetime.html) - used to create calculations of date ranges in functions.

* [Pyfiglet](https://pypi.org/project/pyfiglet/0.7/) - used to render a string as a ASCII text. 

* [Colorama](https://pypi.org/project/colorama/) - used to add color to text styling of print statements.

* [Smtplib](https://docs.python.org/3/library/smtplib.html) - used to create a function that sends email.

## Testing

### Validators

### Compatibility

### Responsiveness

### User Story Testing

## Deplpoyment

### Local Deployment

In order to make a local copy of this repository, you can type the following into your IDE terminal:_

- `git clone https://github.com/declanosullivan/ADHD-Superstars.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/declanosullivan/ADHD-Superstars)

Sending emails within this Python application:

**NOTE**: If receiving errors while sending emails using this app, due to Google's security feature with **2-Factor Authentication**, **Less Secure Apps**, and **DisplayUnlockCaptcha**, you'll need to follow these steps.

- Turn **Off** [2-Factor Authentication](https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome)
- Turn **On** [Less Secure Apps](https://myaccount.google.com/lesssecureapps)
- Turn **On** [DisplayUnlockCaptcha](https://accounts.google.com/DisplayUnlockCaptcha)

It's highly recommend to create a secondary Google account for this purpose, instead of using your actual account (to keep your actual account secure!). This is purely used for sending emails to the user from this application.

## Credits and Learning Experience

### Content

### Media

### Acknowledgements