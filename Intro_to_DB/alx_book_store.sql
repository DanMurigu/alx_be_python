CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id (FOREIGN KEY REFERENCES Authors Table),
    price DOUBLE NOT NULL,
    publication_date DATE,
);

CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    autor_name VARCHAR(215) NOT NULL,
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) UNIQUE NOT NULL,
    address TEXT NOT NULL,
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT FOREIGN KEY REFERENCES Customers table,
    order_date DATE NOT NULL, 
);
  
CREATE TABLE Order_Details (
    orderdetailid INT PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES Orders table,
    book_id INT FOREIGN KEY REFERENCES Books table,
    quantity DOUBLE NOT NULL,
);
