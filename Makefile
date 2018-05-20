runserver:
	FLASK_ENV=development \
	FLASK_APP=webapp.app \
	flask run

start_redis:
	docker run -p 16379:6379 redis:3-alpine

start_worker:
	@rq worker

show_info:
	@rq info

watch_info:
	@rq info --interval 5
