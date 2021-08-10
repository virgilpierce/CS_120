#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pa
import datetime as dt
pa.set_option('max_colwidth', 200)


# In[2]:


first_day = dt.date(2021, 8, 23)


# In[3]:


holidays = [dt.date(2021, 9, 6) ]
turkey_break_start = dt.date(2021, 11, 24)
turkey_break_end = dt.date(2021, 11, 28)
turkey_break_delta = turkey_break_end - turkey_break_start
holidays += [ turkey_break_start + dt.timedelta(i) for i in range(turkey_break_delta.days+1)]


# In[4]:


last_day = dt.date(2021, 12, 3)


# In[5]:


final_exam = dt.date(2021, 12, 6)


# In[6]:


semester_length = last_day - first_day
semester_length


# In[7]:


class_days = []
for i in range((semester_length.days //7 + 1)):
    class_days += [first_day + dt.timedelta(i*7), first_day + dt.timedelta(i*7+2), first_day + dt.timedelta(i*7+4)]
class_days += [final_exam]


# In[8]:


schedule = pa.DataFrame(class_days, columns = ['Day'])
weekday_dict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 
                5:'Saturday', 6:'Sunday'}
for i in range(schedule.shape[0]):
    schedule.loc[i,'Week_Day'] = schedule.loc[i, 'Day'].weekday()
schedule.Week_Day = schedule.Week_Day.map(weekday_dict)


# In[9]:


for holiday in holidays:
    schedule.loc[schedule.Day==holiday, 'Title'] = 'No Class - University Holiday'


# In[10]:


def add_day(title='', description='', notes=''):
    global schedule
    global day
    
    while schedule.loc[day, 'Day'] in holidays:
        day += 1
    if day >= schedule.shape[0]:
        print('Error to many days')
        return 'ERROR'
    else:
        schedule.loc[day, 'Title'] = title
        schedule.loc[day, 'Description'] = description
        schedule.loc[day, 'Notes'] = notes
        
        day += 1
    


# In[17]:


day = 0

# Introduction - our first program

add_day('Introduction to Python / Jupyter', 
        'Variables', 'Compute N! and (2N-1)!!; and how many primes are there less than N?')

add_day('Variables and Functions', 'Types of variables and writing functions')

add_day('Lab Day: Plotting Functions')

## Week 2

add_day('Variables and Functions')

add_day('Variables and Functions')

add_day('Lab Day: Find N! and (2N-1)!!')


## Week 3 

add_day('Local and Global Variables')

add_day('Lab Day: Exploring Local and Global Variables')

## Week 4

add_day('Conditionals and Recursion')

add_day('Conditionals and Recursion')

add_day('Lab Day:  Approximate a square root')

## Week 5

add_day('Introduction to modules', 'Numpy and Matplotlib')

add_day('Introduction to modules')

add_day('Lab Day: How fast does factorial grow?')

## Week 6

add_day('Iterations', 'For and While')

add_day('Iterations', 'For and While')

add_day('Lab Day: Iterations')

## Week 7

add_day('Iterations', 'Iterator Objects')

add_day('Strings', 'Arguably the thing Python does best')

add_day('Lab Day: Strings')

## Week 8 

add_day('Strings', 'Arguably the thing Python does best')

add_day('Strings')

add_day('Lab Day: Analyzing Hamlet')

## Week 9 

add_day('Lists and Tuples', 'Mutable versus Immutaable', 'and why we would care')

add_day('Lists and Tuples', 'Slices, map, filter, reduce')

add_day('Lab Day: How many primes are there less than N?')

## Week 10

add_day('Lists and Tuples')

add_day('Lists and Tuples')

add_day('Lab Day: Find the derrivative of a polynomial')

## Week 11

add_day('Dictionaries')

add_day('Dictionaries')

add_day('Lab Day: Algebra of Permutations')

## Week 12

add_day('Putting it All Together')

add_day('Putting it All Together')

add_day('Putting it All Together')

## Week 14

add_day('Data Structure Selection')

add_day('Data Structure Selection')

add_day('Lab Day:  Activity with Data Structures')

## Week 15

add_day('File Manipulation')

add_day('Lab Day: Using Files')

## Week 16


add_day('Things left undone')

add_day('Things left undone')

add_day('Final Exam/Project')

schedule


# In[ ]:




