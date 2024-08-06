--
DELIMITER //

CREATE TRIGGER update_quantity_after_insert
AFTER INSERT
ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name; -- le ; n'est pas vue comme une fin d'instruction
END //

DELIMITER ;
