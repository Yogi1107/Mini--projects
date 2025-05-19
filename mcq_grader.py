score = 0
total_questions = 5

print("📘 Welcome to the MCQ Quiz!")
print("Type your answer (a/b/c/d) for each question.\n")

print("Q1: What is the capital of India?")
print("a) Mumbai")
print("b) Kolkata")
print("c) New Delhi")
print("d) Chennai")
ans1 = input("Your answer: ").lower()
if ans1 == 'c':
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is: c) New Delhi\n")

print("Q2: Which planet is known as the Red Planet?")
print("a) Earth")
print("b) Mars")
print("c) Venus")
print("d) Jupiter")
ans2 = input("Your answer: ").lower()
if ans2 == 'b':
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is: b) Mars\n")

print("Q3: Who wrote the Ramayana?")
print("a) Tulsidas")
print("b) Kalidas")
print("c) Ved Vyasa")
print("d) Valmiki")
ans3 = input("Your answer: ").lower()
if ans3 == 'd':
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is: d) Valmiki\n")

print("Q4: Which is the largest mammal?")
print("a) Elephant")
print("b) Blue Whale")
print("c) Giraffe")
print("d) Hippo")
ans4 = input("Your answer: ").lower()
if ans4 == 'b':
    print("✅ Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is: b) Blue Whale\n")

print("Q5: What is H2O commonly known as?")
print("a) Oxygen")
print("b) Water")
print("c) Hydrogen")
print("d) Salt")
ans5 = input("Your answer: ").lower()
if ans5 == 'b':
    print("Correct!\n")
    score += 1
else:
    print("❌ Wrong! Correct answer is: b) Water\n")

print("===== Quiz Completed =====")
print(f"Your Score: {score}/{total_questions}")

if score == total_questions:
    print("Perfect score! Excellent work!")
elif score >= total_questions / 2:
    print("Good effort! Keep practicing!")
else:
    print("Don't worry, keep learning and try again!")
