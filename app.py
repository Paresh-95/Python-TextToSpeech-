from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from gtts import gTTS
from googletrans import Translator
import os
import threading
import webview
import time

app = Flask(__name__, template_folder='templates', static_folder='static')

def get_google_voices():
    languages = [
        {'lang': 'en', 'name': 'English'},
        {'lang': 'mr', 'name': 'Marathi'},
        {'lang': 'hi', 'name': 'Hindi'}
    ]
    return languages

def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

def speak(text, lang, audio_file):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(audio_file)

@app.route('/')
def index():
    return render_template('index.html', audio_file='', voices=get_google_voices(), os=os, time=time)

@app.route('/speak', methods=['POST'])
def speak_route():
    text = request.form.get('text')
    lang = request.form.get('lang')

    timestamp = str(int(time.time()))
    audio_file = os.path.join(app.root_path, f'static/output_{timestamp}.mp3')

    try:
        for filename in os.listdir(os.path.join(app.root_path, 'static')):
            if filename.startswith('output_') and filename.endswith('.mp3'):
                os.remove(os.path.join(app.root_path, 'static', filename))

        if lang == 'mr':
            text = translate_text(text, 'mr')

        speak(text, lang, audio_file)
        translation = text if lang == 'mr' else ""
    except Exception as e:
        print(f"Error in speak_route: {e}")
        translation = ""

    return render_template('index.html', audio_file=os.path.basename(audio_file), voices=get_google_voices(), os=os, time=time, lang=lang, translation=translation)

@app.route('/download/<filename>')
def download(filename):
    try:
        return send_from_directory('static', filename, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404

@app.route('/reload', methods=['POST'])
def reload():
    return redirect(url_for('index'))

def run_flask():
    app.run(port=5000, use_reloader=False, debug=True)

def create_gui():
    
    options = {
        "resizable": False,
        "fullscreen": False,
    }
    webview.create_window("TextToSpeech", "http://127.0.0.1:5000/", **options)
   


if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    time.sleep(2)

    create_gui()
    webview.start()
