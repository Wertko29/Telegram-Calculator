import telebot
from telebot import types

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

print("Bot Started. Made by Wertko29. Press Ctrl+C to stop process.")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I'm a calculator in Telegram. Just send me a math expression like: 5+3 or 2*4")

def start_calc(message):  # Fixed parameter name from 'massage' to 'message'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('+', '-', 'x', ':')  # Note: 'x' for multiplication and ':' for division

@bot.message_handler(func=lambda m: True)
def calculator(message):  # Changed function name to lowercase (style convention)
    try:
        text = message.text.replace(" ", "")
        
        # Find which operation is being used
        operation = None
        for op in ['+', '-', 'x', ':']:
            if op in text:
                operation = op
                break
                
        if not operation:
            raise ValueError("No valid operation found. Use +, -, x, or :")
        
        # Split the numbers
        a, b = text.split(operation)
        a = float(a)
        b = float(b)
        
        # Perform calculation
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == 'x':
            result = a * b
        elif operation == ':':
            if b == 0:
                raise ValueError("Division by zero!")
            result = a / b
        
        # Format result nicely
        if result.is_integer():
            result = int(result)
            
        bot.send_message(message.chat.id, f"Result: {result}")
        
    except ValueError as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")
    except Exception as e:
        bot.send_message(message.chat.id, "Something went wrong. Please try again.")

bot.polling(none_stop=True)