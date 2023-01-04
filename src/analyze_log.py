import csv


def get_order_frequencies(orders, key_order, client):
    filtered_orders = ([order[key_order] for order in orders
                        if order["cliente"] == client])

    frequencies = ({item: filtered_orders.count(item)
                    for item in filtered_orders})

    return frequencies


def read_csv_orders(path_to_file):
    is_csv = path_to_file.endswith('.csv')
    if not is_csv:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r") as f:
            content = csv.reader(f)
            orders = ([{"cliente": c[0], "pedido": c[1],
                      "dia": c[2]} for c in content])
            return orders

    except FileNotFoundError:
        pass


def get_marias_most_wanted(orders):
    marias_frequencies = get_order_frequencies(orders, "pedido", "maria")

    sorted_frequencies = (sorted(marias_frequencies.items(),
                                 key=lambda f: f[1], reverse=True))

    most_wanted, _ = sorted_frequencies[0]

    return most_wanted


def arnaldo_hamburger_freq(orders):
    arnaldos_frequencies = get_order_frequencies(orders, "pedido", "arnaldo")

    hamburger_count = (arnaldos_frequencies["hamburguer"]
                       if "hamburguer" in arnaldos_frequencies.keys() else 0)

    return hamburger_count


def joaos_less_wanted(orders, order_key):
    joaos_frequencies = get_order_frequencies(orders, order_key, "joao")

    all_options = [order[order_key]
                   for order in orders]

    never_ordered = set([option for option in all_options
                         if option not in joaos_frequencies.keys()])

    return never_ordered


def analyze_log(path_to_file):
    orders = read_csv_orders(path_to_file)
    if not orders:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    marias_most_wanted = get_marias_most_wanted(orders)
    arnaldos_hamburgers = arnaldo_hamburger_freq(orders)
    joaos_never_ordered = joaos_less_wanted(orders, "pedido")
    joaos_never_attended = joaos_less_wanted(orders, "dia")

    lines = ([f"{marias_most_wanted}\n", f"{arnaldos_hamburgers}\n",
              f"{joaos_never_ordered}\n", f"{joaos_never_attended}"])

    with open("data/mkt_campaign.txt", "w") as mkt:
        mkt.writelines(lines)
