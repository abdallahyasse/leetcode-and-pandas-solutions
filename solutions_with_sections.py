# ----------------------
# 1. Longest Substring Without Repeating Characters
# ----------------------
def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    start = 0
    max_len = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        max_len = max(max_len, i - start + 1)
    return max_len
https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1730307164
# ----------------------
# 2. Two Sum II - Input Array Is Sorted
# ----------------------
def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]  # 1-based indexing
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1730409377
# ----------------------
# 3. Reverse Words in a String
# ----------------------
def reverse_words(s: str) -> str:
    words = s.split()
    return " ".join(reversed(words))
https://leetcode.com/problems/reverse-words-in-a-string/submissions/1730306373
# ----------------------
# Pandas Problems
# ----------------------
import pandas as pd

# 4. Employees Earning More Than Their Managers
def employees_more_than_managers(emp: pd.DataFrame) -> pd.DataFrame:
    mgr = emp[['id', 'salary']].rename(columns={'id': 'managerId', 'salary': 'managerSalary'})
    merged = emp.merge(mgr, on='managerId', how='inner')
    result = merged[merged['salary'] > merged['managerSalary']][['name']]
    result.columns = ['Employee']
    return result

# 5. Customers Who Never Order
def customers_who_never_order(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    result = merged[merged['customerId'].isna()][['name']]
    result.columns = ['Customers']
    return result

# 6. Final Prices With a Special Discount in a Shop
def final_prices(prices):
    res = prices[:]
    stack = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] >= price:
            idx = stack.pop()
            res[idx] = prices[idx] - price
        stack.append(i)
    return res

if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))
    print(two_sum([2,7,11,15], 9))
    print(reverse_words("  hello world  "))
    emp_df = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['Joe', 'Henry', 'Sam', 'Max'],
        'salary': [70000, 80000, 60000, 90000],
        'managerId': [3, 4, None, None]
    })
    print(employees_more_than_managers(emp_df))
    customers_df = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['Joe', 'Henry', 'Sam', 'Max']
    })
    orders_df = pd.DataFrame({
        'id': [1, 2],
        'customerId': [3, 1]
    })
    print(customers_who_never_order(customers_df, orders_df))
    print(final_prices([8, 4, 6, 2, 3]))
