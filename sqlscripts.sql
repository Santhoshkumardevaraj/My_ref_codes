select Empname,MAX(createddatetime) as CreateDate into #Temp from Table_loginlog where Empname in (select Empname from Table_EmpProfile where Active=1) group by Empname order by CreateDate desc

Select Empname,CreateDate,DATEDIFF(DAY,CreateDate,GETDATE()) as daysdiff from #Temp

DROP TABLE #Temp
