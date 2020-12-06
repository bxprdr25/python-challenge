# convert and export the data to use the following format instead:
#
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA

# In summary, the required conversions are as follows:
#
# The Name column should be split into separate First Name and Last Name columns.
#
# The DOB data should be re-written into MM/DD/YYYY format.
#
# The SSN data should be re-written such that the first five numbers are hidden from view.
#
# The State data should be re-written as simple two-letter abbreviations.

import os
import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

employee_csv = os.path.join(".", "Resources", "employee_data.csv")
output_file = os.path.join(".", "Resources", "emp_data_revised" + ".csv")

with open(output_file, 'w') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow(['Emp ID', 'Name', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    with open(employee_csv) as csvfile:
        csv_reader = csv.DictReader(csvfile)

        print('Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State')

        for column in csv_reader:

            #Assign Emp ID and Name columns to variables
            empID = column["Emp ID"]
            empName = column["Name"]

            #split the name column into first name and last name
            splitName = empName.split()
            empFirstName = splitName[0]
            empLastName = splitName[1]

            #replace the - in DOB with a /
            empDOB = column["DOB"]
            empDOB.split('-')[1] + '/' + empDOB.split('-')[2] + '/' + empDOB.split('-')[0]

            #replaces the first 5 digits in ssn with ***-**-
            empSSN = column["SSN"]
            empSSN = "***-**-" + empSSN.split("-")[2]

            #obtain the value in the dictionary associated with the Key in the State column of our csv
            empState = column["State"]
            stateAbbreviation = us_state_abbrev.get(empState)

            #write rows to a revised csv file of the newly formatted data
            writer.writerow([empID, empName, empFirstName, empLastName, empDOB, empSSN, stateAbbreviation])

            #print to terminal
            print(empID, empFirstName, empLastName, empDOB, empSSN, stateAbbreviation)