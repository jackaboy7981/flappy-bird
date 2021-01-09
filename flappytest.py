import turtle
import time
import random
import winsound

s=turtle.Screen()
s.bgpic("bg.gif")
s.addshape("bird.gif")
s.addshape("birddown.gif")
s.addshape("birdup.gif")
s.addshape("poleu.gif")
s.addshape("poled.gif")
s.setup(500,600)
s.tracer(0)

#bird
bird=turtle.Turtle()
bird.speed(1)
bird.shape("bird.gif")
bird.penup()
bird.goto(0,0)
bird.dy=2
bird.t=1
bird.score=0

y1=random.randint(230,600)
y2=random.randint(230,600)

#pole1
pole11=turtle.Turtle()
pole11.speed(0)
pole11.shape("poleu.gif")
pole11.penup()
pole11.goto(300,y1)

#pole2
pole21=turtle.Turtle()
pole21.speed(0)
pole21.shape("poleu.gif")
pole21.penup()
pole21.goto(600,y2)


#pole1
pole12=turtle.Turtle()
pole12.speed(0)
pole12.shape("poled.gif")
pole12.penup()
pole12.goto(300,y1-740)

#pole2
pole22=turtle.Turtle()
pole22.speed(0)
pole22.shape("poled.gif")
pole22.penup()
pole22.goto(600,y2-740)

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}".format(bird.score), align="center", font=("Courier", 24, "normal"))

#variables
f1=True
f2=True
u=20
a=-5
status=True
q=-5
flag=0

# Function
def fly():
    bird.t=1
    winsound.PlaySound("flap.wav",winsound.SND_ASYNC)

# Keyboard binding
if flag==0:
	s.listen()
	s.onkeypress(fly, "Up")

while status:
	time.sleep(0.03)
	s.update()

#bird parameters
	bird.dy=u + a*(bird.t-0.5)
	bird.sety(bird.ycor() + bird.dy)
	if bird.dy>3 :
		bird.shape("birdup.gif")
	if bird.dy<-3 :	
		bird.shape("birddown.gif")
	if bird.dy < 3 and bird.dy > -3 :
		bird.shape("bird.gif")
	bird.t+=0.5

	if bird.ycor()<-210 :
		status=False
		bird.sety(-190)
		s.update()
	if bird.ycor()>320 :
		u=0
		bird.t=1
		bird.shape("birddown.gif")
		while bird.ycor()>-210 :
			time.sleep(0.03)
			bird.dy=u + a*(bird.t-0.5)
			bird.sety(bird.ycor() + bird.dy)
			bird.t+=0.5
			s.update()
		status=False
		bird.sety(-190)
		s.update()	


#pole parameters
	pole11.setx(pole11.xcor()+q)
	pole12.setx(pole12.xcor()+q)
	pole21.setx(pole21.xcor()+q)
	pole22.setx(pole22.xcor()+q)

	if pole11.xcor()<-300 :
		y1=random.randint(230,600)
		pole11.sety(y1)
		pole12.sety(y1-740)
		pole11.setx(300)
		pole12.setx(300)
		f1=True

	if pole21.xcor()<-300:
		y2=random.randint(230,600)
		pole21.sety(y2)
		pole22.sety(y2-740)
		pole21.setx(300)
		pole22.setx(300)
		f2=True
	#pole boundary	
	
	if pole11.xcor()<53 and pole11.xcor()>-53:
		if bird.ycor()>(pole11.ycor()-315) or bird.ycor()<(pole12.ycor()+315):
			q=5
			flag=1
			bird.t=0
			u=0
			winsound.PlaySound("fhit.wav",winsound.SND_ASYNC)

	if pole21.xcor()<53 and pole21.xcor()>-53:
		if bird.ycor()>(pole21.ycor()-315) or bird.ycor()<(pole22.ycor()+315):
			q=5
			flag=1
			bird.t=0
			u=0
			winsound.PlaySound("fhit.wav",winsound.SND_ASYNC)

	if f1:
		if pole11.xcor()<-53:
			f1=False
			bird.score+=1

	if f2:
		if pole21.xcor()<-53:
			f2=False
			bird.score+=1
	if flag:
		if bird.ycor()==-190:
			status=False
			winsound.PlaySound("fg.wav",winsound.SND_ASYNC)


#score		
	pen.clear()
	pen.write("{}".format(bird.score), align="center", font=("Courier", 24, "normal"))
jacob=open("score.txt",'w')
jacob.write(str(bird.score))

pen.setx(0)
pen.sety(0)
pen.clear()
pen.write(" SCORE : {}".format(bird.score), align="center", font=("Courier", 24, "normal"))

time.sleep(3)		