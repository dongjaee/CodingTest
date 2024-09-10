select b.ID,b.GENOTYPE,a.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA as a
left join ECOLI_DATA as b on a.ID=b.PARENT_ID
where b.PARENT_ID is not null and (b.GENOTYPE & a.GENOTYPE) = a.GENOTYPE
order by b.ID asc;



