# Write your MySQL query statement below
select employee_id, IF(name not like 'm%' AND employee_id % 2 <>0, salary, 0) as bonus
from employees
order by employee_id;