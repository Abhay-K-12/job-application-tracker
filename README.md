# 📋 Job Application Tracker

A lightweight Python CLI tool to track your job applications — store company name, role, status, and view all your applications — all saved locally in a CSV file.

---

## 🚀 Features

- ➕ **Add a job application** — Enter company name, role, and current status
- 📄 **View all applications** — See every job you've applied to in one place
- 💾 **Persistent storage** — All data is saved in a local `jobs.csv` file, so nothing is lost between sessions
- 🔁 **Interactive menu loop** — Keep adding or viewing jobs until you choose to exit
- ⚡ **Zero dependencies** — Uses only Python's built-in `csv` module, no installs needed

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| `csv` module (built-in) | Reading and writing job data to `jobs.csv` |

---

## 📁 Project Structure

```
job-application-tracker/
├── JOB TRACKER.PY   # Main CLI program
├── jobs.csv         # Auto-created when you add your first job
└── README.md        # Project documentation
```

---

## ▶️ How to Run

### Prerequisites
- Python 3.x installed — [Download here](https://www.python.org/downloads/)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Abhay-K-12/job-application-tracker.git

# 2. Navigate into the folder
cd job-application-tracker

# 3. Run the program
python "JOB TRACKER.PY"
```

> **Note:** The filename has a space in it, so make sure to wrap it in quotes when running.

---

## 💻 How It Works

When you run the program, you'll see this menu:

```
1. Add Job
2. View Jobs
3. Exit
Choose:
```

**Option 1 — Add Job:**
```
Company: Google
Role: Software Engineer
Status (Applied/Interview/Rejected): Applied
Job added!
```

**Option 2 — View Jobs:**
```
['Google', 'Software Engineer', 'Applied']
['Amazon', 'Data Analyst', 'Interview']
['Infosys', 'Backend Developer', 'Rejected']
```

**Option 3 — Exit:** Closes the program.

All entries are saved to `jobs.csv` automatically.

---

## 📊 CSV File Format

The data is stored in `jobs.csv` like this:

```
Company,Role,Status
Google,Software Engineer,Applied
Amazon,Data Analyst,Interview
Infosys,Backend Developer,Rejected
```

---

## 🔮 Future Improvements

- [ ] Filter jobs by status (e.g. show only "Interview" stage)
- [ ] Count total applications and show summary stats
- [ ] Add date of application (auto-captured)
- [ ] Save job posting link/URL
- [ ] Search by company name or role
- [ ] Delete or update an existing entry
- [ ] Export filtered results to a new CSV
- [ ] Email parsing integration for automation

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** this repository
2. **Create a branch**: `git checkout -b feature/your-feature`
3. **Commit your changes**: `git commit -m "feat: add your feature"`
4. **Push**: `git push origin feature/your-feature`
5. **Open a Pull Request**

---

## 💡 Why This Project Exists

Job hunting is overwhelming — it's easy to lose track of where you applied, what stage you're at, and which companies haven't responded. This tool solves that with a simple, no-fuss CLI that keeps everything organized in a plain CSV file you can open anywhere.

---

## 📄 License

This project is open source and free to use.
