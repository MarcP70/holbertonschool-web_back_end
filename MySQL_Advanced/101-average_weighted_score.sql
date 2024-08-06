-- the stored procedure ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE id_user INT;
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight INT;
    DECLARE average_weighted_score FLOAT;

    -- Declare a cursor for user IDs
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    -- Declare a handler to end the loop when no more rows are found
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Open the cursor
    OPEN user_cursor;

    -- Loop through all user IDs
    user_loop: LOOP
        FETCH user_cursor INTO id_user;
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Calculate the weighted sum and total weight for the current user
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO weighted_sum, total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = id_user;

        -- Calculate the average weighted score
        IF total_weight > 0 THEN
            SET average_weighted_score = weighted_sum / total_weight;
        ELSE
            SET average_weighted_score = 0;
        END IF;

        -- Update the user's average_score in the users table
        UPDATE users
        SET average_score = average_weighted_score
        WHERE id = id_user;
    END LOOP;

    -- Close the cursor
    CLOSE user_cursor;
END //

DELIMITER ;
