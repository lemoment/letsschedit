# Let's Sched It  
We wanted to make scheduling easier. So we created Let’s Sched It, a free service that helps you find the best time for a group to meet, conveniently. Instead of making users input their availability, we utilize Google and Outlook APIs in order to connect user’s calendars and import their events, saving them the time they’d spent cross-referencing.  

Consider a situation where a student is working on a team project and needs to coordinate with their classmates. The group all has their calendars setup using a service like Google Calendars but has been texting back and forth sharing their free times, only to get lost in the fray. Enter Let’s Sched It, which allows lets people schedule meeting with only a calendar link and a quick click to log in.

![Mockup](documentation/Mockups/Desktop-Home-LeavesHalf.png)

Created by Riya Aggarwal, Elias Gabriel, Maalvika Bhat, and Dieter Brehm.

## Installation & Setup
![AR Diagram](documentation/arch-diagram_20190409.png)

You can setup the server component by running
`cd source/api`, then `pip install -r requirements.txt` to install required libraries which are:  

### Backend - Deps  
* Flask  
* Requires  

### Frontend - Deps  
* vue js  
* eslint  
* babel  
* parcel  

The front end can be setup by running
`cd source/web`, then `npm install`

## Usage  
* For the frontend: run `cd source/web` and then `npm run dev`  
* For the backend:  run `cd source/api` and then `python app.py`

## Demo

## Implementation Details  
<insert document>

## Privacy and Impact of Software
The primary source of possible ethical dilemmas we had to be cautious about in this project is privacy and user data handling. While we made an attempt to mitigate this potential issue by modeling our system to be calendar centric instead of user-centric, we do acknowledge that we collect users’ free time blocks through Google and Outlook API’s. The process of logging into the app does, however, clearly indicate the permissions and information being given to us through Google and Outlook.    
  
## Our Journey  
  
## Attribution   
  
