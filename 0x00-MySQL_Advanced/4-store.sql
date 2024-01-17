-- Task 4

DROP TRIGGER IF EXISTS reduce_quantity;
DELIMIER $$
CREATE TIGGER reduce_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
END $$
DELIMITER
