-- Prints thhe sorted database, using WHERE to filter keyword in second_table.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC, name;
