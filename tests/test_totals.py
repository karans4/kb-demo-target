from decimal import Decimal

from invoice import invoice_total, line_total


def test_line_total_applies_discount():
    assert line_total(3, "19.99", 10) == Decimal("53.97")


def test_invoice_total_adds_tax():
    lines = [(2, "10.00", 0), (1, "5.50", 0)]
    assert invoice_total(lines, tax_pct=8) == Decimal("27.54")
