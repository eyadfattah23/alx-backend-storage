-- Trigger = When an event happens, do something
-- ex. (INSERT, UPDATE, DELETE)
-- checks data, handles errors, auditing tables

-- task: creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER dec_items_after_adding_order 
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.NUMBER
WHERE name = NEW.item_name;


-- DROP TRIGGER dec_items_after_adding_order;
