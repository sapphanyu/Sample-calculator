1.รันไฟล์ app.py ใน vs code

2.ต้องรันคำสั่งใน gitbash เพื่อความชัวร์ในการรันคำสั่ง ยิง api

# เรียก API /calculate (POST)

ตัวอย่าง curl:

curl -X POST http://127.0.0.1:5000/calculate \

-H "Content-Type: application/json" \

-d '{"num1": 5, "num2": 3, "operator": "+"}'

# เรียก API /history (GET)

ดึงประวัติการคำนวณทั้งหมด:

curl http://127.0.0.1:5000/history

# ล้างประวัติ /history (DELETE)

curl -X DELETE http://127.0.0.1:5000/history

# หมายเหตุสำหรับ Postman

Method: POST / GET / DELETE ตามตัวอย่าง

URL: http://127.0.0.1:5000/calculate หรือ /history

Headers (สำหรับ POST): Content-Type: application/json

Body (raw JSON) สำหรับ POST /calculate เช่น:

{
  "num1": 7,
  "num2": 2,
  "operator": "*"
}
