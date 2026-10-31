# Write your MySQL query statement below
SELECT Vs.customer_id as customer_id, count(Vs.customer_id) as count_no_trans
FROM Visits AS Vs
LEFT JOIN Transactions AS Ts
ON Vs.visit_id = Ts.visit_id
where Ts.amount  IS NULL
Group by Vs.customer_id;
