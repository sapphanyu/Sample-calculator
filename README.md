# Simple CLI & Web Calculator

## คำอธิบาย
โปรแกรมสำหรับการคำนวณทางคณิตศาสตร์เบื้องต้น รองรับตัวดำเนินการ `+`, `-`, `*`, `/`, `**` ในรูปแบบ `num1 operator num2` เช่น `1 + 2`  

โปรแกรมสามารถใช้งานได้ทั้งแบบ CLI (ใน terminal) และแบบเว็บ (GUI) ผ่าน Flask

---

## วิธีติดตั้งและรัน

1. **ดาวน์โหลดโปรเจกต์**
   - โหลดโค้ดจาก GitHub ลงเครื่องของคุณ

2. **ติดตั้ง dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **รันโปรแกรมแบบ CLI**
   ```bash
   python src/main.py
   ```
   - จะมีข้อความแสดงใน terminal
   - ผู้ใช้สามารถกรอกคำสั่ง เช่น `calculate`, `history`, `clear history`, หรือ `quit`

4. **รันโปรแกรมแบบเว็บ (GUI)**
   ```bash
   python src/app.py
   ```
   - จะปรากฏข้อความใน terminal เช่น:
     ```
     * Serving Flask app 'app'
     * Debug mode: on
     WARNING: This is a development server. Do not use it in production deployment.
     * Running on all addresses (0.0.0.0)
     * Running on http://127.0.0.1:5000
     ```
   - เปิดลิงก์ `http://127.0.0.1:5000` ในเว็บบราวเซอร์
   - กด `CTRL+C` ใน terminal เมื่อต้องการปิดโปรแกรม

5. **รันโปรแกรมด้วย Docker**
   - สร้าง image:
     ```bash
     docker build -t simple-calculator .
     ```
   - รัน container:
     ```bash
     docker run -p 5000:5000 simple-calculator
     ```
   - เปิดลิงก์ `http://127.0.0.1:5000` ในเว็บบราวเซอร์

---

## วิธีใช้งาน

### CLI (main.py)
- รัน `main.py` จะปรากฏข้อความใน terminal
- ผู้ใช้กรอกคำสั่ง:
  - `calculate` → ทำการคำนวณ
  - `history` → แสดงประวัติการคำนวณ
  - `clear history` → ล้างประวัติ
  - `quit` → ออกจากโปรแกรม

### เว็บ (app.py)
- รัน `app.py` แล้วเปิดลิงก์ในเว็บบราวเซอร์
- หน้า Calculator:
  - กรอกโจทย์คำนวณ เช่น `5 + 3`
  - กดปุ่ม `คำนวณ` เพื่อดูผลลัพธ์
- หน้า History:
  - แสดงประวัติการคำนวณทั้งหมด
  - ปุ่ม `Clear History` ลบประวัติทั้งหมด

---

## โครงสร้างโปรเจกต์ (สำคัญ)
```
Sample-calculator/
├─ planning/
│   ├─ flow.md
│   ├─ planning_week 1.md
│   ├─ planning_week 2.md
│   ├─ planning_week 3.md
│   ├─ planning_week 4.md
│   ├─ READMEoid.md
│   └─ วิธีการยิงapiเบื้องต้น.md
├─ src/
│  ├─ templates/
│  ├─ app.py
│  ├─ main.py
│  └─ history.json
├─ static/
├─ Dockerfile
├─ README.md
└─ requirements.txt
```

---

## หมายเหตุ
- ระบบเว็บนี้เป็น **development server** สำหรับทดลองเท่านั้น
- ไม่แนะนำให้ใช้งานใน production โดยตรง
- การรันผ่าน Docker ช่วยให้ตั้งค่าและรันโปรแกรมง่ายขึ้น

