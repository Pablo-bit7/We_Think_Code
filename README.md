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
The **Bootcamp Helper** was part of the bootcamp curriculum at **WTC** (**WeThinkCode_**). This project was designed to be a simple CLI program which emulates the automation and management of internal bootcamp processes and operations. It also served as an introduction to test driven development. There are four distinct features that address common administrative tasks.

---

### 2. Features
1. **Username Generator**
   Generates unique usernames for bootcamp participants based on a specific format.

2. **Team Allocator**
   Assigns participants into teams based on their campus and mode of attendence (virtual/physical).

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
python3 -m unittest unit_tests/test_<feature_name>.py
```
Run exploratory tests for each feature:
```bash
./features/<feature_name>.py
```

---

### 5. Limitations
- File and function names were predefined not be altered.
- Features are implemented as standalone modules, focusing on the internal processes for bootcamp management.

---

### 6. Acknowledgements
This project now serves as the foundation for a more advanced bootcamp management tool.
A special thanks goes out to the mentors and my peers for their guidance, assistance and support!
