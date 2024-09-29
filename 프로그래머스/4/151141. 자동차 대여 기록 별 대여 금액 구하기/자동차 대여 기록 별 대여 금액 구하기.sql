SELECT b.HISTORY_ID,
    round(
        CASE
            WHEN (DATEDIFF(b.END_DATE, b.START_DATE)+1) < 7 THEN 
                (DATEDIFF(b.END_DATE, b.START_DATE)+1) * a.DAILY_FEE
            WHEN (DATEDIFF(b.END_DATE, b.START_DATE)+1) < 30 THEN 
                (100 - (SELECT DISCOUNT_RATE 
                        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                        WHERE DURATION_TYPE = '7일 이상' 
                          AND CAR_TYPE = '트럭'
            )) / 100 * (DATEDIFF(b.END_DATE, b.START_DATE)+1) * a.DAILY_FEE
            WHEN (DATEDIFF(b.END_DATE, b.START_DATE)+1) < 90 THEN 
                (100 - (SELECT DISCOUNT_RATE 
                        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                        WHERE DURATION_TYPE = '30일 이상' 
                          AND CAR_TYPE = '트럭'
             )) / 100 * (DATEDIFF(b.END_DATE, b.START_DATE)+1) * a.DAILY_FEE
            ELSE 
                (100 - (SELECT DISCOUNT_RATE 
                        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                        WHERE DURATION_TYPE = '90일 이상' 
                          AND CAR_TYPE = '트럭'
            )) / 100 * (DATEDIFF(b.END_DATE, b.START_DATE)+1) * a.DAILY_FEE
        END
    ) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS a
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS b ON a.CAR_ID = b.CAR_ID
WHERE a.CAR_TYPE = '트럭'
ORDER BY FEE DESC, b.HISTORY_ID DESC;