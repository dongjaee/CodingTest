select USER_ID, PRODUCT_ID 
from ONLINE_SALE 
group by USER_ID,PRODUCT_ID
having count(PRODUCT_ID)>1
order by USER_ID asc, PRODUCT_ID desc;
