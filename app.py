import streamlit as st

# --- Define the Comprehensive Risk Library ---
risk_library = [
    {
        "id": "risk1",
        "title": "Operational Uncertainty in Complex Environments",
        "description": "When AI systems operate in complex and dynamic environments, there is a higher likelihood of performance uncertainty and unpredictable behavior.",
        "impacts": ["Unpredictable behavior", "Safety hazards", "Operational inefficiencies", "Difficulty in debugging"],
        "mitigation": ["Scenario testing with diverse conditions", "Implementation of adaptive control mechanisms", "Establish continuous monitoring and anomaly detection systems", "Regular performance evaluations"],
        "trigger": "complex_environment"
    },
    {
        "id": "risk2",
        "title": "Opaque Decision-Making and Accountability Gaps",
        "description": "Lack of transparency in AI decision-making processes can lead to difficulty in understanding the rationale behind outputs and assigning accountability.",
        "impacts": ["Loss of trust from stakeholders", "Challenges in regulatory compliance", "Difficulty in identifying and rectifying errors", "Potential for bias to go unnoticed"],
        "mitigation": ["Implement explainability frameworks (e.g., SHAP, LIME)", "Maintain detailed documentation of AI models and decision processes", "Establish clear roles and responsibilities for AI system oversight", "Conduct regular audits of AI decision-making"],
        "trigger": "lack_transparency"
    },
    {
        "id": "risk3",
        "title": "Suboptimal Balance Between Automation and Human Oversight",
        "description": "An imbalance between automation and human oversight can lead to either over-reliance on AI without sufficient human intervention or underutilization of AI capabilities.",
        "impacts": ["Increased risk of errors due to lack of human judgment", "Missed opportunities for efficiency gains", "Reduced user trust in the system", "Potential for deskilling of human workforce"],
        "mitigation": ["Define clear roles and responsibilities for both AI and human actors", "Implement human-in-the-loop systems for critical decisions", "Regularly review and adjust the level of automation based on performance and context", "Provide adequate training for human operators working with AI"],
        "trigger": "level_of_automation"
    },
    {
        "id": "risk4",
        "title": "Compromised Data Quality and Governance in Machine Learning Pipelines",
        "description": "Poor data quality, inadequate data governance, and biases in training data can lead to unreliable and unfair AI models.",
        "impacts": ["Biased or discriminatory outcomes", "Reduced model accuracy and performance", "Increased operational costs due to data errors", "Reputational damage"],
        "mitigation": ["Implement robust data governance frameworks", "Establish rigorous data quality assurance processes (e.g., validation, cleaning)", "Conduct thorough data audits for bias and representativeness", "Ensure data privacy and security compliance"],
        "trigger": "machine_learning"
    },
    {
        "id": "risk5",
        "title": "Hardware Incompatibilities and Performance Limitations",
        "description": "Insufficient or incompatible hardware can lead to performance bottlenecks, system instability, and failure to meet operational requirements.",
        "impacts": ["Slow processing times", "System crashes and failures", "Inability to scale AI applications", "Increased energy consumption"],
        "mitigation": ["Conduct thorough hardware testing and compatibility checks before deployment", "Ensure hardware infrastructure meets the computational demands of the AI system", "Implement monitoring for hardware performance and resource utilization", "Develop a plan for hardware upgrades and maintenance"],
        "trigger": "hardware"
    },
    {
        "id": "risk6",
        "title": "Lack of Comprehensive Lifecycle Management for AI Systems",
        "description": "Absence of a well-defined lifecycle management plan can result in issues during design, deployment, maintenance, and decommissioning of AI systems.",
        "impacts": ["Difficulties in tracking and managing AI assets", "Increased risk of security vulnerabilities", "Challenges in updating and maintaining AI models", "Lack of a plan for responsible decommissioning"],
        "mitigation": ["Develop a comprehensive lifecycle management plan covering all stages", "Establish clear processes for version control and documentation", "Implement security protocols throughout the lifecycle", "Define procedures for monitoring, evaluation, and continuous improvement"],
        "trigger": "lifecycle"
    },
    {
        "id": "risk7",
        "title": "Insufficient Technology Readiness and Potential Performance Drift",
        "description": "Failure to adequately assess the maturity and readiness of AI technologies can lead to performance issues and unexpected behavior over time.",
        "impacts": ["Performance degradation due to changing data patterns", "Inability to adapt to new operational requirements", "Increased maintenance costs", "Loss of effectiveness over time"],
        "mitigation": ["Conduct thorough technology readiness assessments before adoption", "Implement continuous monitoring for performance drift", "Establish retraining and redeployment strategies", "Regularly evaluate the need for technology updates or replacements"],
        "trigger": "technology_readiness"
    },
    {
        "id": "risk8",
        "title": "Lack of Security Measures Against AI-Specific Threats",
        "description": "AI systems can be vulnerable to adversarial attacks, data poisoning, and model theft if specific security measures are not in place.",
        "impacts": ["Compromised model integrity", "Unauthorized access to sensitive data", "Manipulation of AI outputs", "Intellectual property theft"],
        "mitigation": ["Implement security measures designed for AI (e.g., adversarial training)", "Regularly audit AI models for vulnerabilities", "Establish robust data security protocols", "Monitor for AI-specific security incidents"],
        "trigger": "security"
    },
    {
        "id": "risk9",
        "title": "Ethical Concerns and Potential for Bias Amplification",
        "description": "If ethical considerations are not integrated into AI development, there is potential for AI to perpetuate or amplify societal biases.",
        "impacts": ["Unfair or discriminatory outcomes", "Reputational damage", "Legal and regulatory challenges", "Negative societal impact"],
        "mitigation": ["Integrate ethics into the AI development process", "Conduct bias audits and implement mitigation strategies", "Ensure transparency and fairness", "Establish mechanisms for feedback"],
        "trigger": "ethics"
    },
    {
        "id": "risk10",
        "title": "Insufficient User Training and Adoption Challenges",
        "description": "Lack of adequate training and support for users can hinder the adoption and effective use of AI systems.",
        "impacts": ["Low user engagement", "Increased errors", "Resistance to change", "Reduced ROI"],
        "mitigation": ["Develop comprehensive training programs", "Provide ongoing user support", "Design user-friendly interfaces", "Incorporate user feedback into improvements"],
        "trigger": "user_adoption"
    },
]

