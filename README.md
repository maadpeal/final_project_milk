# PRODUCTIVITY ANALYSIS IN 'LA MONTAÑA DE CATALUÑA' DAIRY FARM


## Project Overview 

Livestock farming is one of the agrobusinesses that became very important and requires better management of information and data, since very few companies in Mexico take care of this topic. Livestock entrepreneurs must collect information regarding productive, reproductive, agronomic, labor, tax, climate and input purchase management, among others. A milking parlor is a clear example of a highly demanding livestock production system in terms of information management. Said system is normally linked to an automated information capture and collection equipment. Even so, the collection of information by itself does not generate any utility for the company, if it is not analyzed or used for decision-making based on evidence. In this project we will talk about data management in the livestock company and how we can make correct use of them, to improve milking and obtain better monetary results, a longer and better quality life for the animals.

Click this [Link](https://www.canva.com/design/DAFB0Qjk7Lo/8pKShJEnCYx53ELGNgezXw/view?utm_content=DAFB0Qjk7Lo&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) to check our full project presentation slides.

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


![image](https://user-images.githubusercontent.com/96089967/171966907-2a8f5b38-5bf4-4dd9-94ba-c9fc8277138f.png)



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

![db_structure_png](https://user-images.githubusercontent.com/96633294/170385656-a682e705-e7a7-4ad1-bd12-025d9ea6adaa.png)



## Analysis phase

We are using a classification data model so we can analyze if a cow goes above 10,000 liters or below 10,0000 liters during her lactation considering certain criteria so we can predict their 3rd Lactation and optimize our production. 

## Technologies Used

### Source Control
Github as code hosting platform.

### Data Cleaning and Analysis
We'll be using Pandas for cleaning, Python and Jupyter notebook will be used to complete the analysis.

### Database Storage
AFI milk is our main server where we can extract data in .csv format. PostgreSQL is the database we intend to use, and AWS for displaying data.

Database Storare AWS

We created an AWS Database to reach smoothly tha dataset.

![image](https://user-images.githubusercontent.com/96089967/171967067-5c4df73e-86f7-47b7-8d33-fc41f97d2769.png)



![image](https://user-images.githubusercontent.com/96089967/171967342-9bcf32e7-7575-4b9a-a20c-7eb918b8a903.png)



We conected the AWS Database to Postgrest so we can manage the information

![image](https://user-images.githubusercontent.com/96089967/171967199-aeb2492e-a982-41eb-906e-9535c40110ce.png)



### Database Management

We created 8 tables where we storaged all the information that helped us to process the dataset in our model so we can anwser our first quetion.

Which cows are profitable for the next cycle of milking?

![image](https://user-images.githubusercontent.com/96089967/171967610-bfc71dcf-b0fe-4e86-a2a6-cd7def669e7c.png)


Bellow you can see some of our filled tables:

![b-1](https://user-images.githubusercontent.com/96633294/172076002-e29580f8-77b9-4587-9fd0-41b886a757a2.png)  ![d-1](https://user-images.githubusercontent.com/96633294/172076017-877d8929-6872-4058-98f6-1dc9d2d4fc14.png)





### Dashboard
We use Googles Slides to made this more smooth to get. For the full diplayed and interactive Dasboard we choose Tableau since this is a more friendly way to show clients our product and main results.

Click here to see our full [Technology determination](https://github.com/maadpeal/final_project_milk/blob/main/technology.md) document.

## Machine Learning Model

* Description of preliminary data preprocessing

We had to obtain our data from the cows through the AFIMILK database. We cleaned the database, fixed empty spaces, transform dates etc. After that we uploaded our data to PostgreSQL.



* Description of preliminary feature engineering and preliminary feature selection, including their decision-making process

We filtered our data and removed some data that wouldn't help us out with our model because we decided not to take the daily records of the cows. We summarized the data and based on the costs/per litres produced per cow we figured out that in order to make a profit with a cow she has to produce above 10,000 liters per lactation. 

* Description of how data was split into training and testing sets

We used the tools and what we learned in class plus we made a new column "objectives" to help us out find out if a cow made above 10,000 liters or below 10,000 liters in her 3rd lactation and after that we made our split.

* Explanation of model choice, including limitations and benefits

We used a classification model decision tree because we found it very helpful to code and construct our final objective. It helped us find out if a cow was profitable or not. 

## Dashboard

Main topics:

* Average Days in milk
* Cows per gynecological status
* Top 20 best and worst cows in cattle
* Best lactations

Description of tools

* bar charts
* line charts
* pie charts
* interactive bar charts

Interactive Elements

* Top best and worst cows selector
* Pop Up labels
* KPI selector

We understand that results are the main objective for client. For this reason, we designed the following dashboard that shows the detailed results in a Tableau Story.

[Link for the Tableau Story](https://public.tableau.com/views/PRODUCTIVITYANALYSISINLAMONTAADECATALUADAIRYFARM/Finalhistory?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link)


![preliminary dashboard](https://user-images.githubusercontent.com/96633294/172073474-ac38f710-fe60-493d-b257-d08a1c889c69.png)



## Team Roles and Communication system

Click [here](https://github.com/maadpeal/final_project_milk/blob/Repository/TeamRoles.md) to see more details about our member roles and communication network.

## Index

To see this repo in a more fun way, please click on any topic in the following index

[Technology determination](https://github.com/maadpeal/final_project_milk/blob/main/technology.md)

[ETL Process](https://github.com/maadpeal/final_project_milk/tree/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/ETL)

[Data set cleaning](https://github.com/maadpeal/final_project_milk/blob/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/Resources/full.json)

[EDA](https://github.com/maadpeal/final_project_milk/tree/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/EDA)

[Model drafts](https://github.com/maadpeal/final_project_milk/tree/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/models)

[Project data and resources](https://github.com/maadpeal/final_project_milk/tree/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/Resources)

[Dashboards and visuals](https://github.com/maadpeal/final_project_milk/tree/61adb0614722dd872fa2e7f4b1edca5c0dd10e9c/frontend)


## Glosary

Please click this [Glossary Link](https://github.com/maadpeal/final_project_milk/blob/917ff3d6636bcd8f25e885e6bd1c73f6a9ae9197/Resources/Glosary.md) to learn more about the terms used in this data set



