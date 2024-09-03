with group_USED_GOODS_BOARD as (
    select *
    from USED_GOODS_BOARD
    group by WRITER_ID
    having count(*)>=3)

select USER_ID,NICKNAME,
    concat(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) as 전체주소,
    concat(substring(TLNO, 1, 3), '-', substring(TLNO, 4, 4), '-', substring(TLNO, 8, 4)) AS 전화번호
from group_USED_GOODS_BOARD as a
join USED_GOODS_USER as b on a.WRITER_ID=b.USER_ID
order by USER_ID desc;
 

