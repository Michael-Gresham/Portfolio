CREATE TABLE GenericTree (
    NodeID INT NOT NULL,
    ParentNodeID INT NULL,
    CONSTRAINT PK_GenericTree PRIMARY KEY (NodeID),
    CONSTRAINT FK_GenericTree_Parent FOREIGN KEY (ParentNodeID) REFERENCES GenericTree (NodeID)
);
GO

INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (1, NULL);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (2, 1);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (3, 1);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (4, 1);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (5, 2);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (6, 2);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (7, 3);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (8, 3);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (9, 3);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (10, 6);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (11, 6);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (12, 6);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (13, 6);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (14, 7);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (15, 8);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (16, 8);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (17, 11);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (18, 11);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (19, 16);
INSERT INTO GenericTree (NodeID, ParentNodeID) VALUES (20, 16);
GO

/*
My take on implementing Breadth First Search in SQL is as follows. First I'll make a Table that will act like a queue by using 2 INT variables to represent 1. The current node in the queue and 2. the order in which the node is added.
Essentially I'll loop through the tree until the current node is the last node in the line and then print it and exit. 
Another way I thought about doing it was inserting and removing the front node in the table but quickly realized that Tables aren't ordered in any particular way leading me to add another column to the table to represent
the position in line of the node.

*/


CREATE PROCEDURE usp_BFS
@NodeID INT = NULL
AS
BEGIN
    SET NOCOUNT ON;
	
    /*
        EXECUTE usp_BFS;
    */
	Declare @Queue Table (Nodeid INT, rownum INT);
	DECLARE @c_NodeID INT;
    	DECLARE @v_NodeID INT;
	DECLARE @row_pointer INT = 0;
	DECLARE @row_number INT = 0;
	INSERT INTO @Queue
	VALUES
	(@NodeID, @row_number)

	SET @row_number += 1

	/*WHILE (EXISTS (SELECT 1 FROM @Queue))*/
	WHILE (@row_pointer < @row_number)
	BEGIN
		
		SET @c_NodeID = (SELECT Nodeid FROM @Queue WHERE rownum = @row_pointer)
		DECLARE c_CUR CURSOR FAST_FORWARD LOCAL FOR
			SELECT NodeID
				FROM GenericTree
			WHERE ISNULL(ParentNodeID, 0) = ISNULL(@c_NodeID, 0)
			ORDER BY NodeID;
		OPEN c_CUR;
		FETCH FROM c_CUR INTO @v_NodeID;
		
		WHILE @@FETCH_STATUS = 0
		BEGIN
			INSERT INTO @Queue VALUES (@v_NodeID, @row_number)
			SET @row_number +=1
			FETCH FROM c_CUR INTO @v_NodeID;
		END;

		PRINT @c_NodeID
		SET @row_pointer += 1
		CLOSE c_CUR;
		DEALLOCATE c_CUR;
	
	
	END;
END;
GO

