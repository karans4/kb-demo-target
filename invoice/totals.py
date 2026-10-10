from decimal import Decimal, ROUND_HALF_UP


def line_total(quantity: int, unit_price: str, discount_pct: int = 0) -> Decimal:
    gross = Decimal(unit_price) * quantity
    discount = gross * Decimal(discount_pct) / 100
    return (gross - discount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def invoice_total(lines: list[tuple[int, str, int]], tax_pct: int = 0) -> Decimal:
    subtotal = sum(line_total(q, p, d) for q, p, d in lines)
    # Calculate tax as a percentage of the subtotal with proper rounding
    tax = (subtotal * Decimal(tax_pct) / Decimal(100)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    return (subtotal + tax).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
