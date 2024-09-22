select YEAR(b.SALES_DATE) as YEAR, month(b.SALES_DATE) as MONTH,a.GENDER,
        count(DISTINCT a.USER_ID) as USERS
from USER_INFO as a 
join ONLINE_SALE as b on a.USER_ID=b.USER_ID
where a.GENDER is not null
group by YEAR(b.SALES_DATE),month(b.SALES_DATE),a.GENDER
order by YEAR(b.SALES_DATE),month(b.SALES_DATE), a.GENDER asc;
