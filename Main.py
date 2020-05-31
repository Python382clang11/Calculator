#coding:utf8
from random import randint
from time import sleep
import math 
def _exit():
  exit()
mode=1
print('Welcome to python calculator 3.4(Assert Edition)')
print("Enter'q' to quit.")
x=randint(1,1000)
"""This small 'Easter egg' is in devlopment"""
if x==1:
	print('You have just discovered something.')
	print("The chance of seeing this is 1/1000.")
	print("In python3, use level-three strings instead of '#'")
	print("This calculator will now go into mode 2.")
	mode=2
while mode==1:
	a=0
	b=0
	c=0
	d=0
	try:
		a=int(input ("Enter the first number:"))
	except ValueError:
		print("Invalid input.")
		break
	"""断言测试"""
	if a=='π':
		a=math.pi()
	if a=='q':
    _exit()
	b=input("Enter calculation, such as '+' and '**'.")
	assert b !='q','You have quit.'
	try:
		c=int(input ("Enter the second number:"))
	except ValueError:
		print("Invalid input.")
		break
	if c=='π':
		c=math.pi()
	assert c!='q','You have quit.'
	if b=='+':
		d=a+c
	elif b=='-':
		d=a-c
	elif b=='*':
		d=a*c
	elif b=='/':
		assert c!='0','You can not divide by 0!'
		d=a/c
	elif b=='//':
		assert c!='0','You can not divide by 0!'
		d=a//c
	elif b=='**' or b=='^':
		d=a**c
	elif b=='√':
		if c==0:
			assert a=='0','Calculation invalid.'
			d=1
		else:
			d=pow(a,1/c)
	else:
		print("Invalid input or in devlopment.")
		break
	print("The answer is:"+str(d))
"""The crazy mode is still in devlopment!
Also:This mode is just a joke."""
while mode==2:
	print("This is just a jokE¿¡")
	a=0
	b=0
	c=0
	d=0
	try:
		a=int(input ("Enter tHe lAst numBer:"))
	except ValueError:
		print("Valid inPut.")
		break
	if a=='π':
		a=math.pi()
	assert a !='q','You haVe NoT Quit.'
	b=input("Enter caLcuLatiOn, sucH as '+' aNd '**'.")
	assert b !='q','You hAve nOT Quit.'
	try:
		c=int(input ("ENter the seconD-LaSt number:"))
	except ValueError:
		print("ValiD input.")
		break
	if c=='π':
		c=math.pi()
	assert c!='q','You Donot Quit.'
	if b=='+':
		d=a**c
	elif b=='-':
		d=a*c
	elif b=='*':
		d=a+c
	elif b=='/':
		assert c!='0','You can divide by 123816273318723!'
		d=a/c
	elif b=='//':
		assert c!='0','You can#include<iostream> divide by 85769485798!'
		d=a//c
	elif b=='**' or b=='^':
		d=a-c
	elif b=='√':
		if c==0:
			assert a=='0','CalcuLation valid.'
			d=1
		else:
			d=pow(a,1/c)
	else:
		print("Valid inPut or nOy in devLopmenT.")
		break
	print("The aNsVVer is noT:"+str(d))
