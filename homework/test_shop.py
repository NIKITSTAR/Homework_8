class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        Верните True, если количество продукта больше или равно запрашиваемому,
        и False в обратном случае.
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        Метод покупки.
        Проверяет количество продукта с использованием метода check_quantity.
        Если продуктов не хватает, выбрасывается исключение ValueError.
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError('Не достаточно продукта')

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    """

    def __init__(self):
        # По умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество.
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция.
        Если remove_count больше, чем количество продуктов в позиции, удаляется вся позиция.
        """
        if product in self.products:
            if remove_count is None or self.products[product] <= remove_count:
                del self.products[product]
            else:
                self.products[product] -= remove_count

    def clear(self):
        """
        Очищает корзину.
        """
        self.products.clear()

    def get_total_price(self) -> float:
        """
        Возвращает общую стоимость товаров в корзине.
        """
        total = 0
        for product, count in self.products.items():
            total += product.price * count
        return total

    def buy(self):
        """
        Метод покупки.
        Проверяет наличие товаров на складе и обновляет их количество.
        Если какого-либо товара недостаточно, выбрасывается исключение ValueError.
        """
        for product, count in self.products.items():
            if not product.check_quantity(count):
                raise ValueError(f'Не достаточно продукта: {product.name}')

        for product, count in self.products.items():
            product.buy(count)

        self.clear()