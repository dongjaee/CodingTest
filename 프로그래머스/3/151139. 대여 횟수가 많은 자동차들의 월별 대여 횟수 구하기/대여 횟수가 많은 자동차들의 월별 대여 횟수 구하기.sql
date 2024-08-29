WITH car_rentals AS (
    SELECT 
        CAR_ID, 
        MONTH(START_DATE) AS RENTAL_MONTH,
        COUNT(*) AS TOTAL_RECORDS
    FROM 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE 
        START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY 
        CAR_ID, 
        MONTH(START_DATE)
),
car_rental_counts AS (
    SELECT 
        CAR_ID
    FROM 
        car_rentals
    GROUP BY 
        CAR_ID
    HAVING 
        SUM(TOTAL_RECORDS) >= 5
)

SELECT 
    RENTAL_MONTH AS MONTH,
    cr.CAR_ID,
    cr.TOTAL_RECORDS AS RECORDS
FROM 
    car_rentals cr
JOIN 
    car_rental_counts crc ON cr.CAR_ID = crc.CAR_ID
ORDER BY 
    RENTAL_MONTH ASC, 
    cr.CAR_ID DESC;
