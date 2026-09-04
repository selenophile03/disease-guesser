from predictor import SymptomPredictor

def display_menu(predictor):
    print("=" * 60)
    print("🩺 EDUCATIONAL SYMPTOM-BASED DISEASE PREDICTOR 🩺")
    print("=" * 60)
    print("\nAvailable symptoms in our directory:")
    
    # Render symptoms in clean, organized columns
    symptoms = predictor.get_all_symptoms()
    for i, symptom in enumerate(symptoms, 1):
        print(f"- {symptom:<25}", end="")
        if i % 2 == 0:
            print()
    print("\n" + "=" * 60)

def main():
    predictor = SymptomPredictor()
    
    if not predictor.diseases:
        print("Initialization failed. Please ensure 'dataset.json' exists and is populated.")
        return

    display_menu(predictor)
    
    print("\nEnter your symptoms separated by commas (e.g., cough, fever, fatigue):")
    user_raw_input = input("👉 ").split(",")
    
    print("\nAnalyzing profiles...\n")
    predictions = predictor.analyze_symptoms(user_raw_input)
    
    if not predictions:
        print("❌ No matching conditions found based on the provided symptoms.")
        print("Try adjusting your spelling or mixing symptoms from the chart above.")
    else:
        print(f"📊 Found {len(predictions)} possible matching condition(s):\n")
        for rank, res in enumerate(predictions, 1):
            print(f"{rank}. Condition: {res['disease']}")
            print(f"   🔹 Match Confidence: {res['confidence']}%")
            print(f"   🔹 Matches Triggered: {', '.join(res['matched_symptoms'])}")
            print(f"   🔹 Description: {res['description']}")
            print(f"   🔹 Suggested Steps:")
            for step in res['precautions']:
                print(f"      - {step}")
            print("-" * 50)

if __name__ == "__main__":
    main()
