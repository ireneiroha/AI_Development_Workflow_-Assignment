Ethics & Bias 
How might biased training data affect patient outcomes in the case study?

Bias in training data—such as underrepresentation of specific age groups, genders, or ethnic communities—can severely impact patient outcomes. If an AI system is trained predominantly on data from one demographic (e.g., middle-aged patients), it might inaccurately assess readmission risk for others, such as the elderly or marginalized communities. This could lead to misdiagnosis, delayed treatment, or unnecessary hospital stays for underrepresented groups. In healthcare, this isn't just a technical flaw—it's a risk to patient safety and equity.

Strategy to mitigate this bias:

One effective strategy is data rebalancing during preprocessing. This could include:

Oversampling minority groups (e.g., SMOTE)

Stratified sampling to maintain proportional representation across demographics

Bias audits and fairness-aware algorithms (e.g., Equal Opportunity or Demographic Parity metrics)

Additionally, involving diverse stakeholders during dataset curation and model validation (including clinicians, patients, and ethicists) helps ensure fairness from multiple perspectives.

Trade-offs 
Trade-off between model interpretability and accuracy in healthcare:

In healthcare, interpretability often takes priority over sheer accuracy. While deep learning models (e.g., neural networks) might achieve higher predictive performance, their "black-box" nature makes it difficult for medical professionals to trust or understand their decisions. On the other hand, interpretable models (e.g., Decision Trees, Logistic Regression) may be slightly less accurate but are transparent, easier to explain to patients, and align better with clinical guidelines and legal requirements.

Computational resource constraint and model choice:

With limited computational resources, models with low complexity and faster inference times—such as Random Forests or Gradient Boosted Trees—are more practical than deep neural networks. These models offer a balance between decent accuracy and efficiency. Additionally, simpler models reduce hardware and maintenance costs, ensuring smoother deployment in hospital systems that may not have access to cloud or high-performance computing.

