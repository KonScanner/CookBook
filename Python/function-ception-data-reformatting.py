"""
When processing data, most of the times,
it will not be formatted in the desired way.

We often have to write a massive Python script,
doing some splitting and stiching.

Another way to consider this problem is
using higer order functions.
"""

# Given this dictionary
data = [
    {
        "name": "",
        "age": 35,
        "salary": 100000,
    },
    {
        "name": "Jane Doe",
        "age": 42,
        "salary": 150000,
    },
    {
        "name": "John Doe",
        "age": "23",
        "salary": 85,
    },
    {
        "name": "Bar Foo",
        "age": "302",
        "salary": "32500",
    },
    {
        "name": "Foo Bar",
        "age": "30",
        "salary": "79",
    },
]

"""
Let's say we have to:
* Ignore any person with an empty name.
* Ignore any person with an age over 100.
* Make sure ages are numbers, not strings.
* Make sure salaries are numbers, not strings.
* Convert salaries which are less than $1,000 from hourly rates to yearly.
"""

# First we wirte the functions:


def has_empty_name(person):
    return person['name'] == ''


def has_age_over_100(person):
    return person['age'] > 100


def convert_age_to_number(person):
    person['age'] = float(person['age'])


def convert_salary_to_number(person):
    person['salary'] = float(person['salary'])


def convert_salary_to_yearly(person):
    if person['salary'] < 1000:
        # ~ 2000 work hours in the year
        person['salary'] = 2000*person['salary']


"""
First we'll want to do a pass 
where we make sure that the fields are correct
(convert ages and salaries to numbers, 
then convert hourly salaries to yearly). 
Then, we'll want to filter out the bad data
(empty name or age too high).

The reason for the ordering is that our age checker
requires that the person has an age that is a number,
so we want to convert ages to numbers first.

"""


def clean_data(data, cleaners, filters):
    """
    This function will take in a list of cleaners
    (this is the name I picked for functions that clean up
    the data by modifying it).

    Then, it will take a list of filters, or functions
    that determine if we want to keep them.
    """
    # first ensure data is clean*
    for item in data:
        for cleaner_func in cleaners:
            cleaner_func(item)
    # then keep only the good data
    output = []
    for item in data:
        for filter_ in filters:
            # don't add this item if the filter returns False
            if not filter_(item):
                break
        output.append(item)
    return output


print(clean_data(data,
                 cleaners=[convert_age_to_number,
                           convert_salary_to_number, convert_salary_to_yearly],
                 filters=[has_empty_name, has_age_over_100]))
