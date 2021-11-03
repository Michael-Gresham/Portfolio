## Goal of Question 1 is to use powershell to implement 

$SQLServer = "localhost"
$dbName = "CPSC332"
$server = New-object Microsoft.SqlServer.Management.Smo.Server("(local)")


$db = New-Object Microsoft.SqlServer.Management.Smo.Database($server, $dbName)
if ($db){
    $server.KillDatabase($dbName)
}
#$db.DropIfExists($dbName)
$db.create()
Write-Host $db.CreateDate


Write-Host "Inserting SQL Query into Database:"
Invoke-Sqlcmd -ServerInstance $SQLServer -Database $dbName -InputFile "C:\Users\Michael\Desktop\cpsc 332\CPSC 332 Homework # 1\Company.sql"
