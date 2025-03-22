X = []
y = []

with open("data.txt", "r") as file:
    for line in file:
        height, weight = map(float, line.split())
        X.append(height)
        y.append(weight)

slope = 0.0
intercept = 0.0
learning_rate = 0.0000001
epochs = 1000

def predict(x, m, b):
    return m * x + b

def compute_error(X, y, m, b):
    total_error = 0
    n = len(X)
    for i in range(n):
        y_pred = predict(X[i], m, b)
        diff = y[i] - y_pred
        total_error += diff * diff  # Avoid direct squaring to reduce overflow risk
    return total_error / n

def gradient_descent(X, y, m, b, learning_rate):
    m_gradient = 0
    b_gradient = 0
    n = len(X)
    for i in range(n):
        x = X[i]
        y_true = y[i]
        y_pred = predict(x, m, b)
        m_gradient += (-2/n) * x * (y_true - y_pred)
        b_gradient += (-2/n) * (y_true - y_pred)
    new_m = m - learning_rate * m_gradient
    new_b = b - learning_rate * b_gradient
    return new_m, new_b

print("Training started...")
for epoch in range(epochs):
    slope, intercept = gradient_descent(X, y, slope, intercept, learning_rate)
    error = compute_error(X, y, slope, intercept)
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Error: {error}")

print(f"\nModel: y = {slope:.4f} * x + {intercept:.4f}")

height = 168
weight_pred = predict(height, slope, intercept)
print(f"Predicted weight for height {height}cm: {weight_pred:.2f}kg")