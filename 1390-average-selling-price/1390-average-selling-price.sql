# Write your MySQL query statement below
SELECT p.product_id, ifnull(Round(sum(p.price * u.units )/sum(u.units),2),0) as average_price
FROM Prices p
Left JOIN UnitsSold u
 ON p.product_id = u.product_id
 and purchase_date between start_date and end_date
group by 1