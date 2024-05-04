from experta import *
from experta import KnowledgeEngine
from experta import DefFacts
from experta import Rule

from collections.abc import Mapping

class MedicalExpertSystem(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("Welcome to the Medical Expert System!")
        print("PLease answer the following questions to get a diagnosis.")
        return Fact(action="find_diagnosis")

    @Rule(Fact(action="find_diagnosis"), NOT(Fact(fever=W())), NOT(Fact(headache=W())),NOT(Fact(body_pain=W())),NOT(Fact(cough=W())))        
    def symptom_questions(self):
        self.declare(Fact(fever=confirm("Do you have a fever?")))
        self.declare(Fact(fever=confirm("Do you have a headache?")))
        self.declare(Fact(fever=confirm("Do you have a fever?")))
        self.declare(Fact(fever=confirm("Do you experience body pain?")))
        self.declare(Fact(fever=confirm("Do you have cough?")))
    
    @Rule(Fact(action="find_diagnosis"), Fact(fever=True), Fact(headache=True), Fact(body_pain=True), Fact(cough=True))
    def suggest_flu(self):
        print("Based on your symptoms you may have Flu.")
        print("Recommendation: Get plenty of rest, stay hydrated and consult a doctor if worsens.")

    @Rule(Fact(action="find_diagnosis"), Fact(fever=True), Fact(headache=True), Fact(body_pain=True), NOT(Fact(cough=True)))
    def suggest_common_cold(self):
        print("Based on your symptoms you may have Common Cold.")
        print("Recommendation: Monitor your temperature, stay hydrated, and consult a doctor if worsens.")

    @Rule(Fact(action="find_diagnosis"), Fact(fever=True), NOT(Fact(headache=True)), NOT(Fact(body_pain=True)), NOT(Fact(cough=True)))
    def suggest_fever(self):
        print("Based on your symptoms you may have Fever of unknown origin.")
        print("Recommendation: Monitor your temperature, stay hydrated, and consult a doctor if worsens.")

    @Rule(Fact(action="find_diagnosis"), NOT(Fact(fever=True)), NOT(Fact(headache=True)), NOT(Fact(body_pain=True)), NOT(Fact(cough=True)))
    def no_diagnosis(self):
        print("Based on your responses, I could not determine a specific diagnosis.")
        print("Recommendation: If you have concerning symptoms, please consult a medical professional.")


def confirm(question):
    while True:
        response = input(question + " (y/n) ").lower()
        if response == "y" or "Y":
            return True
        elif response == "n" or "N":
            return False
        else:
            print("Invalid Response. Please Enter 'y' or 'n'.")

engine = MedicalExpertSystem()
engine.reset()
engine.run()


