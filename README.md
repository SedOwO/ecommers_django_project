# Django E-commerce Project

This is a simple e-commerce application built with Django. It includes basic features such as item listing, item details, cart management, and checkout.

## Features

- Item Listing
- Item Details
- Add to Cart
- Reduce Item Quantity in Cart
- Remove Item from Cart
- Checkout

## Installation

1. **Clone the repository**

    ```sh
    git clone https://github.com/your-username/ecommerce.git
    cd ecommerce
    ```

2. **Create a virtual environment and activate it**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run migrations**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser to access the admin panel**

    ```sh
    python manage.py createsuperuser
    ```

6. **Start the development server**

    ```sh
    python manage.py runserver
    ```

7. **Access the application**

    Open your browser and navigate to `http://127.0.0.1:8000/` to access the application. You can access the admin panel at `http://127.0.0.1:8000/admin/`.

## Project Structure

- `ecommerce/`: Main project directory.
  - `settings.py`: Project settings.
  - `urls.py`: URL routing.
  - `wsgi.py`: WSGI configuration.
- `shop/`: Application directory.
  - `admin.py`: Admin configuration.
  - `models.py`: Database models.
  - `urls.py`: URL routing for the application.
  - `views.py`: View functions.
  - `templates/shop/`: HTML templates.

## Models

### Category

- `name`: CharField

### Item

- `name`: CharField
- `description`: TextField
- `image`: ImageField
- `category`: ForeignKey to Category
- `price`: DecimalField

## URL Patterns

- `/`: Item list view
- `/item/<int:pk>/`: Item detail view
- `/cart/`: Cart detail view
- `/checkout/`: Checkout view
- `/add-to-cart/<int:pk>/`: Add item to cart
- `/reduce_quantity/<int:item_id>/`: Reduce item quantity in cart
- `/remove_item/<int:item_id>/`: Remove item from cart

## Views

- `item_list`: Displays a list of items with search functionality.
- `item_detail`: Displays the details of a single item.
- `cart_detail`: Displays the contents of the cart.
- `checkout`: Displays the checkout page.
- `add_to_cart`: Adds an item to the cart.
- `reduce_quantity`: Reduces the quantity of an item in the cart.
- `remove_item`: Removes an item from the cart.

## Static and Media Files

- `STATIC_URL`: URL for static files.
- `MEDIA_URL`: URL for media files.
- `MEDIA_ROOT`: Root directory for media files.

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
