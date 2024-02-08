This python project is designed to automate the creation of a budget by filling in a simple CSV file with two columns of data.

The simple data entry is designed to be very flexable. When entering the Raw data this way, a template can be created to quickly fill in new data. 

Project Goals:


## Easy data entry to start. 
* New cost or income, just add a line anywhere in the form.
* Cost items start with cost_.
* Income items start with income_.
* Savings are defined by savings_ and goal_. 
* Define hourly or annual income.
* Income from multiple sources are supported. 
* Costs can be lumped into one or spread out. 
    * key words may be defined and added too. 

## Easy to read output. 
* Using pandas and excelwriter to output an easy to read and understand excel file.
* Other formats, including auto upload into google docs.
* Automated output, if data is manually added tothe excel file it will still update in line. 

# TODO

## Integrations with personal products via optional API calls.

## Website Interface via Flask webportal

## Database integration with SQLAlchemy instead of csv file.

## 


