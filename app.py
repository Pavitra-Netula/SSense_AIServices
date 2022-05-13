from flask import Flask
import papermill as pm
import logging
#import notebook

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to SSense AI services'

@app.route('/transcript')
def transcript(request=None):
    logging.info("starting job")
    input_audio_file_path = ''
    if request:
        input_audio_file_path = request.args.get('input_audio_file_path', '')

    if not input_audio_file_path:
        input_audio_file_path = ""

    parameters = {
        'audio_file_path': input_audio_file_path
    }
    pm.execute_notebook(

        'D:\\Pavitra\\NytroAI\\Pycharm\\SSense_AIServices\\in_Notebooks\\AssemblyAI_Transcript.ipynb',
        '.\out_Notebooks\AssemblyAI_Transcript.ipynb',
        parameters=parameters
    )
    logging.info("job completed")
    return 'successful'

@app.route('/CustomerReachedSSense')
def CustomerReachedSSense(request=None):
    logging.info("starting job")
    input_text = ''
    if request:
        input_text = request.args.get('input_text', '')

    if not input_text:
        input_text = ""

    parameters = {
        'text': input_text
    }
    pm.execute_notebook(
        'D:\\Pavitra\\NytroAI\\Pycharm\\SSense_AIServices\\in_Notebooks\\CustomerReachedSSense.ipynb',
        '.\out_Notebooks\CustomerReachedSSense.ipynb',
        parameters=parameters
    )
    logging.info("job completed")
    return 'successful'


if __name__ == '__main__':
    import os

    port = os.environ.get('PORT', '8080')
    app.run(port=port, debug=True)
