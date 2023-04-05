kv_m = 7.61
discount = 0.18
kv_m_greened = float(input())
price_of_greened = kv_m_greened * 7.61
discount_put_on = price_of_greened * 0.18
final_price = price_of_greened - discount_put_on
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount_put_on} lv.")