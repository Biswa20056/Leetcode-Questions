CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
select salary into result
    from(select rownum as rn , salary 
    from(select distinct salary
    from Employee
    order by salary desc))
    where rn = N;

    RETURN result;
END;