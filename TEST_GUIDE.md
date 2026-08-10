# 🧪 Authentication System - Test Qo'llanma

## Server Boshlash

```bash
python manage.py runserver
```

Server `http://127.0.0.1:8000` da ishga tushadi.

## 🔗 Asosiy URL'lar

| URL | Nomi | Tavsif |
|-----|------|---------|
| `/` | post_list | Barcha postlar ro'yxati |
| `/login/` | login_page | Kirish sahifasi |
| `/logout/` | logout_page | Chiqish |
| `/signup/` | signup_page | Yangi akkaunt yaratish |
| `/home/` | home_page | Bosh sahifa (login kerak) |
| `/account/` | account_settings | Profil sozlamalari (login kerak) |
| `/change-password/` | change_password | Parol o'zgartirish (login kerak) |

## 📝 Test Ssenariylari

### 1️⃣ Ro'yxatdan o'tish

**URL:** `http://127.0.0.1:8000/signup/`

**Test qadamlari:**
1. "Ro'yxatdan o'tish" formasini to'ldirish:
   - Foydalanuvchi nomi: `testuser1`
   - Ism: `Ali`
   - Familiya: `Karimov`
   - Email: `test@example.com`
   - Parol: `SecurePass123`
   - Parolni tasdiqlang: `SecurePass123`
2. "Ro'yxatdan o'tish" tugmasini bosish
3. **Kutiladi:** Login sahifasiga yo'naltirish

### 2️⃣ Kirish

**URL:** `http://127.0.0.1:8000/login/`

**Test qadamlari:**
1. Login formasini to'ldirish:
   - Foydalanuvchi nomi: `testuser1`
   - Parol: `SecurePass123`
2. "Kirish" tugmasini bosish
3. **Kutiladi:** Bosh sahifaga yo'naltirish
4. Header'da "Xush kelibsiz, Ali!" xabari ko'rinish kerak

### 3️⃣ Profil Sozlamalari

**URL:** `http://127.0.0.1:8000/account/` (login kerak)

**Test qadamlari:**
1. Ismi: "Alisher" ga o'zgartirish
2. Email: "alisher@example.com" ga o'zgartirish
3. "Saqlash" tugmasini bosish
4. **Kutiladi:** "Profil muvaffaqiyatli yangilandi!" xabari

### 4️⃣ Parol O'zgartirish

**URL:** `http://127.0.0.1:8000/change-password/` (login kerak)

**Test qadamlari:**
1. "Parolni O'zgartirish" sahifasiga kirish
2. Formani to'ldirish:
   - Eski parol: `SecurePass123`
   - Yangi parol: `NewPassword456`
   - Yangi parolni tasdiqlang: `NewPassword456`
3. "Parolni O'zgartirish" tugmasini bosish
4. **Kutiladi:** "Parol muvaffaqiyatli o'zgartirildi!" va login sahifasiga yo'naltirish

### 5️⃣ Yangi Parol bilan Kirish

**URL:** `http://127.0.0.1:8000/login/`

**Test qadamlari:**
1. Login formasini to'ldirish:
   - Foydalanuvchi nomi: `testuser1`
   - Parol: `NewPassword456`
2. "Kirish" tugmasini bosish
3. **Kutiladi:** Bosh sahifaga muvaffaqiyatli yo'naltirish

### 6️⃣ Chiqish

**URL:** Header'dagi "Chiqish" tugmasi

**Test qadamlari:**
1. Header'dagi "Chiqish" tugmasini bosish
2. **Kutiladi:** Login sahifasiga yo'naltirish va sessiya yakunlanishi

### 7️⃣ Login Talabyoq Sahifalarga Kirish

**Test qadamlari:**
1. Login qilmasdan `/home/` ga kirish
2. **Kutiladi:** Login sahifasiga yo'naltirish

## ❌ Xato Holatlari

### Noto'g'ri Parol
- **Login sahifasida:** Noto'g'ri login ma'lumotlari bilan
- **Kutiladi:** "Foydalanuvchi nomi yoki parol noto'g\'ri!" xabari

### Parol O'zgartirish Xatolari

| Xato | Xabar |
|------|-------|
| Eski parol noto'g'ri | "Eski parol noto'g\'ri!" |
| Yangi parollar mos kelmadi | "Yangi parollar mos kelmadi!" |
| Parol 8 ta belgidan kam | "Parol kamida 8 ta belgidan iborat bo'lishi kerak!" |

### Ro'yxatdan O'tish Xatolari

| Xato | Xabar |
|------|-------|
| Parollar mos kelmadi | "Parollarning mos kelmadi" |
| Parol oson | "Parol juda sodda" |
| Username allaqachon ishlatilgan | "Bu foydalanuvchi nomi allaqachon mavjud" |
| Email allaqachon ishlatilgan | "Bu email allaqachon ishlatilgan" |

## 🔍 Database Tekshirish

```bash
python manage.py dbshell

-- Barcha users ni ko'rish
SELECT * FROM auth_user;

-- Username orqali user qidirish
SELECT * FROM auth_user WHERE username='testuser1';
```

## 📊 Barcha Test Qadamlarini Cheklist

- [ ] Ro'yxatdan o'tish
- [ ] Login
- [ ] Profil ma'lumotlarini tahrirlash
- [ ] Parol o'zgartirish
- [ ] Yangi parol bilan login
- [ ] Chiqish
- [ ] Login talabyoq sahifalarga kirish (yo'naltirish)
- [ ] Noto'g'ri parol bilan login
- [ ] Xatolik xabarlari ko'rish
- [ ] Mobile responsive design

## 💡 Tips

1. Browser console (F12) dan CSRF hatolari tekshiring
2. Database'da direct query orqali user malumotlarini tekshiring
3. Network tab'da request/response kontrollayın
4. Password hashing Django admin'da ko'rish uchun: `python manage.py createsuperuser`
