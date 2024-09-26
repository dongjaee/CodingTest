SELECT substring(PRODUCT_CODE,1,2), count(product_id)
from PRODUCT
group by substring(PRODUCT_CODE,1,2)
order by substring(PRODUCT_CODE,1,2)