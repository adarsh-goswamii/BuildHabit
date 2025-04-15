# 🧱 BuildHabit

**BuildHabit** is a personalized habit-tracking visual dashboard built specifically for software engineers. Inspired by the contribution heatmaps on platforms like GitHub and LeetCode, this app generates daily progress visuals and makes them easily accessible — even as a widget or wallpaper.

---

## 📌 Motivation

As a software engineer balancing a full-time job and personal growth, it's easy to lose track of progress. 
**BuildHabit** solves this by:
- Visually tracking coding habits.
- Automatically pulling in data from platforms you already use.
- Allowing manual input for things that can’t be automated.
- Displaying it in places you'll see daily (like your desktop or iPad widget).

---

## 💠 Features (MVP)

### ✅ Automated Data Tracking
- **LeetCode**: Fetch daily submission history using their public APIs.
- **GitHub**: Pull commit/activity data to generate a contribution graph.

### ✍️ Manual Tracking
- **Online Courses**: Simple REST API + UI to log what you’re learning and when.

### 🖼 Image Generator
- Generates a contribution-style graph as a visual image.
- Designed to be used as a wallpaper or displayed in a widget.

### 🤭 Daily Automation
- Uses a cron job to:
  - Fetch the data
  - Generate the updated image
  - Save or upload for use in widgets or wallpapers

---

## 💡 Future Goals
- Develop a **SwiftUI-based widget** for iOS/macOS using **WidgetKit**
- Integrate other learning sources like YouTube or Udemy (if API allows)
- Cloud sync / optional login for multi-device support

---

## 🛠 Tech Stack

| Layer         | Tech                        |
|--------------|-----------------------------|
| Backend       | FastAPI, Python             |
| Scheduler     | Cron Job / APScheduler      |
| Image Gen     | Python (Pillow / Matplotlib)|
| Dev Workflow  | pipenv, `.env`              |
| iOS/macOS UI  | SwiftUI + WidgetKit (future)|

---

## 🚀 Getting Started

### 1. Clone and setup environment
```bash
git clone https://github.com/yourname/BuildHabit.git
cd BuildHabit
pipenv install
```

### 2. Run the API
```bash
pipenv run uvicorn main:app --reload --port 4000
```

### 3. Setup Cron (or manual script execution)
This script will generate the daily image using your tracked data.

---

## 📂 Project Structure (Sample)

```
BuildHabit/src
│
├— main.py               # FastAPI app
├— services/
│   ├— github.py         # GitHub data fetcher
│   ├— leetcode.py       # LeetCode data fetcher
│   └— learning.py      # Manual learning logger
├— utils/
│   └— image_gen.py      # Contribution graph generator
├— cron/
│   └— generate_image.py # Script triggered daily
├— static/
│   └— output.png        # Latest generated image
└— .env
```

---

## 👌 Why This Project Matters

You're not just tracking habits — you're **visualizing discipline**.  
This is a build-for-yourself tool that keeps you accountable, focused, and proud of the work you're doing.

---

## 📱 Widget / Wallpaper Support (Upcoming)

- WidgetKit integration on macOS/iOS to display your progress image
- Daily-refresh wallpapers for iPad or macOS via automation

---

## 📬 Contact

Feel free to reach out if you want to contribute or chat about productivity tools for devs!

