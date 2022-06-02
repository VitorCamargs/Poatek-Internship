class FuelPump:
    def __init__(self, price, quantity):
        if price >= 0:
            self.__fuel_price = price
        else:
            self.__fuel_price = None
        if quantity >= 0:
            self.__fuel_quantity = quantity
        else:
            self.__fuel_quantity = None

        self.__gains = float(0)
        self.__sold_fuel = float(0)

    def set_price(self, price: float) -> bool:
        if price >= 0:
            self.__fuel_price = price
            return True
        return False

    def set_quantity(self, quantity: float) -> bool:
        if quantity >= 0:
            self.__fuel_quantity = quantity
            return True
        return False

    def get_price(self) -> float:
        price = self.__fuel_price
        return price

    def get_quantity(self) -> float:
        quantity = self.__fuel_quantity
        return quantity

    def get_gains(self) -> float:
        gains = self.__gains
        return gains

    def reset_gains(self):
        self.__gains = float(0)
        return

    def update_gains(self, price: float):
        self.__gains += price
        return

    def get_amount_sold(self) -> float:
        sold = self.__sold_fuel
        return sold

    def reset_amount_sold(self):
        self.__sold_fuel = float(0)
        return

    def update_amount_sold(self, litters: float):
        self.__sold_fuel += litters
        return

    def fill_with_price(self, price: float) -> float:
        if self.__fuel_price is None:
            return 0
        to_be_pumped = price / self.__fuel_price  # calculate the amount of litters for the given price
        if self.set_quantity(self.__fuel_quantity - to_be_pumped):  # try to update the quantity
            self.update_gains(price)
            self.update_amount_sold(to_be_pumped)
            return to_be_pumped
        else:
            return 0

    def fill_with__litters(self, litters: float) -> float:
        if self.__fuel_price is None:
            return 0
        final_price = litters * self.__fuel_price  # calculate the final price
        if self.set_quantity(self.__fuel_quantity - litters):  # try to update the quantity
            self.update_gains(final_price)
            self.update_amount_sold(litters)
            return final_price
        else:
            return 0


if __name__ == '__main__':
    # testes
    pump = FuelPump(6.7, 100)
    print(f"First user try to fill with 52 litters. The operation return was: {pump.fill_with__litters(52)}\n")
    print(f"Second user Try to fill with price with 100$. The operation return was: {pump.fill_with_price(100)}\n")
    print(f"third user try to fill with 40 litters. The operation return was: {pump.fill_with__litters(40)}\n")
    print(f"After three operations the final earnings of the fuel pump were: {pump.get_gains()} $\n"
          f"and the amount of fuel sold were: {pump.get_amount_sold()} L")
