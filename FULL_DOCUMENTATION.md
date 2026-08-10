# 🔐 Blog Autentifikatsiya Tizimi - Toʻliq Qoʻllanma

## 📋 Umumiy Koʻrinish

Django Blog platformasida toʻliq autentifikatsiya tizimi yaratildi. Foydalanuvchilar roʻyxatdan oʻtish, kirish, profil tahrirlash va parol oʻzgartirish imkoniyatiga ega.

## 🎯 Asosiy Xususiyatlar

### ✅ Autentifikatsiya
- **Ro'yxatdan o'tish** - Email, ismi, parol bilan yangi akkaunt yaratish
- **Kirish** - Foydalanuvchi nomi va parol bilan tizimga kirish
- **Chiqish** - Sessiyani yakunlash

### ✅ Akkaunt Boshqarish
- **Profil Tahrirlash** - Ismi, familiyasi, email, username o'zgartirish
- **Parol O'zgartirish** - Xavfli parol oʻzgartirish (eski parol tekshiriladi)
- **Hatolik Tekshirish** - Toʻliq va qulay xatolik xabarlari

### ✅ Security Features
- Django User modeli (password hashing bilan)
- CSRF protection
- SQL injection himoyasi
- XSS himoyasi
- Session management
- Login decorators

## 📁 Fayllar Strukturasi

```
Blog/
├── blog_app/
│   ├── views.py          ✅ 6 ta yangi function/class
│   ├── forms.py          ✅ 4 ta yangi forma
│   ├── urls.py           ✅ 7 ta yangi URL pattern
│   └── models.py         (o'zgarmadi)
│
├── templates/blog/
│   ├── base.html         ✅ Yangilandi (navigatsiya)
│   ├── home.html         ✅ Yangi
│   └── auth/
│       ├── login.html    ✅ Yangi
│       ├── signup.html   ✅ Yangi
│       ├── account_settings.html  ✅ Yangi
│       └── change_password.html   ✅ Yangi
│
├── static/css/
│   └── auth.css          ✅ Yangi (730 qator)
│
├── config/
│   └── settings.py       ✅ Yangilandi (LOGIN_URL qo'shildi)
│
└── AUTH_SYSTEM_README.md ✅ Yangi
└── TEST_GUIDE.md         ✅ Yangi
```

## 🔧 Views (blog_app/views.py)

### 1. `login_page(request)` - Kirish
```python
- GET: Login formasini ko'rish
- POST: Username va parolni tekshirish
- Xato: Xabar ko'rsatish
- Muvaffaqiyat: home_page ga yo'naltirish
```

### 2. `logout_page(request)` - Chiqish
```python
- Sessiyani yakunlash
- login_page ga yo'naltirish
```

### 3. `home_page(request)` - Bosh sahifa
```python
- @login_required decorator bilan himoyalangan
- Oxirgi 5 ta publishdan postlarni ko'rsatish
- Foydalanuvchini salomlash
```

### 4. `SignUpView` - Ro'yxatdan o'tish
```python
- class-based view
- CustomUserCreationForm ishlatadi
- Muvaffaqiyat: login_page ga yo'naltirish
```

### 5. `account_settings(request)` - Profil sozlamalari
```python
- @login_required decorator
- GET: Hozirgi profil ma'lumotlari
- POST: Profil yangilash
- Xato: Xabar ko'rsatish
```

### 6. `change_password(request)` - Parol o'zgartirish
```python
- @login_required decorator
- Eski parol tekshirish
- Yangi parollarning mos kelishini tekshirish
- Parol minimum 8 ta belgisi
- Muvaffaqiyat: login_page ga yo'naltirish
```

## 📝 Formalar (blog_app/forms.py)

### CustomUserCreationForm
```python
- Maydonlar: username, first_name, last_name, email, password1, password2
- UserCreationForm'dan inherited
- Uzbek tilidagi labellar
```

### LoginForm
```python
- Maydonlar: username, password
- Custom form (ModelForm emas)
```

### UserAccountForm
```python
- Maydonlar: username, first_name, last_name, email
- Parol o'zgartish yo'q
- UserChangeForm'dan inherited
```

### ChangePasswordForm
```python
- Maydonlar: old_password, new_password1, new_password2
- Parol tekshirish (views'da)
```

## 🎨 HTML Shablonlar

### login.html
- CSRF token
- Form fieldslar
- Ro'yxatdan o'tish linki
- Xatolik xabarlari

### signup.html
- Barcha kerakli maydonlar
- Password matching
- Login linki
- Validatsiya xabarlari

### account_settings.html
- Profil tahrirlash formasi
- Parol o'zgartirish linki
- Orqaga va chiqish tugmalari
- Muvaffaqiyat xabarlari

### change_password.html
- Eski parol
- Yangi parol
- Parol talablari
- Orqaga tugmasi

### home.html
- Foydalanuvchini salomlash
- Yangi postlarni ko'rsatish
- Navigation tugmalari
- Yosh post detallari

### base.html (yangilandi)
- Header navigationga user linkalari qo'shildi
- Login/logout linkalari
- Foydalanuvchi ismini ko'rsatish
- Mobil responsive

## 🎨 CSS (static/css/auth.css)

