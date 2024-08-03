-- Inserting sample data into RENTER table
INSERT INTO RENTER (RENTER_NUM, FIRST_NAME, MIDDLE_INITIAL, LAST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, TELEPHONE, EMAIL) VALUES
('R001', 'John', 'A', 'Doe', '123 Maple St.', 'Springfield', 'IL', '62701', '555-1234', 'john.doe@example.com'),
('R002', 'Jane', 'B', 'Smith', '456 Oak St.', 'Springfield', 'IL', '62702', '555-5678', 'jane.smith@example.com'),
('R003', 'Alice', 'C', 'Johnson', '789 Pine St.', 'Springfield', 'IL', '62703', '555-8765', 'alice.johnson@example.com'),
('R004', 'Bob', 'D', 'Williams', '101 Elm St.', 'Springfield', 'IL', '62704', '555-4321', 'bob.williams@example.com');

-- Inserting sample data into PROPERTY table
INSERT INTO PROPERTY (CONDO_LOCATION_NUM, CONDO_LOCATION_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, CONDO_UNIT_NUM, SQUARE_FOOTAGE, BEDROOMS, BATHROOMS, MAX_PERSONS, BASE_WEEKLY_RATE) VALUES
(1, 'Sunset Villas', '101 Beachfront Ave.', 'Oceanview', 'FL', '32123', '101', 850, 2, 1, 4, 1200.00),
(1, 'Sunset Villas', '101 Beachfront Ave.', 'Oceanview', 'FL', '32123', '102', 950, 3, 2, 6, 1500.00),
(2, 'Seaside Retreat', '202 Coastal Dr.', 'Seaside', 'FL', '32124', '201', 1200, 3, 2, 6, 1800.00),
(2, 'Seaside Retreat', '202 Coastal Dr.', 'Seaside', 'FL', '32124', '202', 1100, 2, 2, 4, 1400.00);

-- Inserting sample data into RENTAL_AGREEMENT table
INSERT INTO RENTAL_AGREEMENT (RENTER_NUM, FIRST_NAME, MIDDLE_INITIAL, LAST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, TELEPHONE, START_DATE, END_DATE, WEEKLY_RENTAL_AMOUNT) VALUES
('R001', 'John', 'A', 'Doe', '123 Maple St.', 'Springfield', 'IL', '62701', '555-1234', '2024-08-01', '2024-08-07', 1200.00),
('R002', 'Jane', 'B', 'Smith', '456 Oak St.', 'Springfield', 'IL', '62702', '555-5678', '2024-08-08', '2024-08-14', 1500.00),
('R003', 'Alice', 'C', 'Johnson', '789 Pine St.', 'Springfield', 'IL', '62703', '555-8765', '2024-08-15', '2024-08-21', 1800.00),
('R004', 'Bob', 'D', 'Williams', '101 Elm St.', 'Springfield', 'IL', '62704', '555-4321', '2024-08-22', '2024-08-28', 1400.00);
