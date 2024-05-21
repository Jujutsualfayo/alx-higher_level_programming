-- Lists the number of records with the same score in the
-- table second_table of database hbtn-0c_0 in my MySQL server.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
