select MEMBER_ID,
        MEMBER_NAME,GENDER, 
        DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
from MEMBER_PROFILE
where month(DATE_OF_BIRTH)=3 and TLNO is not null and GENDER ='W'
order by MEMBER_ID asc;