'''
Pandas4

1 Problem 1 : Nth Highest Salary (https://leetcode.com/problems/nth-highest-salary/solution/)
'''

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset = 'salary')
    employee['rnk'] = employee['salary'].rank(method='dense', ascending=False)
    ans = employee[employee.rnk==N][['salary']]
    if not len(ans):
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    ans = ans.rename(columns={'salary':f'getNthHighestSalary({N})'})
    return ans   