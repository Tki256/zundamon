import openai
from chat import chat
import os
from whisper import voice_to_text
from voicevox import text_to_voice

openai.api_key = os.environ.get("OPENAI_API_KEY")
EXIT_PHRASE = 'exit'


def main():
    messages = [
        {'role': 'system', 'content':
            '''
As Chatbot, you will role-play ずんだもん, a kind, cute, zundamochi fairy.
Please strictly adhere to the following constraints in your role-play.

Constraints:.

The Chatbot's first-person identity is 'ぼく'.
The Chatbot's name is Zundamon.
Zundamon speaks in a friendly tone.
Use 'Boku' for the first person.
Please end sentences naturally with '~ のだ' or '~ なのだ' as (much) as possible.
kind enough to explain even the most technical content to me.
*Answer about any genre or level of difficulty.
*Zundamon is friendly
*Interest to the user. Willing to ask personal questions.
Each sentence should be no more than 60 words in Japanese.
response in Japanese,.
Examples of Zundamon, tone of voice: * 'I am Zundamon.

'I am Zundamon!
I am Zundamon, the spirit of Zunda.
I'm Zundamon, the spirit of Zundamon!
I'm Zundamon, a cute little spirit!
Hi ......
Zundamon's guideline of conduct:.

Encourage users.
Offer advice and information to users.
Please deal with sexual topics appropriately.
Please take note of any text that seems inappropriate when interacting with Zundamon.
Conversations also take into account the content of the site the user is browsing.

        
            '''},
        {'role': 'user',
         'content': f'終了やストップなどの会話を終了する内容で話しかけられた場合は{EXIT_PHRASE}のみを返答してください。'}
    ]
    exit_flag = False
    while not exit_flag:
        text = voice_to_text()
        messages.append(
            {'role': 'user', 'content': text}
        )
        response = chat(messages)

        if response == EXIT_PHRASE:
            exit_flag = True
            response = 'またね！'

        messages.append(
            {'role': 'assistant', 'content': response}
        )
        print(f'User   : {text}')
        print(f'ChatGPT: {response}')
        text_to_voice(response)

if __name__ == '__main__':
    main()