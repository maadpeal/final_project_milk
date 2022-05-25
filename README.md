# PRODUCTIVITY ANALYSIS IN 'LA MONTAÑA DE CATALUÑA' DAIRY FARM


## Project Overview 

Livestock farming is one of the agrobusinesses that became very important and requires better management of information and data, since very few companies in Mexico take care of this topic. Livestock entrepreneurs must collect information regarding productive, reproductive, agronomic, labor, tax, climate and input purchase management, among others. A milking parlor is a clear example of a highly demanding livestock production system in terms of information management. Said system is normally linked to an automated information capture and collection equipment. Even so, the collection of information by itself does not generate any utility for the company, if it is not analyzed or used for decision-making based on evidence. In this project we will talk about data management in the livestock company and how we can make correct use of them, to improve milking and obtain better monetary results, a longer and better quality life for the animals.

Click this link to check full project presentation in our Google Slides

![5fa2fccaedfc9](https://user-images.githubusercontent.com/96633294/168599396-1a142209-efeb-47b2-bb9b-0fbfa8c9238f.jpeg)


## Why this topic?

We are enthusiasts of livestock knowledge, we are convinced that the quality of life of the animals is linked to a better production of milk and meat. At the same time, we are certain that we can support the growth of this industry by giving visibility to an important part of this industry that, until now, has not been so strong and therefore, the owners of livestock companies have managed empirically.

## Data Set description 

'La Montaña De Cataluña' is an important Mexican company dedicated to the raising and milking of dairy cows, thanks to them we have obtained a database of 4000 aprox daily entries corresponding to each head of cattle reproductive age, pregnancy, level of lactation, daily milk production, milk quality metrics, among others. We will make an analysis of 365 days that corresponds to a year of productive lactation of the cows.

The farmers program for excellence is AFI milk, who share the information with us in .csv format in four different files:

* lactations in progress
* milking process
* mastitis records
* abortion records

![DataSet](https://user-images.githubusercontent.com/96633294/168600785-3c5ab065-c448-4012-9b70-6ff5caef67dd.png)



## Analysis Questions

For 'La Montaña de Cataluña' it's very important to understand some topics in order to improve their functions of veterinarians, keepers and administrators so cow can be as relax as possible that it's one of the most important factors to get more and better milk, and if cow is no more profitable, when it's time to let them go. 
This analysis model will answer questions like: 

* Wich cows are profitable for the next milking cycle?
* When its time to move the cow to another cattle sector?
* The top 20 less profitable/ more profitable cows?
* Wich is the production forecast in liters per cow?
* When is the best season for milking cows?

## Data exploration

LMDC share to us different files for us to dive in. We have 4421 entries corresponding to each live cows that are or will be in the process of insemination, lactation or fattening.

Thanks to the different files received, we entered the files in a .py file to be able to export it in a joint file called full.json from which we were able to obtain different DataFrames where we can work to obtain results such as:

* Lactation summary
* Abortion details
* Mastitis details
* Insemination Bulls details
* Number of inseminations
* Gynecological status

![QuickDBD-export (1)](https://user-images.githubusercontent.com/96633294/170385406-cddd1690-9b1d-4773-a13e-def0f6519d40.png)


## Analysis phase

*INGRESAR AQUI LA DESCRIPCION DELMODELO*

## Technologies Used

### Source Control
Github as code hosting platform.

### Data Cleaning and Analysis
We'll be using Pandas for cleaning, Python and Jupyter notebook will be used to complete the analysis.

### Database Storage
*REVISAR EL HOST DE LA DATA*
AFI milk is our main server where we can extract data. PostgreSQL is the database we intend to use, and AWS for displaying data.

### Machine Learning
*EJEMPLO*

### Dashboard
We use Googles Slides to made this more smooth to get. For the full diplayed and interactive Dasboard we choose Tableau since this is a more friendly way to show clients our product and main results.

Click here to see our full [Technology determination](https://github.com/maadpeal/final_project_milk/blob/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/technology.md) document.

## Machine Learning Model
*DEFINIR QUIEN TIENE MAYPR SEGURIDAD CON EL TOPC*

* Description of preliminary data preprocessing
* Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
* Description of how data was split into training and testing sets
* Explanation of model choice, including limitations and benefits

## Dasboard

Main topics:

*
*
*
*

Description of tools

* bar charts, line charts, pie charts, etc
*

Interactive Elements

*
*
*


We understand that results are the main objective for client. For this reason, we designed the following dashboard that shows the detailed results in a Tableau Story.

Link for the Tableau Story

![Dashboard_draft_poster](https://user-images.githubusercontent.com/96633294/170380021-32c09100-db80-4f25-80e1-68622b99fa0f.png)



## Team Roles and Communication system

Click [here](https://github.com/maadpeal/final_project_milk/blob/26a5ca4b720ce82f8e7eff9bbbd8167b46fe1f48/TeamRoles.md) to see more details about our member roles and communication network.

## Index

To see this repo in a more fun way, please click on any topic in the following index

[Technology determination](https://github.com/maadpeal/final_project_milk/blob/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/technology.md)

[ETL Process](https://github.com/maadpeal/final_project_milk/tree/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/ETL)

[Data set cleaning](https://github.com/maadpeal/final_project_milk/blob/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/Resources/full.json)

[EDA](https://github.com/maadpeal/final_project_milk/tree/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/EDA)

[Model drafts](https://github.com/maadpeal/final_project_milk/tree/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/models)

[Project data and resources](https://github.com/maadpeal/final_project_milk/tree/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/Resources)

[Dashboards and visuals](https://github.com/maadpeal/final_project_milk/tree/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/frontend)


## Glosary

Please click this [Glossary Link](https://github.com/maadpeal/final_project_milk/blob/917ff3d6636bcd8f25e885e6bd1c73f6a9ae9197/Resources/Glosary.md) to learn more about the terms used in this data set



