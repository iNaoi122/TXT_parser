from dataclasses import dataclass
from pathlib import Path
from typing import List
from fpdf import FPDF
from datetime import date

columnNameList = ["Наименование", "Серийные номера", "Количество", "Цена", "Сумма"]


class PDF(FPDF):
    def __init__(self):
        super(PDF, self).__init__()
        self.width_line = 35
        self.height_line = 7
        self.total_quantity = 0
        self.total_sum = 0
        self.add_page()
        self.set_top_margin(0)
        self.set_auto_page_break(True, 0)
        try:
            self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
            self.set_font("DejaVu", style="", size=10)
        except:
            print("Файл кодировок не найден")

    # принимает данные для записи в пдф

    def write_data_in_pdf(self, order):
        if order is None:
            print("Order is None")
        else:
            self.cell(180, 0, f"Накладная № {order.id} {date.today().strftime('%d.%m.%Y')}", align="C", ln=1)
            self.cell(180, 10, "Выдача товара на реализацию", align="C", ln=1)

            # Меняем шрифт для наглядности
            self.set_font("DejaVu", style="", size=10)
            self.cell(10, 10, "Кому: " + order.customer.name, align="L", ln=1)

            # Создаем заголовки таблицы
            for columnName in columnNameList:
                self.cell(self.width_line, self.height_line, columnName, align="C", border=1)
            self.ln()

            # Смена шрифта
            self.set_font("DejaVu", style="", size=self.height_line)

            # Заполнение таблицы
            for item in order.items:

                # Имя продукта
                self.cell(self.width_line, self.height_line * item.quantity, item.product.name,
                          align="L", border=1)

                # IMEI продукта
                for imei in item.imeis:
                    self.cell(self.width_line, self.height_line, imei.imei, align="R", border=1, ln=2)

                self.set_x_y(item.quantity)

                # Число продуктов
                self.cell(self.width_line, self.height_line * item.quantity, f"{item.quantity}", border=1)
                # Цена продукта
                self.cell(self.width_line, self.height_line * item.quantity,
                          str(item.price)[:-2] + "," + str(item.price)[len(str(item.price)) - 2:],
                          border=1)
                # Сумма продукта
                self.cell(self.width_line, self.height_line * item.quantity, str(item.quantity * item.price)[:-2] +
                          "," + str(item.price * item.quantity)[len(str(item.price * item.quantity)) - 2:], border=1)

                self.total_quantity += item.quantity
                self.total_sum += item.quantity * item.price

                self.ln()

            # Расчет значений Итого
            self.cell(self.width_line, self.height_line, "Итого", border=1)
            self.set_xy(self.get_x() + self.width_line, self.get_y())
            self.cell(self.width_line, self.height_line, f"{self.total_quantity}", border=1)
            self.set_xy(self.get_x() + self.width_line, self.get_y())
            self.cell(self.width_line, self.height_line,
                      str(self.total_sum)[:-2] + "," + str(self.total_sum)[len(str(self.total_sum)) - 2:], border=1)
            self.output("Task.pdf")

    # Вычисляем позицию для переноса строки, после заполнения IMEI
    def set_x_y(self, quantity):
        x = self.get_x() + self.width_line
        y = self.get_y() - self.height_line * quantity
        self.set_xy(x, y)


# покупа    тель
@dataclass
class Customer:
    name: str


# товар
@dataclass
class Product:
    name: str


# серийный номер
@dataclass
class Imei:
    imei: str


# позиция заказа
@dataclass
class OrderItem:
    product: Product
    quantity: int
    price: int
    imeis: List[Imei]


# заказ
@dataclass
class Order:
    id: int
    customer: Customer
    items: List[OrderItem]


product1 = Product(name='iPhone 12 Pro 256 White')
product2 = Product(name='iPhone 12 64 Green')
product3 = Product(name='Apple Watch 45 S7 Starlight')

order = Order(
    id=1,
    customer=Customer(name='Иванов Иван'),
    items=[
        OrderItem(
            product=product1,
            quantity=5,
            price=2000000,
            imeis=[
                Imei(imei='136291092200748'),
                Imei(imei='598042927964944'),
                Imei(imei='941229886882327'),
                Imei(imei='995291113719735'),
                Imei(imei='443108326690001')
            ]
        ),
        OrderItem(
            product=product2,
            quantity=7,
            price=3000000,
            imeis=[
                Imei(imei='923194674201781'),
                Imei(imei='713244626318060'),
                Imei(imei='561048995687396'),
                Imei(imei='030671718035247'),
                Imei(imei='253205665836920'),
                Imei(imei='085553524878853'),
                Imei(imei='661290424039104')
            ]
        ),
        OrderItem(
            product=product3,
            quantity=20,
            price=1000000,
            imeis=[
                Imei(imei='941497937575938'),
                Imei(imei='670755030117478'),
                Imei(imei='471900343989819'),
                Imei(imei='671887929353095'),
                Imei(imei='429936914213026'),
                Imei(imei='448553082986003'),
                Imei(imei='275765380548980'),
                Imei(imei='316933615250086'),
                Imei(imei='498103090078384'),
                Imei(imei='692862730900836'),
                Imei(imei='956637184824914'),
                Imei(imei='524631242649151'),
                Imei(imei='021124913925817'),
                Imei(imei='778693161112415'),
                Imei(imei='801473093145394'),
                Imei(imei='535544255712689'),
                Imei(imei='694225972068421'),
                Imei(imei='833261756140789'),
                Imei(imei='571054652928194'),
                Imei(imei='718572287816578')
            ]
        ),
        OrderItem(
            product=product1,
            quantity=5,
            price=2000000,
            imeis=[
                Imei(imei='136291092200748'),
                Imei(imei='598042927964944'),
                Imei(imei='941229886882327'),
                Imei(imei='995291113719735'),
                Imei(imei='443108326690001')
            ]
        ),
        OrderItem(
            product=product3,
            quantity=20,
            price=1555555,
            imeis=[
                Imei(imei='941497937575938'),
                Imei(imei='670755030117478'),
                Imei(imei='471900343989819'),
                Imei(imei='671887929353095'),
                Imei(imei='429936914213026'),
                Imei(imei='448553082986003'),
                Imei(imei='275765380548980'),
                Imei(imei='316933615250086'),
                Imei(imei='498103090078384'),
                Imei(imei='692862730900836'),
                Imei(imei='956637184824914'),
                Imei(imei='524631242649151'),
                Imei(imei='021124913925817'),
                Imei(imei='778693161112415'),
                Imei(imei='801473093145394'),
                Imei(imei='535544255712689'),
                Imei(imei='694225972068421'),
                Imei(imei='833261756140789'),
                Imei(imei='571054652928194'),
                Imei(imei='718572287816578')
            ]
        ),
    ]
)


# создани пдф накладной для заказа
def export_order_pdf(order: Order) -> Path:
    pd = PDF()
    pd.write_data_in_pdf(order)


export_order_pdf(order)
