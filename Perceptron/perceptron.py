X = []
y = []

with open("data.txt", "r") as file:
    for line in file:
        values = list(map(float, line.split()))
        X.append(values[:-1])  # Features
        y.append(values[-1])   # Label

weights = [0.0] * len(X[0])
bias = 0.0
learning_rate = 0.1
epochs = 100

def predict(features, weights, bias):
    total = bias
    for i in range(len(features)):
        total += features[i] * weights[i]
    return 1 if total >= 0 else 0

def train(X, y, weights, bias, learning_rate):
    for epoch in range(epochs):
        for i in range(len(X)):
            prediction = predict(X[i], weights, bias)
            error = y[i] - prediction
            bias += learning_rate * error
            for j in range(len(weights)):
                weights[j] += learning_rate * error * X[i][j]
        if epoch % 10 == 0:
            total_error = sum([abs(y[i] - predict(X[i], weights, bias)) for i in range(len(X))])
            print(f"Epoch {epoch}, Error: {total_error}")

train(X, y, weights, bias, learning_rate)

print(f"\nWeights: {weights}")
print(f"Bias: {bias}")

test = [2.0, 1.0]
result = predict(test, weights, bias)
print(f"Prediction for {test}: {result}")