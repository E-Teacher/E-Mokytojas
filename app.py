from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code'].upper()
        return redirect(url_for('lesson_page', code=code, page=1))
    return '''
        <h1>e-mokytojas</h1>
        <form method="post">
            <input name="code" maxlength="4" placeholder="Pvz: ABCD">
            <button type="submit">Pradėti</button>
        </form>
    '''

@app.route('/lesson/<code>/<int:page>')
def lesson_page(code, page):
    path = os.path.join('LessonFiles', code, f'{page}.html')
    if not os.path.isfile(path):
        return f'<h2>Puslapis nerastas ({code}/{page})</h2><a href="/">Grįžti</a>', 404
    
    next_page_path = os.path.join('LessonFiles', code, f'{page + 1}.html')
    has_next = os.path.isfile(next_page_path)
    
    with open(path, encoding='utf-8') as f:
        html = f.read()
    return render_template('lesson.html', code=code, page=page, content=html, has_next=has_next)


@app.route('/health')
def health_check():
    return "OK"
