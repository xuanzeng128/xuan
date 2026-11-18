# 1. 原始資料：保留文字資料，另外建立整理後的變數。
event_name = "  WEEKEND DINNER  "
meal_amount = " NT$1,200 "
people = "4"

service_rate = 0.10
discount = 100
budget_per_person = 300

# 2. 整理聚餐名稱。
clean_event_name = event_name.strip().lower()

# 3. 清理餐費文字，再轉換餐費與人數的型別。
clean_meal_text = meal_amount.replace("NT$", "").replace(",", "").replace(" ", "")
meal_value = float(clean_meal_text)
people_count = int(people)

# 4. 先按原始餐費計算服務費，再扣除折價券。
service_fee = meal_value * service_rate
total_amount = meal_value + service_fee - discount
amount_per_person = total_amount / people_count

# 5. 比較結果直接保存為 bool。等於預算時不算超過。
is_over_budget = amount_per_person > budget_per_person

# 6. 輸出時才將金額格式化為兩位小數。
print(f"聚餐名稱：{clean_event_name}")
print(f"原始餐費：{meal_value:.2f} 元")
print(f"服務費：{service_fee:.2f} 元")
print(f"折價券：{discount:.2f} 元")
print(f"應付總額：{total_amount:.2f} 元")
print(f"分攤人數：{people_count} 人")
print(f"每人費用：{amount_per_person:.2f} 元")
print(f"每人預算：{budget_per_person:.2f} 元")
print(f"是否超過預算：{is_over_budget}")
