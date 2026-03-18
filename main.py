from analyzer import analyze_code

def main():
    file_path = input("Enter Python file path: ")

    try:
        with open(file_path, "r") as file:
            code = file.read()

        results = analyze_code(code)

        print("\n🔍 Analysis Report:")
        for issue in results:
            print(issue)

    except FileNotFoundError:
        print("❌ File not found. Check path again.")

if __name__ == "__main__":
    main()
