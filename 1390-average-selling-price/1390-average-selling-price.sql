# Write your MySQL query statement below
SELECT p.product_id, case when Round(sum(p.price * u.units )/sum(u.units),2) is null then 0 else 
             Round(sum(p.price * u.units )/sum(u.units),2) end as average_price
FROM Prices p
Left JOIN UnitsSold u
ON p.product_id = u.product_id
and purchase_date between start_date and end_date
group by 1