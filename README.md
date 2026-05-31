# Phishing Email Detection Model

## Overview
The **Phishing Email Detection Model** is a simple cybersecurity project built using Python. This tool analyzes email content and detects whether an email is **Safe**, **Suspicious**, or a **Phishing Email** based on common phishing patterns such as suspicious keywords, links, and urgency messages.

This project is beginner-friendly and does not require any external libraries, making it easy to run in any Python environment.

---

## Features
- Detects common phishing keywords
- Identifies suspicious links (`http://` or `https://`)
- Checks for urgency-based phishing language
- Classifies emails as:
  - **Safe Email**
  - **Suspicious Email**
  - **Phishing Email**
- Beginner-friendly and lightweight
- No external libraries required

---

## Technologies Used
- **Python**
- Built-in Python Functions
- String Handling

---

## Project Structure
```

Phishing-Email-Detection/
│── phishing_detector.py
│── README.md

```

---

## How It Works
The program scans the email content and looks for:

### 1. Phishing Keywords
Examples:
- urgent
- verify
- click here
- login
- password
- winner
- free
- account suspended
- security alert

### 2. Suspicious Links
The tool checks for links such as:
```

http://
https://

```

### 3. Email Pattern Analysis
- Suspicious urgency messages
- Fake account verification requests
- Unusual email formatting

Based on these checks, the system calculates a phishing score and predicts whether the email is safe or malicious.

---

## Installation

### Step 1: Install Python
Make sure Python is installed on your system.

Check Python version:
```bash
python --version
```

### Step 2: Download the Project
Clone this repository:

```bash
git clone https://github.com/your-username/phishing-email-detection.git
```

Or download the ZIP file.

### Step 3: Run the Program

```bash
python phishing_detector.py
```

---

## Usage

Run the program and paste email content when prompted.

### Example 1: Phishing Email
Input:
```

URGENT! Your bank account is suspended.
Click here: http://fakebank-login.com
Verify your password immediately.

```

Output:
```

Result: PHISHING EMAIL

```

### Example 2: Safe Email
Input:
```

Hello Team,
Meeting is scheduled for tomorrow at 10 AM.
Thank you.

```

Output:
```

Result: SAFE EMAIL

```

---

## Example Code Logic
The program works by:
1. Checking suspicious phishing keywords
2. Detecting links inside emails
3. Assigning a phishing score
4. Classifying the email based on score

---

## Future Improvements
- Add Machine Learning support
- Improve phishing detection accuracy
- Add GUI interface
- Detect fake domains
- Email attachment scanning

---

## Expected Outcome
This project helps users understand:
- Phishing attacks
- Email security
- Cybersecurity basics
- Threat detection techniques

---

## Author
**Lakshita Mangal**

Cybersecurity Internship Project
