import base64

def img_to_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


user_avatar = img_to_base64("user.png")   
bot_avatar = img_to_base64("bot.png")

css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
}
.chat-message.user {
    background-color: #2b313e;
}
.chat-message.bot {
    background-color: #475063;
}
.chat-message .avatar {
    width: 15%;
    display: flex;
    flex-direction: column;
    align-items: center;   
}
.chat-message .avatar img {
    max-width: 70px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 85%;
    padding: 0 1.5rem;
    color: #fff;
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="data:image/png;base64,{bot_avatar}">
        <div class="label">Bot</div>
    </div>
    <div class="message">
        {{$MSG}}
    </div>
</div>
'''.replace("{bot_avatar}", bot_avatar)

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,{user_avatar}">
        <div class="label">You</div>
    </div>
    <div class="message">
        {{$MSG}}
    </div>
</div>
'''.replace("{user_avatar}", user_avatar)
