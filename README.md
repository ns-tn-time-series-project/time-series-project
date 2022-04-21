# Time Series Project - Superstore Dataset

### Project Description:
- The marketing team for our superstore is looking to lanch a new marketig campaign soon as has asked the data science department to analyze the company's customer and order data to help them develop an effective campaign. They have asked our department to recommend specific target areas or target groups to focus on with their project.

### Project Goals:
- Goal 1: Identify marketing targets within the company's product lines

- Goal 2: Identify marketing targets within the company's customer base

- Goal 3: Make marketing recomendations from the results of our analysis

- Goal 4: Provide insight to next steps for target exploration and marketing focus

### Data Dictionary:

| Variable | Meaning |
|----------|---------|
|order_date|the date that an order was placed|
|ship+date|the date the order was shipped to the customer|
|sales|the sales value in us dollars of the order|
|quantity|the number of a specific product that was included in the order|
|discount|the percentage of discount applied to the specific order in decimal format|
|profit|the profit value in us dollars from the specific order|
|cust_name|the full first and last name of the customer associated with the order|
|prod_name|the full name of the product|
|ship_time|the time in days between when the order was placed and when the order was shipped to the customer|
|unit_cost|the cost of the product to the company in us dollars calculated by subtracting the profit value from the sales value|
|profit_margin|calculated by dividing the profit value by the sales value minus the discount given|
|revenue|calculated by subtracting the discount value from the sales value|

### Project Planning:
- First, write a function to pull the correct dataset from the database and save it as a csv in the local directory.

- Save the data acquision function in a seperate acquire.py file for future use

- Then, write a function that prepares the data by dealing with missing values, removing unneeded columns, renames columns, and creating engineered feature columns

- Save the data preparation functions in the acquire.py file for later use

- Explore the data by visualizing key features related to the questions and how they relate to sales or profit values

- Continue to explore the data by running statistical tests to verify statistical significance of the relationships between the variables

- Document initial takeaways from the data exploration

- Analyze the data groups informed by initial exploration to determine targets for the marketing team

- Document key findings, recomendations, and next steps

### How to Reproduce this Project and Findings:

To reproduce my findings on this project you will need:

- An env file with you own credentials (hostname, username, password) to access the database and pull the superstore dataset

- The acquire.py file in this repository that contains all the functions used to acquire, prep, and wrangle the dataset

- The jupyter notebook in this repository named "final_report_time_series_project" which contains the code used to produce the project.

- Libraries used are numpy, pandas, seaborn, sklearn, scipy, and matplotlib. All imports are included at the top of the notebook.

### Summary:

- 

- The Central region should be a priority for marketing efforts since we have seen the largest decrease in sales and order value in that region

- Segmented customer groups were identified using a RFM Analysis for use with targeted marketing strategies

- Customer groupings resulting from the analysis are available as a csv file for use by the marketing department

### Recomendations:

- 

Recomendations based on customer research

- Customers with a "Top Customer" or "High Value Customer" rating are our best customers and would most likely respond well to marketing focused on loyalty programs or early access to new products

- Customers with a "High" frequency rating may not be the highest spending customers but they make purchases most often and would most likely respond well to marketing focused on free shipping or similar offers

- Customers with a "High" monetary rating are our big spending customers and will most likely respond to marketing focued on luxury offers or higher level subscription tiers

- Customers with a "High" recency rating have made an order with us in the last 6 months so we are on their mond and we should focus marketing on keeping us on their mind with new peodut anouncements or recomendations based on their recent purchases

- Customers with a "Low" recency rating have not made an order with us in the last year and are at risk of not coming back. they should be targeted with marketed focused on retension such as discount pricing or with specific customer engagement efforts

### Next Steps:

- 

- If we had more time to analyze customer groups we would conduct a RFM analysis on the other 3 regions to identify focus groups for targeted marketing in those regions
