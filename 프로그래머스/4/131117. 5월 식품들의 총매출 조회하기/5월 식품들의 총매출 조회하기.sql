select distinct a.PRODUCT_ID,
        a.PRODUCT_NAME,
        (a.PRICE*(sum(b.AMOUNT) over (partition by b.PRODUCT_ID))) as TOTAL_SALES
        
from FOOD_PRODUCT as a
left join FOOD_ORDER as b on a.PRODUCT_ID=b.PRODUCT_ID
where b.PRODUCE_DATE like '2022-05%'
order by (a.PRICE*(sum(b.AMOUNT) over (partition by b.PRODUCT_ID))) desc,
        a.PRODUCT_ID asc;