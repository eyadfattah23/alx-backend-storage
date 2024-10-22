DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    -- Update average_score for each user
    UPDATE users
    SET average_score = (
        -- Calculate the weighted sum of scores for the current user
        (SELECT SUM(c.score * (SELECT p.weight FROM projects p WHERE p.id = c.project_id))
         FROM corrections c
         WHERE c.user_id = users.id
        )
        /
        -- Calculate the sum of weights of projects for the current user
        (SELECT SUM((SELECT p.weight FROM projects p WHERE p.id = c.project_id))
         FROM corrections c
         WHERE c.user_id = users.id
        )
    );
END //

DELIMITER ;
