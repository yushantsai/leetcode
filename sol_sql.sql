# Find employees who earn the top three salaries in each of the department.
select D1.Name as Department, E1.Name as Employee, E1.Salary
from Employee E1, Department D1
where D1.Id = E1.DepartmentId and
(
    select count(distinct E2.Salary)
    from Employee E2
    where E2.DepartmentId = D1.Id and E2.Salary > E1.Salary
) < 3