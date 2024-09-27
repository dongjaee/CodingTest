select a.MEMBER_NAME,b.REVIEW_TEXT,date_format(b.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE as a
join REST_REVIEW as b on a.MEMBER_ID=b.MEMBER_ID
where a.MEMBER_NAME=(
    select a2.MEMBER_NAME
    from MEMBER_PROFILE as a2
    join REST_REVIEW as b2 on a2.MEMBER_ID = b2.MEMBER_ID
    group by a2.MEMBER_NAME
    order by count(*) desc
    limit 1
)
order by b.REVIEW_DATE asc, b.REVIEW_TEXT asc
