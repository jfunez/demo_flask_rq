from flask import Flask, url_for
from rq import Queue
from redis import Redis
from .jobs import count_words_at_url

import rq_dashboard

# inicializamos app flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

# configurações padrão do rq-dashboard
app.config.from_object(rq_dashboard.default_settings)
# plugamos a interface na rota: /dashboard
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/dashboard")

# definição de conexão com Redis e da Queue (por padrão: 'default')
redis_conn = Redis()
r_queue = Queue(connection=redis_conn)


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/scraper/simple/<string:url>")
def scraper_simple(url):
    result = count_words_at_url(url)
    return f"<h1>URL tem tamanho: {result}</h1>"


@app.route("/scraper/task/<string:url>")
def scraper_task(url):
    # enfileiro a task
    job = r_queue.enqueue(count_words_at_url, url)
    # gero a url para facilitar a consulta do resultado
    job_result_url = url_for('.scraper_result', job_id=job.id)

    return f"<h1>Job enfilerado</h1> <h2>(id: <a href='{job_result_url}'>{job.id}</a>)</h2>"


@app.route("/scraper/task/result/<string:job_id>")
def scraper_result(job_id):
    job = r_queue.fetch_job(job_id)
    return f"<h1>{job.result}</h1><h2>Job id:{job_id}</h2>"
