import data

class question_frame:
    def __init__(self, qu, a):
        self.qu = qu
        self.a = a

class question_display:

    def __init__(self, ques_list):
        self. q_no = 0
        self.ques_list = ques_list
        self.score = 0

    def question_next(self):

        if self.q_no+1 < len(self.ques_list):

            ques = self.ques_list[self.q_no]
            self.q_no += 1

            ans = input(f"Q.{self.q_no} :{ques.qu} (True/False)?").lower()

            if ans == ques.a:
                print("Correct answer")
                self.score +=1
                print(f"Score : {self.score}/ {self.q_no}")
                print("\n")
            else:
                print("wrong answer")
                print(f"Score : {self.score} /{self.q_no}")
                print("\n")
        else:
            print("Quiz fininshed")

q_list = []

for x in data.question_data:
    que = x["text"]
    ans = x["answer"]
    question = question_frame(que, ans)
    q_list.append(question)

is_on = True
nest_q = question_display(q_list)
while is_on:

    nest_q.question_next()


