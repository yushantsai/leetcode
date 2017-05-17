# Find employees who earn the top three salaries in each of the department.
select D1.Name as Department, E1.Name as Employee, E1.Salary
from Employee E1, Department D1
where D1.Id = E1.DepartmentId and
(
    select count(distinct E2.Salary)
    from Employee E2
    where E2.DepartmentId = D1.Id and E2.Salary > E1.Salary
) < 3

# Return the n-th highest salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    # Cannot change the value in the query
    set N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select ifnull(
          (select distinct salary
          from Employee
          order by Salary desc
          limit 1 offset N)
    , NULL)
  );
END

# Rank scores and if scores are the same, they share the same ranking number.
select S1.Score,
(
    select count(distinct S2.Score)
    from Scores S2
    where S2.Score >= S1.Score
) as Rank
from Scores S1
order by S1.Score desc

# Find numbers that appear at leat 3 times consecutively.
select distinct l1.Num as ConsecutiveNums
from Logs l1, Logs l2, Logs l3
where l1.Num = l2.Num and l2.Num = l3.Num and l1.Id = l2.Id - 1 and l2.Id = l3.Id - 1

# Delete the duplicated emails and keep the unique email based on its smallest id.
delete P1
from Person P1, Person P2
where P1.Email = P2.Email and P1.Id > P2.Id

# Find the cancellation rate of requests made by unbanned clients between 2013/10/01 and 2013/10/03.
select Request_at as Day,
round(sum(if(Trips.Status != "completed", 1, 0)) / count(*), 2) as "Cancellation Rate"
from Trips
where Request_at between "2013-10-01" and "2013-10-03" and Client_Id in
(
    select Users_Id
    from Users
    where Banned = "No" and Role = "client"
)
group by Request_at