class TrackOrders:
    def __init__(self):
        self.__orders = []

    def __len__(self):
        return len(self.__orders)

    @staticmethod
    def get_order_frequencies(orders, key_order, customer):
        filtered_orders = ([order[key_order] for order in orders
                            if order["customer"] == customer])

        frequencies = ({item: filtered_orders.count(item)
                        for item in filtered_orders})

        return frequencies

    @staticmethod
    def get_sorted_days_frequencies(orders, is_reverse):
        days_visited = ([order["day"] for order in orders])

        frequencies = ({item: days_visited.count(item)
                        for item in days_visited})

        sorted_days_frequencies = (sorted(frequencies.items(),
                                   key=lambda f: f[1], reverse=is_reverse))

        return sorted_days_frequencies

    def add_new_order(self, customer, order, day):
        keys = ("customer", "order", "day")
        order_map = dict(zip(keys, (customer, order, day)))
        self.__orders.append(order_map)

    def get_most_ordered_dish_per_customer(self, customer):
        order_frequencies = (TrackOrders.get_order_frequencies(self.__orders,
                             "order", customer))
        sorted_frequencies = (sorted(order_frequencies.items(),
                              key=lambda f: f[1], reverse=True))

        most_wanted, _ = sorted_frequencies[0]
        return most_wanted

    def get_never_ordered_per_customer(self, customer):
        order_frequencies = (TrackOrders.get_order_frequencies
                             (self.__orders, "order", customer))

        all_options = [order["order"] for order in self.__orders]

        never_ordered = set([option for option in all_options
                             if option not in order_frequencies.keys()])

        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        order_frequencies = (TrackOrders.get_order_frequencies
                             (self.__orders, "day", customer))

        all_options = [order["day"] for order in self.__orders]

        never_visited = set([option for option in all_options
                             if option not in order_frequencies.keys()])

        return never_visited

    def get_busiest_day(self):
        sorted_days_visited = (TrackOrders.get_sorted_days_frequencies
                               (self.__orders, True))
        busiest_day, _ = sorted_days_visited[0]
        return busiest_day

    def get_least_busy_day(self):
        days_visited = (TrackOrders
                        .get_sorted_days_frequencies(self.__orders, False))
        least_busy_day, _ = days_visited[0]
        return least_busy_day
