-- stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id_input INT
)
BEGIN
    DECLARE average_score FLOAT;

    -- Calculer la moyenne des scores pour l'utilisateur donné
    SELECT AVG(score) INTO average_score
    FROM corrections
    WHERE user_id = user_id_input;

    -- Mettre à jour le score moyen de l'utilisateur dans la table users
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id_input;
END //

DELIMITER ;
