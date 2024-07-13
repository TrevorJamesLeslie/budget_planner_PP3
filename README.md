# Budget Planner $$$

![Am I responsive](readme_documents/responsively-screenshots/Am_I_responsive_main.png)

Visit the deployed site here: [Budget Planner](https://budget-planner-ef48562f3908.herokuapp.com/)

This appliation is designed to track budget .... 

## User Experience/User Interface (UX/UI) 

### User Stories

**As a user, I:**

- Want the quiz to be responsive to my devices.
- Want clear instructions on how to navigate through the quiz.
- Want to know how many questions there are.
- Want to know if I selected the correct answer.
- Want to get help if I am stuck on a question.
- Want to be able to reset the quiz if I made a mistake.
- Want to know what question number I am on during the quiz.
- Want to know my score during the quiz.
- Want to know what the correct answer is if I selected the wrong answer.
- Want to know my final score.

### First Time Visitor Goals

1. Understand the main purpose of the site and learn about the Friends trivia quiz.
2. Navigate the site easily to start the quiz or learn more about it.
3. Experience a flashback into the show's great moments.

### Returning Visitor Goals

1. Access new or updated quiz questions.
2. Switch off from everyday life and have fun.
3. Check for any new features or updates related to the quiz.

## Design   

Entire program is displayed in CLI(Command Line Interface). Application allows to display window of 80 characters long and 24 rows down with a vertical scrollbar.

<br>

# Project Creation Process

## Planning 

- **Flowchart :** bla bla

- **Google API SetUp :**   
Prior to starting any program function code, the relevant Credentials and API set up needed to take place. This process is detailed in the [Creation & Deployment](#creation--deployment) section. Security was an important factor with the connecting of a Google Account (one that I created solely for the project) to access the Google Sheets worksheet. Steps were followed carefully to ensure that no important files like, `CREDS.json`, were pushed to the cloud for the public to view. Guidance for the setting up of these authorisations and credentials, was provided through the Code Institute's Full Stack Software Development course.

- **Google Sheets :**
was used to store any entered user data and called upon when data was manipulated and updated. It was used to simulate a database, as the user will have no direct interaction with the actual worksheets. All data entry and manipulation takes place within the terminal. 

Clear instructions are printed in the terminal instructing the user in how to enter the data, so that it may be displayed correctly on its output, within the scope of this project. For future development,  

## Python Logic  
With this being my first Python project, my main goal was to create an application that accessed, displayed and edited data successfully from Google Sheets worksheets; to simulate a database. I will admit that my Scope for this project was regularly adjusted when my simultaneous learning of the gspread library reached it's limits in what I could create. Reminding myself to consider the MVP kept me on track.

I began by creating simple functions which pushed the flow of user input through the application. Menus were created using if/elif statements and user input was validated using while loops and try/except statements. 

From these initial menus, smaller functions were added that controlled the movement and manipulation of data. Functions containing enumerate() were essential in pulling the data from specific matched locations in the worksheets, once the user's input was validated to be present within the worksheets. I constantly tested the validation functions throughout the project build so that I would not be left with gaps in the flow of the application. 

Once I confirmed one section's function to be successful, I investigated whether the code could be reused in other sections with similar purposes. In some instances it could, once the data handling remained the same. In other situations, code was personalised for the individual function, particularly in how the data was displayed. Parallel iteration using the python zip() function was needed in displaying Batch and Inventory data, whilst Sales Data was displayed using the Python '\t' whitespace character. This gave space between each item in the Sales Data sheet, when represented in the terminal.   
    *Welcome Page Message*
    - ![View](readme_documents/visual_page_1.jpeg)

<br>

# Features

## How to Use Budget Planner

### Main Menu  
After the opening screen of BakeStock ASCII art, the user is greeted by the below menu. Users may enter the number displayed beside the menu options. Any input not connected to the menu choices will be confirmed as invalid and the user is prompted to enter a numbered menu option.
![Main Menu screenshot](documentation/readme/main_menu_f.png)  
  
    
### Sales Menu    
Similar to the opening menu, the user is prompted to enter their menu option choice. The user is informed of any invalid input and prompted to try again.
![Sales menu screenshot](documentation/readme/sales_menu_f.png)
  
  
### Sales Figures   
Sales figures are printed to the terminal and are as current as the data that is stored in the Google Sheet. The data will refresh during the user session if they choose to add any sales figures at the end of the day. If the Sales Worksheet is refreshed, then a Yellow text warning is displayed to the user informing them of 'No data' available, incase the user is thinks that the program has stalled in its data display. The user can return to the Sales Menu by following the instructions to enter 's'.
![Sales figures screenshot](documentation/readme/sales_figs_f.png)  
  
    
### Records Sales Figures  
The user is prompted to enter the Sales figures by first entering the date and the abbreviated baked items. This is done so that the Sales table will display correctly in the terminal and allows different baked items to be recorded daily. Further learning of data formatting, for future versions, will allow me to remove the abbreviated restriction for the user so that the data displays with full words. Data entry is restricted to 9 columns within the worksheet to assist in the Sales display. The user is informed of this if they exceed the value restriction.
<details open>
<summary>Records Sales Figures Feature</summary>
<img src = "documentation/readme/record_sales_f.png">
</details>  
  
### Clear Sales Data  
The user is prompted to enter the words 'CLEAR DATA' exactly as displayed if they wish to clear the Sales worksheet. Again, user input validation has been very important here to ensure no actions are executed if the user did not intend for them. Several steps of input are required to ensure no mistakes are made.
<details>
<summary>Clear Sales Figures Feature</summary>
<img src = "documentation/readme/clear_f.png">
</details>  

### Batch Numbers  
Batch numbers are displayed beneath the Batch menu banner. A yellow text warning alerts the user that the batch quantity consists of 12 items. 
<details>
<summary>View Batch Numbers Feature</summary>
<img src = "documentation/readme/batch_nums_f.png">
</details>   

### View Batch Menu  
Users are greeted with the Batch Menu providing several options.
<details>
<summary>Batch Menu Feature</summary>
<img src = "documentation/readme/batch_menu_f.png">
</details>   
 
### Add Item, Change Item, Update Item, Clear Item in Batches  
 Multiple options are provided to allow for customisation by the user. The Flavours/Items section is editable by the user to allow for different baked items everyday. Similar to making a to-do list in a notebook, the baker/user can update the required batch numbers at the end of the day, ready for the next baking day. When they complete a batch, these numbers can be edited back to zero to reflect this. This gives the baker real-time information on what is left to do every time they view the batch numbers.
<details>
<summary>Add, Change, Update, Clear Batch Item</summary>
<img src = "documentation/readme/enter_newb_f.png">
<img src = "documentation/readme/change_batch.png">
</details>

### Ingredient Inventory  
Following a similar UI from the earlier Menu options, the Inventory displays the current stock levels. 
<details>
<summary>Ingredient Inventory Feature</summary>
<img src = "documentation/readme/ing_view_f.png">
</details>   

### Inventory Menu  
Users are greeted by an Inventory Menu providing several options.
<details>
<summary>Inventory Menu Feature</summary>
<img src = "documentation/readme/ing_menu.png">
</details> 
  
### Add Item, Change Item, Update Item, Clear Item in Inventory  
These items are customisable with an 'Ingredient' section for displaying the ingredient name and unit in brackets. The 'Quantity' value is numerical only and may be updated when bakes have been processed. Similar to the Batch menu, the UX prompts, validates and acts on user input.
<details>
<summary>Add, Change, Update, Clear Inventory Item</summary>
<img src = "documentation/readme/add_ing.png">
<img src = "documentation/readme/change_ing.png">
</details>  

### Exit  
Some users may like to have an option to feel that they have exited the program. Although it's function is very minor, I felt that it was important to include and to thank the user for using BakeStock.
<details>
<summary>Program Exit</summary>
<img src = "documentation/readme/exit_f.png">
</details>   
 

-----  

<br>

## Future Enhancements

- **Year :** Adding a year
- **Multiple Users :** 
- **Aesthetics:** A visually appealing 
- **Aesthetics and functionality :** Connecting with other librarie for faster response and nicer look.

-----  

<br>

# Languages and Technologies Used 
   - Python  
   - HTML5, JavaScript - provided within the Code Institute's [Python Essentials template](https://github.com/Code-Institute-Org/python-essentials-template) 
   - [Lucidchart](https://www.lucidchart.com/pages/) - used to create the flowchart needed during project planning.
   - [GitHub](https://github.com/) - used for hosting the program's source code.
   - [Gitpod](https://www.gitpod.io/) - used as a workspace for developing the code and testing the program.
   - Git - used for version control.
   - [Google Sheets](https://docs.google.com/spreadsheets/) - used for storing edited and saved user data.
   - [Google Cloud Platform](https://cloud.google.com/) - used to provide the APIs for connecting the data sheets with the Python code.
   - [Heroku](https://heroku.com/apps) - used for deploying the project.
   - [PEP8 Validator](https://pep8ci.herokuapp.com/#) - used for validating the Python code.
   - [Tiny PNG](https://tinypng.com/) - used to compress images.
-----  

<br>

# Libraries & Packages 
   - **gspread** - gspread was imported and used to add, remove and manipulate data in the connected Google Sheets worksheets.  

   - **google.oauth.service_account** - This library was used for the authentication needed to access the Google APIs for connecting the Service Account with the Credentials function. A `CREDS.json` file was generated from this with the details needed for the API to access my Google account which holds the Google Sheets worksheet containing the applications data. When deploying to Heroku, this information is then stored in the config var section to ensure the application will run.  

   - **time & sys** -the time & sys libraries were used for the text-typing effect for typePrint and typeInput statements to create a visual effect 0f the text appearing on screen in real time.  

   - **os** - os library was used to add the clearScreen() function to assist in creating a neater flow from Menu options by clearing the screen for the user's choice from the Menu to be displayed. 


-----  
<br>

# Testing  
I have created an additional file for my Manual Testing and Validation this can be found here: [TESTING.md](/TESTING.md)

### Code Validation


### Known Bugs / fixed bugs 
- #### No known bugs recorded at the end of the project.
  Many of the issues I had found were simple semicolons or naming mistakes and some were as complicated as function being connected incorreclty. Once one bug was fixed another appeared which made the learning really deep.
  Many bugs during the process of making it abd to list them all would be a challenge. The main issue I had was with answerr button colors and hint and had used tutor support on this ocassions. 
  The score wont load properly - function issue, naming was incorrect.
  Colors on the correct / incorrect buttons wont apply properly - I was targeting answer buttons not buttons individually.
  Buttons wont apply correct colors - Changed accepthing answers tio true, used const not let  
  Colors apply but on background not buttons - solved with tutor help, parent element was the issue, 
  Color worked but not always - it was spotted by tutor , mouse was still hovering over it - disabled mouse afetr the answer was made. 
  Hint messsage was not clearing - hint name was chaged to a fixed name , but after the call with mentor I got a great advice to change the whole naming and and separate icon with a span. 



# Setting up & Deployment    
  
The below steps to creating and setting up a new Python workspace and API credentials has been guided by and adapted from the [Code Institute's](https://codeinstitute.net/ie/) Python walkthrough project 'Love Sandwiches'. Please check each step is relevant to your project needs and change the data entered to suit it.

### Creating a new repository 
<details open>
<summary>Steps to create a new repository.</summary>  

The [Code Institute's Python Essential Template](https://github.com/Code-Institute-Org/python-essentials-template) was used to create a terminal for my Python file to generate it's output. To use this template, please follow these steps:
1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above Python template repository.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the green '**Gitpod**' button to generate a new workspace.   

</details> 
  
-----  
### GitHub Pages

The project was deployed to GitHub Pages using the following steps:

1. Log in to GitHub and locate the [Friends_Trivia Repository](https://github.com/monika-mak/Project_Portfolio_2-Friends_Trivia).
2. At the top of the Repository (not top of page), locate the "Settings" button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" section.
4. Under "Source," click the dropdown called Source is set to 'Deploy from Branch' and select "main."
5. Make sure the folder is set to / (root).
6. Under Branch, click Save. The page will automatically refresh.
7. Scroll back down through the page to locate the now published site [Friends Trivia Quiz](https://monika-mak.github.io/Project_Portfolio_2-Friends_Trivia/) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [Friends_Trivia Repository](https://github.com/monika-mak/Project_Portfolio_2-Friends_Trivia)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Activating the Google Drive & Sheets API
<details>
<summary>Steps to activate the APIs</summary>
To access the data in a Google Sheets worksheet using Python code, an API is required. Please follow these steps to set up your APIs:  

1. Navigate to the [Google Cloud Platform](https://cloud.google.com), using an email address/Google account that is registered to you alone.
2. In the Google Cloud Platform Dashboard, create a new project by clicking on the '**Select a Project**' button and choosing the '**New Project**' option. Give your new project a name and click '**Create**'. (Your access credentials are unique to each project, so create a new project for every project that you build.) 
3. Click '**Select Project**' in the blue banner to bring you to your project page.
4. Select '**APIs and Services**' from the left side menu, then select '**Library**'.
5. Use the search bar to search for the two APIs needed for this project, Google Drive API and Google Sheets API. One at time, choose the APIs from the search and click '**Enable**' on their main page. Follow the below steps for the Google Drive API, but only click '**Enable**' for the Google Sheets API. There is no need to download credentials again for it.
6. On the API overview page, click '**Create Credentials**' to generate some credentials which will allow us access to our Google Drive from our Python code.
7. Fill out the forms fields and dropdown menus with the information that is relevant to your project. For mine, I chose **Google Drive API -> Application Data -> No, I'm not using them** (regarding using Kubernetes, App Engine etc)
8. Under Service Account Details, choose a Service Account name and click '**Create**'.
9. In the Role Dropdown box choose **Basic -> Editor** then press '**Continue**'. Click '**Done**' to finish the form if you do not need to grant users access to the service account if it is a personal project.
10. On the next page, click on your new Service Account that has been created, then click on the '**Keys**' tab to '**Add Key**'. Select '**Create New Key**'.
11. Select JSON and '**Create**'. Your json file containing your API credentials will be downloaded to your machine.

</details>

-----  

### Setting up the Gitpod workspace for the APIs
<details>
<summary>Steps for workspace setup</summary>
  
1. In the new Gitpod workspace you've created with the Python Essentials template, click and drag the json file that you created in the above steps, into the Gitpod workspace.  
2. Rename it to `CREDS.json`, if you wish, and open the file. Find the client_email address you previously entered, copy it without the quotes around it.
3. In the Google Sheets file that you have created for this project, click the '**Share**' button and paste the email address into the field, choose '**Editor**', untick '**Notify People**' and click '**Share**'. This allows our project access to the spreadsheet.
4. To ensure the private credentials that you have created do not make their way to the cloud for others to view, add the `creds.json` file to your `gitignore` file before you commit any changes to your repository, and push them to the cloud.
5. Use the command `git status` to check that the `creds.json` file is not staged to be committed.

</details>  
  
-----  

### Initial Code for connecting to our API with Python
<details>
<summary>Steps to including the Python/API connection code</summary>

1. The code needed to ensure your APIs connect correctly can be found at the top of the `run.py` file connected to this project. It is important that you remember to pass the exact same name as your spreadsheet to the `SHEET = GSPREAD_CLIENT.opn('your-filename-here')` code, or else gspread will throw an error.
2. The command `pip3 install gspread google-auth` is needed to install the gspread package for handling the worksheet data and the google-auth package to allow access to the Google Sheets account via the Credentials we downloaded earlier. Use the above command in the Gitbash terminal to install.
3. Please refer to the `run.py` file for the import, SCOPE, CREDS, SCOPED CREDS, GSPREAD CLIENT, SHEET code that is needed to connect the APIs and change any data that is personal to your project.

</details>
  
-----  

### Deploying to Heroku  

Heroku has been used to deploy this project as Python is used as a back-end language. To allow for accurate testing, I deployed the project to Heroku early on using Automatic Deployment to update the program everytime new code was pushed to my GitHub repository. Here are the steps that I followed to set my project up, guidance was provided by the [Code Institute's](https://codeinstitute.net/ie/) 'Love Sandwiches' project.     

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
<details>
<summary>Create new app</summary>
<img src ="documentation/readme/heroku_1.png">
</details>  

3. Enter an app name and choose your region. Click '**Create App**'.
<details>
<summary>Enter app name</summary>
<img src ="documentation/readme/heroku_2.png">
</details>  
  
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. In KEY enter `CREDS`, in VALUE, paste in the text content of your `CREDS.json` file. Select '**Add**'.  
5. Repeat this process with a KEY:VALUE pair of `PORT` and `8000`.
6. In the Settings tab, in the Buildpack section, click '**Add Buildpack**', located near the bottom, right of the refreshed screen. One at a time, choose the '**Python**' pack, save changes, then choose the '**NodeJS**' buildpack and save changes. **NB: the Python buildpack _must_ be above the NodeJS buildpack.**
  
<details>
<summary>Choose Buildpacks</summary>
<img src ="documentation/readme/heroku_bp.png">
</details>  
  
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9. Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Automatic' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site.

  
-----  


## Credits

### Idea

The idea for this project came from actual need of knowing our houshold budget. It was atask that I had put off for way too many years (to be honnest). 
Fun Fact: Even knowing this could be a great use of the project, part of me was resistant... I knew what was coming $$$. I am happy that I  have took on this challenge though.  

### Content

Content was inspired mainly by the tutorials below:
- **Code Institute** Love Sandwiches Project Walkthrough 
- [BakeStock](https://budget-planner-ef48562f3908.herokuapp.com/)
- [bla bla ](https://www.youtube.com/watch?v=rFWbAj40JrQ&list=PLB6wlEeCDJ5Yyh6P2N6Q_9JijB6v4UejF)
- [Amy Richardson's README](https://github.com/amylour/BakeStock/blob/main/README.md) Thank you Amy!

### Learning and Support Resources

- [Code Institute](https://codeinstitute.net/) - Main source of information, structure and support learnings.
- [W3Schools](https://www.w3schools.com/) - 
- [YouTube](https://www.youtube.com/) - To source a deeper understanding.
- [ChatGPT](https://openai.com/chatgpt) - quick inforamtion when needed,loved using it to understand concepts, found very useful when prompting("explain as if to a 10 year old").quick information support when needed.

- [SoloLrarn](https://www.sololearn.com/en/) - Python constant practise.
- [Study Music, Concentration, Focus](https://www.youtube.com/results?search_query=study+music+concentration+focus) - To keep me calm during work.

### Acknowledgements

A massive shout-out to:

- Amy Richardson again, thank you for your constant support as well as great advices and tips given throughout the process.
- Femi - my mentor who utilized our meetings very well, giving constructive feedback and excellent practice, your feedback is always very powerful and to the point.
