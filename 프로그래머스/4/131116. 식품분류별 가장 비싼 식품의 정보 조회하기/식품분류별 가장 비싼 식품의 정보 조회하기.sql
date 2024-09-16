select FP.CATEGORY, FP.PRICE, FP.PRODUCT_NAME
from FOOD_PRODUCT FP
join (
    select CATEGORY, max(PRICE) as MAX_PRICE
    from FOOD_PRODUCT
    where CATEGORY in ('과자', '국', '김치', '식용유')
    group by CATEGORY
) as MAX_FP
on FP.CATEGORY = MAX_FP.CATEGORY and FP.PRICE = MAX_FP.MAX_PRICE
order by MAX_FP.MAX_PRICE desc;


