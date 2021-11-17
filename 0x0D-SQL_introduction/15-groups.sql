-- Lists number of records with the same value in the table second_table in descending order.
SELECT score, COUNT(score) AS "number" FROM second_table GROUP BY score ORDER BY score DESC;
