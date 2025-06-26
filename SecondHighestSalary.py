'''
2 Problem 2 : Second Highest Salary ( https://leetcode.com/problems/second-highest-salary/ )
'''

import numpy as np
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset = 'salary')
    if len(employee['salary'].unique())<2:
        return pd.DataFrame({'SecondHighestSalary':[np.NaN]})

    employee['rnk'] = employee['salary'].rank(method='dense', ascending=False)
    ans = employee[employee.rnk==2][['salary']]
    ans = ans.rename(columns={'salary':'SecondHighestSalary'})
    return ans   