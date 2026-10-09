import joblib
import sys

def main():
    print("=" * 45)
    print("      MUSIC GENRE PREDICTION INTERFACE       ")
    print("=" * 45)

    # 1. Load the trained model
    try:
        model = joblib.load('music-recommender.joblib')
        print("[+] Trained model loaded successfully.")
    except FileNotFoundError:
        print("[!] Error: 'music-recommender.joblib' not found.")
        print("    Please run music_recommender.ipynb first to save the model artifact.")
        sys.exit(1)

    # 2. Collect and validate user input
    while True:
        try:
            age_raw = input("\nEnter age (or 'q' to quit): ").strip()
            if age_raw.lower() == 'q':
                print("Exiting recommendation tool. Bye!")
                break

            age = int(age_raw)
            if age <= 0 or age > 120:
                print("Please enter a realistic age between 1 and 120.")
                continue

            gender_raw = input("Enter gender (m/f): ").strip().lower()
            if gender_raw in ['m', 'male', '1']:
                gender = 1
            elif gender_raw in ['f', 'female', '0']:
                gender = 0
            else:
                print("Invalid input. Please enter 'm' for male or 'f' for female.")
                continue

            # 3. Model inference
            prediction = model.predict([[age, gender]])
            genre = prediction[0]

            gender_label = "Male" if gender == 1 else "Female"
            print("-" * 45)
            print(f"Profile: Age {age} | Gender: {gender_label}")
            print(f"Recommended Genre: >>> {genre.upper()} <<<")
            print("-" * 45)

        except ValueError:
            print("Invalid input. Age must be a whole number.")

if __name__ == '__main__':
    main()