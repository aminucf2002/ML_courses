from data import question_data
from question_model import Question
from quiz_brain import QuizeBrain

question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(q_text=question_text,q_answer=question_answer)
    question_bank.append(new_question)

quiz=QuizeBrain(question_bank)
while quiz.still_has_questions()==True:
    quiz.next_question()
print("You've complete the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")