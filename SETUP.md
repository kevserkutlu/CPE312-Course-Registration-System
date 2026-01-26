# 🚀 Quick Start Guide

## One-Command Setup

### macOS / Linux:
```bash
cd CPE312-Course-Registration-System
chmod +x run.sh
./run.sh
```

### Windows:
```cmd
cd CPE312-Course-Registration-System
run.bat
```

That's it! The script will:
1. ✅ Create a virtual environment
2. ✅ Install all dependencies
3. ✅ Check PostgreSQL connection
4. ✅ Start the Flask web server
5. ✅ Display the web URL

## 🌐 Access the Application

Once started, open your browser and go to:
```
http://localhost:5001
```

## ❌ Troubleshooting

### PostgreSQL not running?

**macOS:**
```bash
brew services start postgresql
```

**Linux (Ubuntu/Debian):**
```bash
sudo systemctl start postgresql
```

**Windows:**
- Open Services (services.msc)
- Find PostgreSQL and start it
- Or use pgAdmin GUI

### Port 5001 already in use?

**macOS/Linux:**
```bash
lsof -i :5001
kill -9 <PID>
./run.sh
```

**Windows:**
```cmd
netstat -ano | findstr :5001
taskkill /PID <PID> /F
run.bat
```

### Dependencies not installing?

```bash
source .venv/bin/activate  # macOS/Linux
pip install flask sqlalchemy psycopg2-binary
python3 web.py
```

## 📝 Default PostgreSQL Credentials

The system uses these default credentials. If your setup differs, modify `src/config/database/db.py`:

```python
DB_USER = "postgres"
DB_PASSWORD = "kvyu8dutx"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "postgres"  # Don't change this - system uses default 'postgres' DB
```

## 🎯 Next Steps

After the app starts:

1. **Add Students** - Go to "Students" tab → Fill form → Click "Add"
2. **Add Instructors** - Go to "Instructors" tab → Fill form → Click "Add"
3. **Add Courses** - Go to "Courses" tab → Enter course name and instructor ID → Click "Add"
4. **Enroll Students** - Go to "Enrollments" tab → Enter student and course IDs → Click "Enroll"
5. **View Reports** - Go to "Reports" tab → Select a report type and view results

## 📞 Need Help?

Check the main README.md for:
- Detailed feature documentation
- API endpoint reference
- Architecture diagrams
- Database schema details
- Example code snippets

---

**Happy registering!** 🎓
