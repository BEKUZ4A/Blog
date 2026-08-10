# 🚀 Quick Start - Blog Authentication System

## ⚡ Immediate Start

```bash
cd "C:\Users\behru\OneDrive\Desktop\New folder (3)\Blog"
python manage.py runserver
```

📱 Open: **http://127.0.0.1:8000/**

---

## 🎯 Main Features

### ✅ For Visitors (Not Logged In)
- See all posts on homepage
- Click "Kirish" to login
- Click "Ro'yxatdan o'tish" to signup

### ✅ For Users (Logged In)
- See username in header
- Click ⚙️ to change profile
- Click "Chiqish" to logout
- Access `/change-password/` for password change

### ✅ Key Pages
| Page | URL | Access |
|------|-----|--------|
| Homepage | `/` | Everyone |
| Login | `/login/` | Not logged in |
| Register | `/signup/` | Not logged in |
| Settings | `/account/` | Logged in only |
| Change Password | `/change-password/` | Logged in only |
| Post Detail | `/<year>/<month>/<day>/<slug>/` | Everyone |

---

## 🔐 User Data Stored

- Username (unique)
- First Name (Ismi)
- Last Name (Familiyasi)
- Email (unique)
- Password (encrypted)

---

## 🎨 Header Layout

```
[Logo: IT-NEWS]  [User Name]  [⚙️]  [Logout]
```

Or if not logged in:
```
[Logo: IT-NEWS]  [Login]  [Signup]
```

---

## 🧪 Test Flow

1. Go to `/signup/` → Create account
2. Go to `/login/` → Login with credentials
3. See username in header
4. Click ⚙️ → Change name, email
5. Click "Chiqish" → Back to homepage

---

## 📝 Important Notes

✅ **Clean & Simple** - No extra pages, everything in header
✅ **Responsive** - Works on mobile & desktop
✅ **Secure** - Passwords encrypted, CSRF protected
✅ **Uzbek Ready** - All labels in Uzbek
✅ **Database Integrated** - User data stored in SQLite

---

## 🛠️ Admin Panel

```bash
python manage.py createsuperuser
# Then go to: http://127.0.0.1:8000/admin/
```

---

**Status:** ✅ READY TO USE
