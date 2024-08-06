--
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id_input INT
)
BEGIN
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight INT;
    DECLARE average_weighted_score FLOAT;

    -- Calculate the weighted sum and total weight
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO weighted_sum, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id_input;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        SET average_weighted_score = weighted_sum / total_weight;
    ELSE
        SET average_weighted_score = 0;
    END IF;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = average_weighted_score
    WHERE id = user_id_input;
END //

DELIMITER ;
