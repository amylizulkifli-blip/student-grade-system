# app.py
import streamlit as st
from student_module import Student, HonourStudent, calculate_total_marks, determine_status

st.set_page_config(page_title="Student Grade System", page_icon="🎓")
st.title("🎓 Student Grade & GPA Calculator")
st.write("Enter student details and marks to compute average, grade and status.")

# ---------- GUI INPUTS (>=3 required) ----------
name = st.text_input("Student Name")
age = st.number_input("Age", min_value=5, max_value=100, step=1)
student_id = st.text_input("Student ID")
is_honour = st.checkbox("Honour Student? (adds +5 bonus)")
bonus = st.slider("Bonus marks (if honour)", 0, 10, 5)

marks_input = st.text_area(
    "Enter marks separated by commas (e.g. 80, 75, 90)",
    placeholder="80, 75, 90"
)

# ---------- USER EVENTS (>=3 required) ----------
# Events used: text_input, number_input, checkbox, slider, text_area, button, expander
with st.expander("ℹ️ How grading works"):
    st.write("A ≥ 80, B ≥ 70, C ≥ 60, D ≥ 50, F < 50")

# ---------- BUTTON TRIGGERS PROCESSING ----------
if st.button("Calculate Result"):
    try:
        # --- Exception handling: empty fields (error 1) ---
        if not name.strip():
            raise ValueError("Student Name cannot be empty.")
        if not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not marks_input.strip():
            raise ValueError("Marks field cannot be empty.")

        # --- Parse marks + numeric validation (error 2) ---
        try:
            marks = [float(m.strip()) for m in marks_input.split(",") if m.strip()]
        except ValueError:
            raise ValueError("Marks must be numbers separated by commas.")

        if not marks:
            raise ValueError("Please enter at least one mark.")

        # --- Range validation (error 3) ---
        if any(m < 0 or m > 100 for m in marks):
            raise ValueError("Each mark must be between 0 and 100.")

        # --- Instantiate the correct object (OOP requirement b) ---
        if is_honour:
            student = HonourStudent(name, int(age), student_id, marks, bonus=bonus)
        else:
            student = Student(name, int(age), student_id, marks)

        # --- Use module functions (module requirement c) ---
        total = calculate_total_marks(marks)
        avg = student.calculate_average()
        grade = student.generate_grade()
        status = determine_status(avg)

        # --- Display results clearly (GUI requirement e) ---
        st.success("✅ Result generated successfully!")
        st.subheader("📊 Result Summary")
        st.write(student.display_info())

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Marks", f"{total:.2f}")
        col2.metric("Average", f"{avg:.2f}")
        col3.metric("Grade", grade)

        if status == "PASS":
            st.success(f"Status: **{status}**")
        else:
            st.error(f"Status: **{status}**")

    except ValueError as ve:
        st.error(f"⚠️ Input Error: {ve}")
    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")