# Simple CLI & Web Calculator

# คำอธิบาย
 เป็นโปรแกรมสำหรับการคำนวณทางคณิตศาสตร์เบื้องต้น รองรับ +,-,*,/,** ในรูปแบบ num1 operator num2(เช่น 1 + 2)

# วิธีติดตั้งและรัน
 สามารถโหลดโค้ดนี้จาก GitHub ลงเครื่องสามารถรันที่ไฟล์ main.py ในกรณีรันเพียงโค้ด app.py ในกรณีต้องการรันและแสดงผลแบบ gui 

#  วิธีใช้งาน
 เมื่อรันไฟล์ main.py จะปรากฎข้อความใน terminal ผู้ใช้สามารถกรอกข้อมูลตามที่โปรแกรมได้กำหนดไว้

 เมื่อรันไฟล์ app.py ใน vs code จะมีข้อความปรากฎใน terminal ประมาณนี้
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.62.125.161:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 126-511-549

เลือกเปิดลิ้ง Running on http://127.0.0.1:5000 หรือ copy url เปิดในบราวเซอร์ที่ต้องการ
เมื่อต้องการเลิกใช้งาน app.py
ให้กด CTRL+C ใน terminal

ในกรณีรัน Docker
สามารถโหลดโค้ดนี้และรันใน terminal ดังนี้
สร้างdocker
docker build -t simple-calculator .
รันdocker
docker run -p 5000:5000 simple-calculator



 
