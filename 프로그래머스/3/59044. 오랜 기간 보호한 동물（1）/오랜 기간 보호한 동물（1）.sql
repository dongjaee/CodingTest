select a.NAME,a.DATETIME
from ANIMAL_INS as a
left join ANIMAL_OUTS as b on a.ANIMAL_ID=b.ANIMAL_ID
where b.NAME is null and a.NAME is not null
order by a.DATETIME asc
limit 3;