# --- App Title and Description ---
st.title("Interactive ISO 42001 AI Risk Assessment Tool")
st.write("Answer the questions below to identify potential risks related to your AI systems.")

# --- Step 1: Collect User Responses ---
st.header("Step 1: Provide Your Organization’s AI Environment Details")

# Collect user responses using radio buttons
complex_environment = st.radio("1. Do your AI systems operate in highly complex or dynamic environments?", ("Yes", "No"))
transparency = st.radio("2. Do you have well-defined processes for ensuring AI transparency and explainability?", ("Yes", "No"))
automation = st.radio("3. Is there an optimal balance between automation and human oversight in your AI systems?", ("Yes", "No"))
ml_data_quality = st.radio("4. Do you have robust data governance and quality assurance for your ML pipelines?", ("Yes", "No"))
hardware_testing = st.radio("5. Have you conducted thorough hardware testing and compatibility checks for your AI systems?", ("Yes", "No"))
lifecycle_mgmt = st.radio("6. Do you have a comprehensive lifecycle management plan?", ("Yes", "No"))
tech_readiness = st.radio("7. Have you performed technology readiness assessments?", ("Yes", "No"))
security = st.radio("8. Do you have specific security measures to address AI threats?", ("Yes", "No"))
ethics = st.radio("9. Have you integrated ethical considerations into your AI development?", ("Yes", "No"))
user_adoption = st.radio("10. Do you provide sufficient training and support for your AI system users?", ("Yes", "No"))

# --- Step 2: Map Responses to Risk Triggers ---
triggered_risks = []
if complex_environment == "Yes":
    triggered_risks.append("complex_environment")
if transparency == "No":
    triggered_risks.append("lack_transparency")
if automation == "No":
    triggered_risks.append("level_of_automation")
if ml_data_quality == "No":
    triggered_risks.append("machine_learning")
if hardware_testing == "No":
    triggered_risks.append("hardware")
if lifecycle_mgmt == "No":
    triggered_risks.append("lifecycle")
if tech_readiness == "No":
    triggered_risks.append("technology_readiness")
if security == "No":
    triggered_risks.append("security")
if ethics == "No":
    triggered_risks.append("ethics")
if user_adoption == "No":
    triggered_risks.append("user_adoption")

st.write("### Triggers Identified:", triggered_risks)

# --- Step 3: Display Matching Risks and Suggested Mitigations ---
st.header("Step 2: Identified Risks and Mitigation Strategies")

if triggered_risks:
    for risk in risk_library:
        if risk["trigger"] in triggered_risks:
            st.subheader(risk["title"])
            st.write("**Description:**", risk["description"])
            st.write("**Potential Impacts:**")
            for impact in risk["impacts"]:
                st.write("- " + impact)
            st.write("**Mitigation Strategies:**")
            for strategy in risk["mitigation"]:
                st.write("- " + strategy)
            st.markdown("---")
else:
    st.info("No specific risks identified based on your responses. This might indicate a well-managed AI environment or that further assessment is needed.")

st.markdown("---")
st.subheader("Disclaimer")
st.write("This tool provides a preliminary risk assessment based on your input. It is not a substitute for a comprehensive ISO 42001 audit or professional consultation.")
