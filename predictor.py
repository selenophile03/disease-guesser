 import json

class SymptomPredictor:
    def __init__(self, dataset_path="dataset.json"):
        self.dataset_path = dataset_path
        self.diseases = self._load_dataset()

    def _load_dataset(self):
        try:
            with open(self.dataset_path, 'r') as file:
                data = json.load(file)
                return data.get("diseases", [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_all_symptoms(self):
        all_symptoms = set()
        for disease in self.diseases:
            all_symptoms.update(disease["symptoms"])
        return sorted(list(all_symptoms))

    def analyze_symptoms(self, user_inputs):
        user_symptoms = [s.strip().lower() for s in user_inputs if s.strip()]
        if not user_symptoms:
            return []

        results = []
        for disease in self.diseases:
            matched_symptoms = []
            for sym in disease["symptoms"]:
                for user_sym in user_symptoms:
                    if user_sym in sym or sym in user_sym:
                        if sym not in matched_symptoms:
                            matched_symptoms.append(sym)

            if matched_symptoms:
                match_score = (len(matched_symptoms) / len(disease["symptoms"])) * 100
                results.append({
                    "disease": disease["name"],
                    "confidence": round(match_score, 2),
                    "matched_symptoms": matched_symptoms,
                    "description": disease["description"],
                    "precautions": disease["precautions"]
                })

        return sorted(results, key=lambda x: x['confidence'], reverse=True)
