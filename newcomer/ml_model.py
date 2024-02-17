import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from transformers import GPT2LMHeadModel, GPT2Tokenizer
# Load the pre-trained GPT-2 model and tokenizer
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Load the dataset
def train_model():
        
    data = pd.read_csv('path/to/dataset.csv')

    # Split the data into features and target variable
    X = data.drop('target', axis=1)
    y = data['target']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    score = model.score(X_test, y_test)
    print(f"Model score: {score}")


#get suggestion from some huggingface models
def get_suggestion(prompt):
    # Tokenize the input text
    tokenizer.pad_token = tokenizer.eos_token
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    # Generate response using the GPT-2 model
    output = model.generate(input_ids, max_length=100, num_return_sequences=1,top_k=50, top_p=0.95, temperature=0.7,do_sample=True)
    
    return tokenizer.decode(output[0], skip_special_tokens=True)
