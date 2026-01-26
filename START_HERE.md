# 🎓 START HERE - Course Registration System

Welcome! This is your **complete, ready-to-use Course Registration System**.

## ⚡ Quick Start (30 seconds)

### For macOS/Linux:
```bash
cd CPE312-Course-Registration-System
chmod +x run.sh
./run.sh
```

### For Windows:
```cmd
cd CPE312-Course-Registration-System
run.bat
```

**Then open your browser and go to:**
```
http://localhost:5001
```

✅ **That's it! The system is running!**

---

## 🎯 What to Do Next

Once you see the web interface:

1. **Add a Student**
   - Go to "Students" tab
   - Fill: First Name, Last Name, Department
   - Click "Add"

2. **Add an Instructor**
   - Go to "Instructors" tab
   - Fill: First Name, Last Name, Department
   - Click "Add"

3. **Add a Course**
   - Go to "Courses" tab
   - Course Name: "Database Systems"
   - Instructor ID: 1
   - Click "Add"

4. **Enroll Student**
   - Go to "Enrollments" tab
   - Student ID: 1
   - Course ID: 1
   - Click "Enroll"

5. **Assign Grade**
   - Student ID: 1
   - Course ID: 1
   - Grade: AA
   - Click "Assign"

6. **View Reports**
   - Go to "Reports" tab
   - Click any report button
   - See the results!

---

## 📚 Documentation

- **README.md** - Full documentation
- **SETUP.md** - Detailed setup instructions
- **FEATURES.md** - Complete feature list
- **PROJECT_SUMMARY.md** - Project overview

---

## 🆘 Troubleshooting

### PostgreSQL not running?
```bash
brew services start postgresql  # macOS
sudo systemctl start postgresql  # Linux
```

### Port 5001 already in use?
```bash
lsof -i :5001          # Find process
kill -9 <PID>          # Kill it
./run.sh               # Restart
```

### Dependencies missing?
The startup script handles this automatically. If you get errors, try:
```bash
pip install flask sqlalchemy psycopg2-binary
```

---

## ✨ Features at a Glance

✅ Student Management  
✅ Instructor Management  
✅ Course Management  
✅ Enrollment Management  
✅ 5 Different Reports  
✅ Input Validation  
✅ Error Handling  
✅ Responsive UI  
✅ English Interface  

---

## 📞 Need Help?

1. Check the relevant .md file
2. Look at the error message
3. Check PostgreSQL is running
4. Verify port 5001 is free

---

## 🚀 You're All Set!

Your Course Registration System is:
- ✅ Fully functional
- ✅ Ready to use
- ✅ Well documented
- ✅ Production ready

**Just run the startup script and you're good to go!**

---

**Version**: 1.0.0  
**Status**: ✅ Ready for Production  
**Last Updated**: January 27, 2026
