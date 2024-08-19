select a.ID, count(b.ID) as CHILD_COUNT
from ECOLI_DATA as a
left join (select ID,PARENT_ID
    from ECOLI_DATA) as b
on a.ID=b.PARENT_ID
group by a.ID
order by a.ID asc;

    
    