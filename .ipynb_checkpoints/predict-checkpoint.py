from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

kernal_evals = dict()
def evaluate_classification(model, name, X_train, X_test, y_train, y_test):
    train_accuracy = metrics.accuracy_score(y_train, model.predict(X_train))
    test_accuracy = metrics.accuracy_score(y_test, model.predict(X_test))
    
    train_precision = metrics.precision_score(y_train, model.predict(X_train))
    test_precision = metrics.precision_score(y_test, model.predict(X_test))
    
    train_recall = metrics.recall_score(y_train, model.predict(X_train))
    test_recall = metrics.recall_score(y_test, model.predict(X_test))
    
    kernal_evals[str(name)] = [train_accuracy, test_accuracy, train_precision, test_precision, train_recall, test_recall]
    print("Training Accuracy " + str(name) + " {}  Test Accuracy ".format(train_accuracy*100) + str(name) + " {}".format(test_accuracy*100))
    print("Training Precesion " + str(name) + " {}  Test Precesion ".format(train_precision*100) + str(name) + " {}".format(test_precision*100))
    print("Training Recall " + str(name) + " {}  Test Recall ".format(train_recall*100) + str(name) + " {}".format(test_recall*100))

    actual = y_test
    predicted = model.predict(X_test)
    confusion_matrix = metrics.confusion_matrix(actual, predicted)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['normal', 'attack'])

    fig, ax = plt.subplots(figsize=(10,10))
    ax.grid(False)
    cm_display.plot(ax=ax)
    
    # Tạo DataFrame
    df = pd.DataFrame({"Y_test": y_test['label'].values, "Y_pred": model.predict(X_test)})
    
    # Vẽ biểu đồ
    plt.figure(figsize=(16, 8))
    plt.plot(df['Y_test'][:20], label='Actual')  # Vẽ Y_test
    plt.plot(df['Y_pred'][:20], label='Predicted')  # Vẽ Y_pred
    plt.xticks(ticks=range(0, 20), labels=range(0, 20), rotation=0)  # Hiển thị tất cả các chỉ số mẫu
    plt.xlim(0, 19)
    plt.legend()
    plt.title('Actual vs Predicted')
    plt.xlabel('Sample Index')
    plt.ylabel('Value')
    plt.show()