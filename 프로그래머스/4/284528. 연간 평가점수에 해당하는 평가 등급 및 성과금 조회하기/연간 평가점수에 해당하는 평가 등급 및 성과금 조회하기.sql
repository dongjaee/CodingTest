with hr as (
    select EMP_NO,
        case 
            when avg(SCORE) >= 96 then 'S'
            when avg(SCORE) >= 90 then 'A'
            when avg(SCORE) >= 80 then 'B'
            else 'C'
        end as GRADE
    from HR_GRADE
    group by EMP_NO
)

select a.EMP_NO,a.EMP_NAME,b.GRADE,
    case
        when b.GRADE='S' then a.SAL*0.2
        when b.GRADE='A' then a.SAL*0.15
        when b.GRADE='B' then a.SAL*0.1
        else 0
    end as BONUS
from HR_EMPLOYEES as a
join hr as b on a.EMP_NO=b.EMP_NO
order by a.EMP_NO asc;