-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (IN n_user_id INT)
BEGIN
    SET @user_score := (SELECT AVG(score) from corrections WHERE n_user_id = user_id);

    UPDATE users SET average_score = @user_score WHERE id = n_user_id;
END //

DELIMITER ;

-- DROP Procedure `ComputeAverageScoreForUser`;
