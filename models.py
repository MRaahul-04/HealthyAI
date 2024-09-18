# models.py

from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    conversations = db.relationship('Conversation', backref='user', lazy=True)
    appointments = db.relationship('Appointment', backref='user', lazy=True)

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    reason = db.Column(db.Text, nullable=False)

def store_conversation(user_id, message, response):
    new_conversation = Conversation(user_id=user_id, message=message, response=response)
    db.session.add(new_conversation)
    db.session.commit()

def book_appointment_in_db(data):
    new_appointment = Appointment(
        user_id=data['user_id'],
        name=data['name'],
        date=data['date'],
        time=data['time'],
        reason=data['reason']
    )
    db.session.add(new_appointment)
    db.session.commit()


# def process_message(message):
#     # Load pre-trained model and tokenizer
#     model_name = "distilbert-base-uncased-finetuned-sst-2-english"
#     model = AutoModelForSequenceClassification.from_pretrained(model_name)
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#
#     # Preprocess the input message
#     inputs = tokenizer.encode_plus(
#         message,
#         add_special_tokens=True,
#         max_length=512,
#         return_attention_mask=True,
#         return_tensors='pt'
#     )
#
#     # Get the sentiment analysis output
#     output = model(inputs['input_ids'], attention_mask=inputs['attention_mask'])
#     sentiment_scores = torch.nn.functional.softmax(output.logits, dim=1)
#
#     # Determine the response based on the sentiment score
#     sentiment_label = torch.argmax(sentiment_scores)
#     if sentiment_label == 0:  # Negative sentiment
#         response = "Sorry to hear that. How can I assist you today?"
#     elif sentiment_label == 1:  # Positive sentiment
#         response = "That's great to hear! How can I help you today?"
#     else:  # Neutral sentiment
#         response = "How can I help you today?"
#
#     return response