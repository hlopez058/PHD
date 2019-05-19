from numpy import *

def compute_error_for_given_points(b,m,points):
    totalError=0
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        totalError += (y - (m*x+b))**2
    return totalError / float(len(points))


def step_gradient(b_current,m_current,points,learning_rate):
    #gradient descent
    b_gradient = 0
    m_gradient = 0
    #partial derivative of the values will give the gradient
    # the gradient will provide a positive or negative or a 0,
    # once it is at 0 then its at its minimum
    N = float(len(points))
    for i in range(0,len(points)) :
        x = points[i,0]
        y = points[i,1]
        b_gradient += -(2/N) * (y - (m_current*x+b_current))
        m_gradient += -(2/N) * x * (y - (m_current*x+b_current))

    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return (new_b,new_m)





def gradient_descent_runner(points,starting_b,starting_m,learning_rate,num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b,m,array(points),learning_rate)
    return [b,m]

def run():
    points=genfromtxt('PHD/EEL 6935 Smart Grid/linear regression/data.csv',delimiter=',')
    #hyperparameters
    learning_rate=0.001;
    #y = mx+b (slope formula)
    initial_b=0
    initial_m=0
    num_iterations = 10
    [b,m] = gradient_descent_runner(points,initial_b,initial_m,learning_rate,num_iterations)
    print(b)
    print(m)

if __name__ == '__main__':
    run()