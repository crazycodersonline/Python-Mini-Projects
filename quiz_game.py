
questions = ["Who is father of computer","What is ALU","Who invented www"]
answers = ["Charles Babbage" , "Arithmetic Logic Unit" , "Tim Berners-Lee"]

score = 0

for question , answer in zip(questions,answers):
    user_ans = input(question+"?")
    
    if user_ans.lower() == answer.lower():
        score = score + 1
        print("Correct!")
    else:
        print("Incorrect!")
        
    
print(f"Final Score: {score} / {len(questions)}".center(100))