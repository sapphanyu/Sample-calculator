🔎 Flow การทำงาน

main() เริ่มทำงาน → print เมนู

รอ input จากผู้ใช้

ถ้า quit → จบการทำงาน

ถ้า calculate → เรียก get_numbers_and_operator()

get_numbers_and_operator()

รับ input เป็น (num1 operator num2) เช่น 3 + 5

แยกด้วย .split() → ได้ parts = [num1, operator, num2]

เช็คว่า operator ถูกต้อง + แปลง num1, num2 → float

return (num1, num2, operator)

main() → เรียกฟังก์ชันที่ตรงกับ operator → print ผลลัพธ์

กลับไปเริ่ม loop ใหม่