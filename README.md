# Cafeteria System

A web system developed with Flask in Python that allows users to view the cafeteria menu, select products by code and add to the order.

## Requirements

Make sure you have the following requirements installed in your development environment:

- Python 3.x
- Flask (instalável via `pip install flask`)

# Installation

1. Clone the repository to your local environment:

   `git clone https://github.com/joseabrantesjr/PedidosLanchonete.git`

2. Access the project directory:
   
   `cd PedidosLanchonete`

3. Create a virtual environment (optional but recommended) and activate it:
   
   `python3 -m venv venv`
   
   `source venv/bin/activate`

4. Install the project's dependencies:
   
   `pip install -r requirements.txt`

5. Configure the environment variables:
Create an .env file in the project's root directory
Define the following variables in the .env file:

   `FLASK_APP=app.py`

   `FLASK_ENV=development`

6. Run the application:
   
   `flask run`

7. Access the application in your web browser at the following address:
   
    `http://localhost:5000`

To use

When accessing the application, you will see the cafeteria menu with the available products and their respective codes.
Enter the desired product code in the selection box and click "Add to Order" to add the product to the current order.
The order will be displayed below the menu, showing the selected products and the total amount to be paid.
Contribution

Contributions are welcome! If you would like to contribute to this project, please follow the contribution guidelines and submit a request to receive it. To report issues or make suggestions, open an issue.
