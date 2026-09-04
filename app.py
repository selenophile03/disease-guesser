from predictor import SymptomPredictor

def display_menu(predictor):
    print("=" * 60)
    print("SYMPTOM MATRIX DIAGNOSTIC")
    print("=" * 60)
    print("\nAvailable Directory:")
    symptoms = predictor.get_all_symptoms()
    for i, symptom in enumerate(symptoms, 1):
        print(f"- {symptom:<25}", end="")
        if i % 2 == 0:
            print()
    print("\n" + "=" * 60)

def main():
    predictor = SymptomPredictor()
    if not predictor.diseases:
        print("Dataset baseline missing.")
        return

    display_menu(predictor)
    print("\nEnter symptoms separated by commas:")
    user_raw_input = input("> ").split(",")
    
    predictions = predictor.analyze_symptoms(user_raw_input)
    if not predictions:
        print("No active configurations match.")
    else:
        for rank, res in enumerate(predictions, 1):
            print(f"\n{rank}. Match: {res['disease']} ({res['confidence']}%)")
            print(f"   Indicators: {', '.join(res['matched_symptoms'])}")
            print(f"   Description: {res['description']}")
            print(f"   Protocols:")
            for step in res['precautions']:
                print(f"      - {step}")

if __name__ == "__main__":
    main()
