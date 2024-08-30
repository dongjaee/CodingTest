with SUM_SALES as(
    select BOOK_ID,sum(SALES) as TOTAL
    from BOOK_SALES
    where SALES_DATE like '2022-01%'
    group by BOOK_ID
) 
select CATEGORY,sum(TOTAL) as TOTAL_SALES
from BOOK as a
join SUM_SALES as b on a.BOOK_ID=b.BOOK_ID
group by CATEGORY
order by CATEGORY asc;
