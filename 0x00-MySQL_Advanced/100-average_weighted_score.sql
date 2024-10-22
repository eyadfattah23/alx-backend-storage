-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN n_user_id INT)
BEGIN

    SET @factors_sum := (SELECT SUM(weight) FROM projects);

    SET @score_times_weight := (SELECT SUM(score * (SELECT weight FROM projects WHERE id = project_id)) FROM corrections WHERE user_id = n_user_id);

    UPDATE users SET average_score = (@score_times_weight / @factors_sum)
    WHERE id = n_user_id;
END // 

DELIMITER ;

-- DROP Procedure ComputeAverageWeightedScoreForUser;
