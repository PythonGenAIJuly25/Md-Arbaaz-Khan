CREATE TABLE Logs (
log_id INT PRIMARY KEY
);
INSERT INTO Logs (log_id) VALUES (1);
INSERT INTO Logs (log_id) VALUES (2);
INSERT INTO Logs (log_id) VALUES (3);
INSERT INTO Logs (log_id) VALUES (7);
INSERT INTO Logs (log_id) VALUES (8);
INSERT INTO Logs (log_id) VALUES (10);
select * from Logs;
WITH numbered AS (
    SELECT 
        log_id,
        log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp
    FROM Logs
)
SELECT 
    MIN(log_id) AS start_id,
    MAX(log_id) AS end_id
FROM numbered
GROUP BY grp
ORDER BY start_id;


