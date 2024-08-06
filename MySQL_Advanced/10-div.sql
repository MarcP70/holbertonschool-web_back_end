-- divides (and returns) the first by the second number
-- or returns 0 if the second number is equal to 0.
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
NO SQL
BEGIN
    DECLARE result FLOAT;

    -- Check if the denominator is zero
    IF b = 0 THEN
        SET result = 0;
    ELSE
        -- Perform the division
        SET result = a / b;
    END IF;

    -- Return the result
    RETURN result;
END //

DELIMITER ;
