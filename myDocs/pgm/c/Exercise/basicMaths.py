print "Basic Maths"
num1=input("Enter num1")
num2=input("Enter num2")
print "1.addition\n2.subtraction\n3.multiplication\n4.division\n5.modulus"
choice=input("Enter your input")
switch choice
	case 1:
		print "addition=",num1+num2
		break
	case 2:
		print "subtraction=",num1-num2
		break
	case 3:
		print "multiplication=",num1*num2
		break
	case 4:
		print "division=",num1/num2
		break
	case 5:
		print "modulus=",num1%num2
		break
	default:
		print "No operation"
		break
