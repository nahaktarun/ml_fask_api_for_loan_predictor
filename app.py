
import pickle
from flask import Flask, request


app =  Flask(__name__)


model_pickle = open('./artifacts/classifier.pkl','rb')

clf = pickle.load(model_pickle)

@app.route("/ping",methods=['GET'])
def ping():
    return {"message" : "Hi there I'm working"}

@app.route("/",methods=['GET'])
def mainPage():
    return {"message" : "Welcome to Flask Home"}


# Define the endpoint which will make prediction

@app.route('/predict',methods=['POST'])
def prediction():
    """
    Returns loan application status using ML model
    """
    loan_req = request.get_json()
    print(loan_req)

    if loan_req['Gender'] =="Male":
        Gender = 0
    else:
        Gender = 1
    
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
    
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1
    
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']


    result = clf.predict([[Gender,Married,ApplicantIncome,LoanAmount,Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"
    
    return {"loan_approval_status" : pred}

