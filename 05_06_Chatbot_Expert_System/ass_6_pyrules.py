import py_rules

class MedicalExpertSystem:
    def __init__(self):
        self.engine = py_rules.create_engine()

    def run(self):
        print("Welcome to the Medical Expert System!")
        print("Please answer the following questions to get a diagnosis.")

        fever = self.confirm("Do you have a fever?")
        headache = self.confirm("Do you have a headache?")
        body_pain = self.confirm("Do you experience body pain?")
        cough = self.confirm("Do you have a cough?")

        self.engine.reset()
        self.engine.activate('diagnosis')
        self.engine.facts['fever'] = fever
        self.engine.facts['headache'] = headache
        self.engine.facts['body_pain'] = body_pain
        self.engine.facts['cough'] = cough
        self.engine.run()

    def confirm(self, question):
        while True:
            response = input(question + " (y/n) ").lower()
            if response == "y":
                return True
            elif response == "n":
                return False
            else:
                print("Invalid response. Please enter 'y' or 'n'.")

    @py_rules.rule('diagnosis')
    def suggest_flu(self, fever, headache, body_pain, cough):
        if fever and headache and body_pain and cough:
            print("Based on your symptoms, you may have the flu.")
            print("Recommendation: Get plenty of rest, stay hydrated, and consult a doctor if symptoms persist or worsen.")

    @py_rules.rule('diagnosis')
    def suggest_common_cold(self, fever, headache, body_pain, cough):
        if fever and headache and body_pain and not cough:
            print("Based on your symptoms, you may have a common cold.")
            print("Recommendation: Get plenty of rest, drink fluids, and consider over-the-counter medications for symptom relief.")

    @py_rules.rule('diagnosis')
    def suggest_fever(self, fever, headache, body_pain, cough):
        if fever and not headache and not body_pain and not cough:
            print("Based on your symptoms, you may have a fever of unknown origin.")
            print("Recommendation: Monitor your temperature, stay hydrated, and consult a doctor if the fever persists or worsens.")

    @py_rules.rule('diagnosis')
    def no_diagnosis(self, fever, headache, body_pain, cough):
        if not fever and not headache and not body_pain and not cough:
            print("Based on your responses, we could not determine a specific diagnosis.")
            print("Recommendation: If you have any concerning symptoms, please consult a medical professional.")

expert_system = MedicalExpertSystem()
expert_system.run()