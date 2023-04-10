import telebot, wikipedia, re

bot = telebot.TeleBot('bot token')
wikipedia.set_lang("en")


def get_wiki(s):
    '''
    the function that receives information from the site and displays
    text up to 1000 characters without paragraphs and some characters.
    returns string
    '''
    try:
        page = wikipedia.page(s)
        text = page.content[:1000]
        wiki_arr = text.split('.')
        wiki_arr = wiki_arr[:-1]
        final_text = ''
        for x in wiki_arr:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    final_text = final_text + x + '.'
            else:
                break
        final_text = re.sub('\{[^\{\}]*\}', '', final_text)
        final_text = final_text + '\n\nMore: ' + page.url
        return final_text
    except Exception as e:
        return 'The encyclopedia has no information about it.'


@bot.message_handler(commands=["start"])
def start(m, res=False):
    '''
    The function that handles the '/start' command.
    '''
    bot.send_message(m.chat.id, 'Send me any word and I will look it up on Wikipedia')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    '''
    The function that handles the receiving messages from a user.
    '''
    bot.send_message(message.chat.id, get_wiki(message.text))


bot.polling(none_stop=True, interval=0)
