# Part 1: Short Answer Questions 

---

## 1. Problem Definition 

**Hypothetical AI Problem**:  
*Predicting Student Dropout Risk in Online Learning Platforms*

**Objectives**:
1. Identify at-risk students early to enable timely interventions.
2. Improve overall student retention rates.
3. Provide actionable insights to educators and course designers.

**Stakeholders**:
- **Students** – primary beneficiaries who receive timely support.
- **School Administrators / Academic Advisors** – decision-makers who implement interventions.

**Key Performance Indicator (KPI)**:
**Dropout Prediction Accuracy** – the percentage of correctly predicted dropout cases compared to actual cases.

---

## 2. Data Collection & Preprocessing 

**Two Data Sources**:
1. Learning Management System (LMS) Logs – login frequency, activity duration, assignment submissions.
2. Demographic and Academic Records – age, GPA, attendance, background.

**One Potential Bias**:
Students with limited internet access or socioeconomic disadvantages may be underrepresented, leading to skewed risk predictions and unfair interventions.

**Three Preprocessing Steps**:
1. Handling Missing Data – use mean/mode imputation for numerical/categorical fields.
2. Normalization – scale features like login frequency using MinMaxScaler.
3. Categorical Encoding – convert variables like gender or education level using one-hot encoding.

---

## 3. Model Development (8 Points)

**Model Choice**:  
Random Forest Classifier

**Justification**:
- Handles high-dimensional data well.
- Robust to overfitting and noisy features.
- Provides feature importance scores.

**Train/Validation/Test Split**:
- 70% Training
- 15% Validation
- 15% Testing

**Two Hyperparameters to Tune**:
1. `n_estimators` – Number of trees in the forest; affects accuracy and computation.
2. `max_depth` – Controls tree depth; prevents overfitting.

---

## 4. Evaluation & Deployment 

**Two Evaluation Metrics**:
1. Precision – Measures the accuracy of positive predictions.
2. Recall – Measures the ability to find all actual dropout cases.

**What is Concept Drift?**  
It refers to the change in underlying data patterns over time.

**Monitoring Drift**:
- Use statistical tests (e.g., Population Stability Index).
- Re-evaluate model performance quarterly using fresh test sets.

**Technical Challenge During Deployment**:  
Scalability – ensuring the model can handle predictions in real-time for thousands of students.

---
