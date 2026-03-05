import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

prices = re.findall(r'\d{1,3}(?: \d{3})*,\d{2}', text)

products = re.findall(r'\d+\.\s*(.*?)\n\d+,\d+ x', text, re.DOTALL)
products = [p.strip() for p in products]

def parse_price(p):
    return float(p.replace(" ", "").replace(",", "."))

total_sum = sum(parse_price(p) for p in prices[:-3])

datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})', text)
datetime = datetime_match.group(1) if datetime_match else None

payment_match = re.search(r'(Банковская карта|Наличные|Оплата картой)', text)
payment_method = payment_match.group(1) if payment_match else "Неизвестно"

receipt_data = {
    "products": [{"name": p, "price": parse_price(prices[i])} for i, p in enumerate(products)],
    "total": parse_price(prices[-3]),  
    "date_time": datetime,
    "payment_method": payment_method
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=2))