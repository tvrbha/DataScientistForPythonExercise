""" Exercise 1: Write a Pandas program to create and display a DataFrame from a specified
dictionary data which has the index labels."""

import pandas as pd
import numpy as np
def dataframe_with_null_values():
    exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    exam_data = pd.DataFrame(exam_data,index = ['a','b','c','d','e','f','g','h','i','j'])
    print(exam_data)

dataframe_with_null_values()

"""
Exercise 2: Write a Pandas program to select the rows where 
number of attempts in the examination is less than 2 and score greater than 15.
"""

import pandas as pd
import numpy as np
def dataframe_with_condition_values():
    exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    exam_data = pd.DataFrame(exam_data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    print(exam_data.loc[(exam_data['attempts'] <= 2) & (exam_data['score'] > 15)])

dataframe_with_condition_values()


""" Exerise 3: Change the value in row 'd' to 11.5"""
import pandas as pd
import numpy as np
def dataframe_update_specfic_value():
    exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    exam_data = pd.DataFrame(exam_data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    # Changing the values of a particular row and col
    exam_data.loc['d', 'score'] = 11.5
    print(exam_data)

dataframe_update_specfic_value()


"""Exercise 4: Write a Pandas program to calculate the sum of the examination attempts by the students."""

import pandas as pd
import numpy as np
def dataframe_total_no_of_attempts():
    exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    exam_data = pd.DataFrame(exam_data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    print(exam_data)
    print('Total No. Of Attempts   : ', exam_data['attempts'].sum())

dataframe_total_no_of_attempts()

""" Exercise 5: print a list of rows from a specified DataFrame"""
import pandas as pd
import numpy as np
def dataframe_list_of_rows_specified_fomat():
    d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
    d = pd.DataFrame(d)
    print(d)
    print(d.loc[(d['col1'] == 4)])


dataframe_list_of_rows_specified_fomat()

"""Exercise 5: Drop a list of rows from a specified DataFrame"""
import pandas as pd
import numpy as np
def dataframe_drop_list_of_rows_specified_fomat():
    d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
    d = pd.DataFrame(d)
    print(d)
    print(d.drop([2, 4]))


dataframe_drop_list_of_rows_specified_fomat()

"""Exercise 6: Check whether a given column is present in a DataFrame or not"""

import pandas as pd
import numpy as np
def dataframe_is_column_exisits():
    d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
    d = pd.DataFrame(d)
    print(d)
    if 'col4' in d.columns:
        print('Col4 Exisits')
    else:
        print('Col4 Not Exisits')

dataframe_is_column_exisits()


"""Exercise 7: Get column index from column name of a given DataFrame"""

import pandas as pd
import numpy as np
def dataframe_getcolumnindex_from_columnname():
    d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
    d = pd.DataFrame(d)
    print(d)
    print('Column Location of Col2 : ',d.columns.get_loc('col2'))

dataframe_getcolumnindex_from_columnname()


"""Exercise 8: Write a Pandas program to select all columns, except one given column in a DataFrame."""

import pandas as pd
import numpy as np
def dataframe_dropspecificcolumn_from_dataframe():
    d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
    d = pd.DataFrame(d)
    print(d)
    d.drop('col3',axis=1)
    print('Dropping one Specific column Col3  : \n',d.drop('col3',axis=1))

dataframe_dropspecificcolumn_from_dataframe()


""" Exercise 9: Write a Pandas program to remove last n rows of a given DataFrame."""
import pandas as pd
import numpy as np
def dataframe_droplastnrows_from_dataframe():
    d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
    d = pd.DataFrame(d)
    print(d)
    no_of_rows=int(input('Enter the Number of Rows to be removed : '))
    df_dropped_rows = d.iloc[:-no_of_rows]
    print('Dropping one last specifc rows : \n',df_dropped_rows)

dataframe_droplastnrows_from_dataframe()


"""Exercise 10: Display the movies longer than 30 minutes and shorter than 360 minutes"""
import pandas as pd
import numpy as np
def dataframe_listrows_basedoncondition():
    movie_df = pd.read_csv("C:/Users/Bhavani/python/IMDB-Movie-Data.csv")
    print(movie_df)
    movie_df.loc[(movie_df['Runtime (Minutes)'] >= 30) & (movie_df['Runtime (Minutes)'] <= 360)]
    print(movie_df)

dataframe_listrows_basedoncondition()
