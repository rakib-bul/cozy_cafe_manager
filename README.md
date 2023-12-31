# Cozy Cafe
![cozy cafe](https://github.com/rakib-bul/cozy_cafe_manager/blob/main/cozy_01.png)

<div align="center"> A simple lightweight POS system for small cafe and fastfood shop.</div>

<div align="center"> During my time in the E-commerce course for Management Information Systems, I had the wonderful opportunity to collaborate with five other talented students on an exciting group assignment. Our mission was to create a food cart on campus and operate it as a small cafe and fast-food shop. To streamline our sales and keep track of our business transactions, I took the initiative to develop a delightful and user-friendly Point of Sale (POS) system, which I lovingly named "Cozy Cafe." </div>

<div align="center">The idea behind Cozy Cafe was to keep it simple and lightweight, tailored specifically for the needs of small cafes and fast-food shops like ours. With a passion for programming and a love for Python, I led the development process and crafted an efficient POS system that would make our daily operations a breeze.In the backend, I opted to use Postgresql to store all the essential data. However, I also ensured that the system was versatile enough to accommodate other popular database options like Sqlite or MySQL, giving us the flexibility to adapt as per our requirements. </div>

<div align="center"> The development journey was both challenging and rewarding. I worked tirelessly to make the user interface intuitive, allowing our team to quickly process orders, track sales, and manage the menu effortlessly. Cozy Cafe became the heartbeat of our little food cart, empowering us to provide excellent service to our fellow students and faculty.
While Cozy Cafe started as a personal project for our group assignment, it quickly became an essential tool in our entrepreneurial endeavor. This experience not only honed my technical skills in Python and database management but also instilled in me a profound appreciation for the intersection of technology and business.</div>

<div align="center"> Looking back, I cherish the memories of our bustling food cart, where Cozy Cafe played a vital role in fostering a warm and inviting atmosphere. The project not only taught me about software development but also about collaboration, creativity, and the joy of bringing innovative solutions to real-life challenges.</div>


<<<<<<< Updated upstream
### Setting Up PostgreSQL
1.Create Database:
`CREATE DATABASE cozy_cafe;`

2.Connect to the cozy_cafe database:
`\c cozy_cafe;`

3.Create the employees table:
`CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL
);`

4.Create the menu table:
`CREATE TABLE menu (
    id SERIAL PRIMARY KEY,
    item VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);`

5.Create the transactions table:
`CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    emp_id INT NOT NULL REFERENCES employees(id),
    item_id INT NOT NULL REFERENCES menu(id),
    quantity INT NOT NULL,
    total_price NUMERIC(10, 2) NOT NULL
);`

**You will need python3 and tkinter to run the program***




=======
>>>>>>> Stashed changes


