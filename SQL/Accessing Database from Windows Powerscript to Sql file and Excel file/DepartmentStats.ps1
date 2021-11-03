$SqlConnection = New-Object System.Data.SqlClient.SqlConnection;
$SqlConnection.ConnectionString = "Server=localhost;Database=CPSC332;Integrated Security=True;";
$SqlConnection.Open();


$SqlCmd = New-Object System.Data.SqlClient.SqlCommand;
$Sqlcmd.CommandTimeout = 0;
$SqlCmd.Connection = $SqlConnection;
$SqlCmd.CommandText = 

#Note this requires the use alias's as you need to be able to link two seperate queries
#To one table under DEPARTMENT NAME and you need to inner join y to x in order to combine the two together.
#under one table.
# x will group sum of salary and avg of salary together under department name and 
# y will group sum or working hours  and avg working hours together under department name
# Finally combining both together to create the table. 
"
Select
x.DepartmentName,
y.DepartmentName,
SumOfSalary,
AvgOfSalary,
SumOfWorkingHours,
TotalNumOfProjects
FROM(
Select 
	dbo.DEPARTMENT.Dname AS DepartmentName,
	SUM(dbo.EMPLOYEE.Salary) AS SumOfSalary,
	AVG(dbo.EMPLOYEE.Salary) AS AvgOfSalary
FROM
	dbo.DEPARTMENT
	INNER JOIN dbo.EMPLOYEE
	ON dbo.DEPARTMENT.Dnumber = dbo.EMPLOYEE.Dno
	GROUP BY dbo.DEPARTMENT.Dname
) AS x

INNER JOIN
(
Select
	dbo.DEPARTMENT.Dname AS DepartmentName,
	SUM(ISNULL(dbo.WORKS_ON.Hours, 0)) AS SumOfWorkingHours,
	COUNT(DISTINCT dbo.WORKS_ON.Pno) AS TotalNumOfProjects
FROM 
	dbo.DEPARTMENT
	INNER JOIN dbo.EMPLOYEE
	ON dbo.DEPARTMENT.Dnumber = dbo.EMPLOYEE.Dno
	INNER JOIN dbo.WORKS_ON
	ON dbo.EMPLOYEE.Ssn = dbo.WORKS_ON.Essn
	GROUP BY dbo.DEPARTMENT.Dname
) AS y

ON x.DepartmentName = y.DepartmentName;

"

#This statement doesn't work as the innerjoin from dbo.Works_ON would cut out
#Some of the workers salary information giving an incorrect value.
#"Select 
#	dbo.DEPARTMENT.Dname AS DepartmentName,
#	SUM(dbo.EMPLOYEE.Salary) AS SumOfSalary,
#	AVG(dbo.EMPLOYEE.Salary) AS AvgOfSalary,
#	SUM(ISNULL(dbo.WORKS_ON.Hours, 0)) AS SumOfWorkingHours,
#	COUNT(DISTINCT dbo.WORKS_ON.Pno) AS TotalNumOfProjects
#FROM
#	dbo.DEPARTMENT
#	INNER JOIN dbo.EMPLOYEE
#	ON dbo.DEPARTMENT.Dnumber = dbo.EMPLOYEE.Dno
#	INNER JOIN dbo.WORKS_ON
#	ON dbo.EMPLOYEE.Ssn = dbo.WORKS_ON.Essn
#	GROUP BY dbo.DEPARTMENT.Dname
#";

$SqlAdapter = New-Object System.Data.SqlClient.SqlDataAdapter
$SqlAdapter.SelectCommand = $Sqlcmd


$DataSet = New-Object System.Data.DataSet
$SqlAdapter.Fill($DataSet)

$SqlConnection.Close()

$DataSet.Tables[0] | Select "DepartmentName", "SumOfSalary", "AvgOfSalary", "SumOfWorkingHours", "TotalNumOfProjects" | Export-Csv -NoTypeInformation "C:\Users\Michael\Desktop\DepartmentStats.csv"
#$DataSet.Tables[0] | Select "x.DepartmentName", "y.DepartmentName" | Export-Csv -NoTypeInformation "C:\Users\Michael\Desktop\DepartmentStats.csv"




