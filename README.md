# Bootcamp Helper

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Testing](#testing)
5. [Limitations](#limitations)
6. [Acknowledgements](#acknowledgements)

---

### 1. Project Overview
**Bootcamp Helper** is a program designed to automate internal bootcamp processes and manage bootcamp operations. It includes four distinct features that address common administrative tasks. This project serves as a foundation for developing a more advanced bootcamp management tool, BootBuddy.

---

### 2. Features
1. **Username Generator**  
   Generates unique usernames for bootcamp participants based on a specific format.

2. **Team Allocator**  
   Assigns participants into teams based on track (experienced/inexperienced), campus, and bootcamp type (virtual/physical).

3. **Registration Station**  
   Displays candidate information and booking details, allowing users to confirm or modify their bookings.

4. **Bootcamp Exercise Marker**  
   Administers and grades multiple-choice exams, iteratively presenting incorrectly answered questions until answered correctly.

---

### 3. Requirements
- **Environment**: Ubuntu 20.04 LTS  
- **Programming Language**: Python 3.8.5  
- **Testing Framework**: `unittest`  
- File and function names are predefined and cannot be modified.  

---

### 4. Testing
Run the unit tests for each feature:  
```bash
python3 -m unittest test_<feature_name>.py
