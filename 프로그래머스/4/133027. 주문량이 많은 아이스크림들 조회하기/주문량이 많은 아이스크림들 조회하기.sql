with JUL as (
    select FLAVOR,sum(TOTAL_ORDER) as TOTAL_ORDER
    from JULY
    group by FLAVOR
    )

select a.FLAVOR
from FIRST_HALF as a 
join JUL as b on a.FLAVOR=b.FLAVOR
order by a.TOTAL_ORDER+b.TOTAL_ORDER desc
limit 3;

