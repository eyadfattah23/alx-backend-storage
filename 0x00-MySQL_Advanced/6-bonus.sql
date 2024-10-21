-- creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id  INT,
                          IN project_name VARCHAR(50),
                          IN score FLOAT)

BEGIN


    INSERT INTO projects (name) SELECT project_name WHERE NOT EXISTS        
        (SELECT 1 FROM projects WHERE name = project_name);

    SET @proj_id := (SELECT id FROM projects WHERE name = project_name);
    INSERT INTO corrections
        VALUES (user_id, @proj_id, score);

END $$

DELIMITER ; 

-- drop Procedure AddBonus;













----- another solution ------

-- DELIMITER //
-- CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
-- BEGIN
--     IF (SELECT id FROM projects WHERE name = project_name) IS NULL THEN
--         INSERT INTO projects (name) VALUES (project_name);
--         SET @project_id = LAST_INSERT_ID();
--     ELSE
--         SELECT id INTO @project_id FROM projects WHERE name = project_name;
--     END IF;
--     INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
-- 
-- END //
-- DELIMITER ;
----------------------------------------------------------------



---not tested solution
-- DELIMITER //
-- CREATE PROCEDURE ADDBonus (IN user_id INT, IN project_name VARCHAR(50), IN score INT)
-- BEGIN
--     DECLARE proj_id INT;
-- 
--     -- Check if project exists
--     IF EXISTS (SELECT id FROM projects WHERE name = project_name) THEN
--         SET proj_id := (SELECT id FROM projects WHERE name = project_name);
--     ELSE
--         -- If project does not exist, insert it and get the new project id
--         INSERT INTO projects (name) VALUES (project_name);
--         SET proj_id := LAST_INSERT_ID();
--     END IF;
-- 
--     -- Insert the correction
--     INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, proj_id, score);
-- END //
-- DELIMITER ;
