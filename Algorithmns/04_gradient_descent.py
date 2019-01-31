
x = [1, 2, 3]
y = [1, 2, 3]

m = len(y)

theta0 = 1
theta1 = 1.5
alpha = 0.01

def cost_function(theta0,theta1):
	predicted_y = [theta0+(theta1*1), theta0+(theta1*2), theta0+(theta1*3)]
	sum=0
	for i,j in zip(predicted_y,y):
		sum = sum+((i-j)**2) 
	J = 1/(2*m)*sum 
	return (J)

def gradientDescent(x, y, theta1, alpha):
	J_history = []
	for i in range(50):
		for i,j in zip(x,y):
			delta=1/m*(i*i*theta1-i*j);
			theta1=theta1-alpha*delta;
			J_history.append(cost_function(theta0,theta1))
	print (min(J_history))
	

gradientDescent(x, y, theta1, alpha)





"""	

def gradientDescent(X, y, theta1, alpha):
	m = length(y)
	J_history = []
	for i in range(1500):
		delta=1/m*(X'*X*theta-X'*y);
		theta1=theta1-alpha.*delta;
		
def nithya():
	return (10)
J_history = []
J_history.append(nithya())
print (J_history)

function [theta, J_history] = gradientDescent(X, y, theta1, alpha)
m = length(y); 
J_history = []    
for i = 1:1500
    delta=1/m*(X'*X*theta-X'*y);
    theta=theta-alpha.*delta;
    J_history(i) = computeCost(X, y, theta);
end
end
"""