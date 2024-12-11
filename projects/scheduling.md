# Project: Bio Course Scheduling System

## Overview
In this project, you will build a scheduling system for a bio course that efficiently assigns teachers, courses, and classrooms based on various constraints. Your goal is to maximize the overall "profit" of the schedule, which is influenced by factors such as teacher popularity and the number of students enrolled in each course. Additionally, the system must avoid scheduling conflicts and respect class dependencies (i.e., some courses must be taken in sequence).

To get started, you’ll create an Excel sheet containing the following information:
- Teachers' availability and qualifications
- Classroom characteristics
- Course requirements (like student count and equipment needs)
- Course dependencies (if any)

Once the data is provided, your program will use optimization techniques to generate a schedule that meets all constraints while maximizing the overall value for the term.

---

## Project Breakdown

### 1. **Data Preparation (Excel Setup)**
- **Goal**: Create an Excel file that holds all necessary scheduling data, which will be used as input for the scheduling system.
- **Tasks**:
  - Create **Sheet 1: Teachers**:
    - **Columns**: Teacher Name, Teacher ID, Available Time Slots, Courses They Can Teach, Popularity (a score for each course they teach).
  - Create **Sheet 2: Classes**:
    - **Columns**: Classroom ID, Size, Has Projector (Yes/No).
  - Create **Sheet 3: Courses**:
    - **Columns**: Course Name, Course ID, Number of Students, Needs Projector (Yes/No).
  - Create **Sheet 4: Dependencies**:
    - **Columns**: Course Dependencies (list of courses that need to be scheduled in order, e.g., A1 -> A2 -> A3).
   
- **Hint**: You can generate mock data for the initial testing. For example, assign random time slots to teachers and create a few dependencies between courses.

---

### 2. **Reading and Parsing Excel Data**
- **Goal**: Write Python code to read the scheduling information from the Excel file into your program for further processing.
- **Tasks**:
  - Use **pandas** to read the Excel file.
  - Extract information about teachers, courses, classrooms, and dependencies into separate data structures (e.g., dictionaries or lists).
  - Parse the teacher popularity scores, class sizes, and course projector requirements.
   
- **Hint**: You can use `pandas.read_excel()` to load each sheet into a DataFrame. Ensure that you handle missing data gracefully.

---

### 3. **Constraint Setup and Conflict Avoidance**
- **Goal**: Define and implement the core scheduling constraints to ensure no conflicts arise (e.g., no double booking of teachers or classrooms).
- **Tasks**:
  - Define the following constraints:
    - **Time Conflicts**: No teacher or classroom can be scheduled for two courses at the same time.
    - **Class Size**: A classroom must be large enough to accommodate the students registered for each course.
    - **Equipment Needs**: If a course requires a projector, it must be scheduled in a classroom that has one.
    - **Teacher Assignment**: Only assign teachers to courses they are qualified to teach.
  - Implement a function to check for potential scheduling conflicts when attempting to assign teachers, classrooms, and courses.
   
- **Hint**: Create a "schedule matrix" where each row represents a time slot, and each column represents a resource (teacher or classroom). Populate the matrix to detect conflicts.

---

### 4. **Handling Course Dependencies**
- **Goal**: Ensure that courses with dependencies are scheduled in the correct order.
- **Tasks**:
  - Parse the course dependencies from the Excel sheet.
  - Implement a logic that schedules dependent courses sequentially.
  - For example, if Course A1 must be taken before Course A2, schedule A1 in an earlier time slot.
   
- **Hint**: You can represent the course dependencies as a directed graph and perform a **topological sort** to ensure that courses are scheduled in the correct order.

---

### 5. **Optimization: Maximizing Profit**
- **Goal**: Create an objective function that maximizes the profit (or value) of the schedule based on teacher popularity and course enrollments.
- **Tasks**:
  - Define the "profit" of the schedule as a combination of factors:
    - The popularity of the teacher assigned to a course.
    - The number of students enrolled in the course (the more students, the higher the value).
  - Use an optimization technique like **greedy algorithms** or **constraint satisfaction problems (CSP)** to maximize this profit while satisfying all constraints.
  - If multiple valid schedules are possible, the algorithm should choose the one with the highest profit.

- **Hint**: Start with a simple approach like a greedy algorithm, where you assign the most popular teachers to the most crowded courses first. Then refine your solution to handle edge cases.

---

### 6. **Generating the Schedule**
- **Goal**: Create a final schedule that assigns courses, teachers, and classrooms to available time slots.
- **Tasks**:
  - After all constraints and optimizations are applied, generate the final schedule.
  - Present the schedule in a readable format (either in the terminal, as an Excel file, or a simple GUI).
  - Ensure that the schedule contains the following information:
    - Course Name
    - Assigned Teacher
    - Classroom
    - Time Slot
   
- **Hint**: Consider creating a new Excel file or updating the existing one to output the final schedule.

---

### 7. **Error Handling and User Feedback**
- **Goal**: Ensure that your program gracefully handles potential errors, such as missing data or scheduling conflicts that can't be resolved.
- **Tasks**:
  - Implement error messages for cases where a course cannot be scheduled (e.g., no available teacher or classroom).
  - Provide feedback to the user on the validity of the generated schedule, and suggest manual adjustments if necessary.

- **Hint**: You can log potential issues (like unresolved conflicts) to a separate file or display them on the console.

---

## Optional Enhancements
- **Teacher Preferences**: Allow teachers to specify their preferred time slots and courses, and try to accommodate these preferences when generating the schedule.
- **Flexible Class Sizes**: Adjust class sizes based on the availability of classrooms and teacher preferences.
- **Real-Time Scheduling**: Add an interactive GUI that allows users to adjust schedules dynamically.
- **Advanced Optimization**: Explore more sophisticated optimization algorithms like **genetic algorithms** or **linear programming** to further maximize the profit.

---

## Key Concepts to Review
- **Excel Data Handling with pandas**
- **Greedy Algorithms and Backtracking**
- **Graph Algorithms (Topological Sort)**
- **Constraint Satisfaction Problems (CSP)**
- **Scheduling and Optimization Techniques**

---

Good luck! This project will help you build critical skills in constraint-based problem solving, optimization, and data manipulation with Python.

Oct 8, 2024 at 15:13
#learning/courses/python