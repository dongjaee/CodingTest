select a.name, a.datetime
from ANIMAL_INS as a
left join animal_outs as b on a.animal_id=b.animal_id
where b.name is null and a.name is not null
order by a.datetime 
limit 3
