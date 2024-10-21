-- creates a trigger that resets the attribute valid_email only when the email has been changed.

DELIMITER //

CREATE TRIGGER reset_valid_email_on_email_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email has changed
    IF NEW.email != OLD.email THEN
        -- Reset the valid_email to 0
        SET NEW.valid_email = 0;
    END IF;
END//

DELIMITER ;

drop TRIGGER reset_valid_email_on_email_update;
