import turtle
import pandas
#import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50 :
    answer_state= screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt = "What's another state's name? ").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())

#states_to_learn.csv
screen.exitonclick()

#If answer_state is one of the states in all the states of the 50_states.csv
    #If they got it right:
        #Create a turtle to write the name of the sate at the state's x and y coordinate


# def get_mouse_click_coor(x,y): #function to get the coordinates through the points clicked in the frame
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# answer_state.capitalize()
# turtle.mainloop()


#you'll know that I tried (T_T)(http://prntscr.com/1zklt63)
# with open(50_states.csv,'') as 50:
#     for states 50[state]:
#         if answer_state= states:
#             turtle.goto(50[x[answer_state],50[y[answer_state]]])
#             turtle.write(answer_state)







