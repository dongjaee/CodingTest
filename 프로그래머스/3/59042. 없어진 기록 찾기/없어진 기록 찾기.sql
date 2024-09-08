select a.ANIMAL_ID, a.NAME
from ANIMAL_OUTS as a
left join ANIMAL_INS as b on a.ANIMAL_ID=b.ANIMAL_ID
where b.ANIMAL_ID is null
order by a.ANIMAL_ID asc;