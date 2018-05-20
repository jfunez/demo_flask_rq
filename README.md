# python-rq: uma alternativa ao Celery

Palestra apresentada por mim no meetup do GruPy-SP no dia 19/05/18 na Faculdade Impacta (São Paulo)

Link para as slides: https://docs.google.com/presentation/d/1E9g79yPgxzRD-ZngCr8-JZdTvfxMNl2b2ImxnPvmv30/edit?usp=sharing

# Instruções:

1. Clonar este repositório: `git clone git@github.com:jfunez/demo_flask_rq.git`
2. Instalar um virtualenv com python 3.6 ou superior (`python -m venv venv` onde python é versão 3.6 ou superior);
3. Certifiquese que o venv esta ativado (`source venv/bin/activate`);
4. Instalar as dependencias dentro do virtualenv: `pip install -r requirements.txt`;
5. Numa aba de terminal iniciar o container do Redis: `make start_redis` (deve aparecer o output do redis server na tela);
6. Em outra aba de terminal iniciar a app flask: `make run_server` para iniciar o servidor flask;
7. Em outra aba de terminal iniciar o processo worker: `make start_worker` (pode iniciar tantos workers como desejar).
8. Pronto! pode ver as rotas no `app.py` para enfilerar tareas e para ver os resultados.
