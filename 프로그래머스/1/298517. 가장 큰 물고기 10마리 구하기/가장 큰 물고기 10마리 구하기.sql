select ID,ifnull(LENGTH,10) as LENGTH  
from FISH_INFO
where LENGTH>10
order by LENGTH desc
limit 10;

