from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('new.html')


@app.route("/download", methods=['GET', 'POST'])
def test():
    data = {'unit': str(request.form.get('comp_select')), 'word': request.form.get('word'),
            'speaking_word': request.form.get('speaking_word'),
            'translated_text_1': request.form.get('translated_text_1'),
            'example_sentence_1': request.form.get('example_sentence_1'),
            'translated_text_2': request.form.get('translated_text_2'),
            'example_sentence_2': request.form.get('example_sentence_2')}

    from static.main import convertor

    return render_template('download.html', data=data), convertor(data['word'], data['unit'], data['word'],
                                                                  data['speaking_word'], data['translated_text_1'],
                                                                  data['example_sentence_1'], data['translated_text_2'],
                                                                  data['example_sentence_2'])


if __name__ == '__main__':
    app.run(debug=True)