- 7383 qator CSS kodi
- Barcha autentifikatsiya sahifalari uchun
- Responsive design (mobile-friendly)
- Dark theme (site dizayniga mos)
- Smooth animatsiyalar

### Asosiy Komponentlar:
- `.header-nav` - Header navigationni
- `.form-group` - Forma gruppalari
- `.btn-primary`, `.btn-secondary` - Tugmalar
- `.alert` - Xabarlar
- `.auth-container` - Auth sahifalari
- `.account-container` - Account sahifalari

## 🔗 URL Routing (blog_app/urls.py)

| URL | View | Name |
|-----|------|------|
| `/` | PostListView | post_list |
| `/login/` | login_page | login_page |
| `/logout/` | logout_page | logout_page |
| `/signup/` | SignUpView | signup_page |
| `/home/` | home_page | home_page |
| `/account/` | account_settings | account_settings |
| `/change-password/` | change_password | change_password |
| `/<year>/<month>/<day>/<slug>/` | post_detail | post_detail |
| `/<post_id>/share/` | post_share | post_share |

## ⚙️ Settings (config/settings.py)

Qo'shilganlar:
```python
LOGIN_URL = 'blog_app:login_page'           # Login decorator uchun
LOGIN_REDIRECT_URL = 'blog_app:home_page'   # Login dan keyin
```

## 🔒 Security Features

### 1. Password Security
```python
- Django's make_password() automatik hashing
- check_password() bilan tekshirish
- Minimum 8 ta belgi
- Parol matching validation
```

### 2. CSRF Protection
```html
{% csrf_token %}  <!-- Barcha POST formlarda -->
```

### 3. SQL Injection Protection
```python
# Django ORM ishlatiladi - parameterized queries
user = User.objects.get(username=username)
```

### 4. Session Management
```python
# Django session middleware
login(request, user)  # Session yaratish
logout(request)       # Session yakunlash
request.user          # Hozirgi foydalanuvchi
```

### 5. Access Control
```python
@login_required(login_url='blog_app:login_page')
def account_settings(request):  # Login kerak
```

## 📊 Database Schema

Django built-in `auth_user` jadval ishlatiladi:

```sql
auth_user:
├── id (PK)
├── username (UNIQUE)
├── first_name
├── last_name
├── email
├── password (HASHED)
├── is_staff
├── is_active
├── is_superuser
├── last_login
└── date_joined
```

## 🚀 Foydalanish

### 1. Server Boshlash
```bash
python manage.py runserver
```

### 2. Ro'yxatdan O'tish
```
http://127.0.0.1:8000/signup/
```

### 3. Kirish
```
http://127.0.0.1:8000/login/
```

### 4. Profil Sozlamalari
```
http://127.0.0.1:8000/account/
```

### 5. Parol O'zgartirish
```
http://127.0.0.1:8000/change-password/
```

### 6. Chiqish
```
Header'dagi "Chiqish" tugmasi
```

## 🧪 Testing

Detailed test guide uchun: `TEST_GUIDE.md`

Test qadamlari:
1. ✅ Ro'yxatdan o'tish
2. ✅ Kirish
3. ✅ Profil tahrirlash
4. ✅ Parol o'zgartirish
5. ✅ Yangi parol bilan kirish
6. ✅ Chiqish
7. ✅ Login talabyoq sahifalarga kirish
8. ✅ Xatolik holatlari

## 📞 Foydalanuvchi Xabarlar (Uzbek Tilida)

### Success Messages:
- ✅ "Profil muvaffaqiyatli yangilandi!"
- ✅ "Parol muvaffaqiyatli o'zgartirildi!"

### Error Messages:
- ❌ "Foydalanuvchi nomi yoki parol noto'g'ri!"
- ❌ "Eski parol noto'g'ri!"
- ❌ "Yangi parollar mos kelmadi!"
- ❌ "Parol kamida 8 ta belgidan iborat bo'lishi kerak!"

## 📱 Responsive Design

- Desktop (1200px+) - Full layout
- Tablet (768px-1199px) - Adjusted layout
- Mobile (<768px) - Optimized layout
- Barcha sahifalar mobile-friendly

## 🎯 Keyingi Qadam (Opsional)

1. Email verification
2. Password reset (forgot password)
3. User profile image
4. User bio/about
5. Social authentication
6. Two-factor authentication
7. Activity log
8. User permissions/roles

## ✅ Bajarilgan Ishlar Checklisti

- [x] Login view
- [x] Logout view  
- [x] Signup view
- [x] Home page (protected)
- [x] Account settings
- [x] Change password
- [x] All forms with validation
- [x] HTML templates (4)
- [x] CSS styling
- [x] URL routing
- [x] Error handling
- [x] Success messages
- [x] Database integration
- [x] Security features
- [x] Responsive design
- [x] Uzbek language support

## 📚 Django Dokumentatsiya

- https://docs.djangoproject.com/en/6.1/topics/auth/
- https://docs.djangoproject.com/en/6.1/ref/contrib/auth/
- https://docs.djangoproject.com/en/6.1/topics/forms/

---

**Yaratildi:** 18 Avgust 2026
**Status:** ✅ Tayyor
**Test:** ✅ Muvaffaqiyatli
