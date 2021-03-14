create-ssl-certificate: 
	openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx/certs/key.pem -out nginx/certs/cert.pem

create-nginx-account:
	# reference here: https://github.com/PhungXuanAnh/tech-note/blob/master/devops/nginx/nginx-configuration-snippets.md#enable-basic-authentication
	sudo apt-get install apache2-utils -y
	htpasswd nginx/htpasswd admin

run:
	reset && .venv/bin/python manage.py runserver 127.0.0.1:8091

# ============================== sqlite =================================
rm-old-data:
	rm -rf db.sqlite3

migrate:
	.venv/bin/python manage.py migrate

makemigrations:
	.venv/bin/python manage.py makemigrations

create-supperuser:
	.venv/bin/python manage.py shell -c "from django.contrib.auth.models import User; \
							User.objects.filter(username='admin').exists() or \
							User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

create-sample-data: rm-old-data migrate makemigrations create-supperuser
	.venv/bin/python create_sample_data.py

# ============================== postgres - docker =================================
docker-rm-old-data:
	docker-compose down
	docker volume rm genetica-test_postgres_data
	docker-compose up -d
	sleep 3

docker-migrate:
	docker exec genetica-test_my-backend_1 python3 manage.py migrate

docker-makemigrations:
	docker exec genetica-test_my-backend_1 python3 manage.py makemigrations

docker-create-supperuser:
	docker exec genetica-test_my-backend_1 python3 manage.py shell -c "from django.contrib.auth.models import User; \
								User.objects.filter(username='admin').exists() or \
								User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

docker-create-sample-data: docker-rm-old-data docker-makemigrations docker-migrate docker-create-supperuser
	docker exec genetica-test_my-backend_1 python3 create_sample_data.py

# ========================================= viewset ===============================================

musican-viewset-create:
	curl -X POST "http://127.0.0.1:8091/api/v1/musican-viewset" \
		-u admin:admin \
		-H "accept: application/json" \
		-H "Content-Type: application/json" \
		-H "X-CSRFToken: kCWi9tLrdnfvPUmQvLx1cp5EAN0ZXN7iJaUisNhdLpj4tB6A5UXoFYdXC23Rs8jU" \
		-d "{ \"first_name\": \"first_name 1\", \"last_name\": \"first_name 1\", \"instrument\": \"piano\"}" \
		| jq

musican-viewset-list:
	curl "http://127.0.0.1:8091/api/v1/musican-viewset" \
		-u admin:admin \
		-H "accept: application/json" \
		| jq

musican-viewset-get:
	curl "http://127.0.0.1:8091/api/v1/musican-viewset/10" \
		-u admin:admin \
		-H "accept: application/json" \
		| jq

musican-viewset-put:
	curl -X PUT "http://127.0.0.1:8091/api/v1/musican-viewset/1" \
		-u admin:admin \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 11\", \"last_name\": \"first_name 11\", \"instrument\": \"gita\"}" \
		| jq

musican-viewset-patch:
	curl -X PATCH "http://127.0.0.1:8091/api/v1/musican-viewset/2" \
		-u admin:admin \
		-H "Content-Type: application/json" \
		-d "{ \"first_name\": \"first_name 123\", \"last_name\": \"first_name 321\"}" \
		| jq

musican-viewset-delete:
	curl -X DELETE "http://127.0.0.1:8091/api/v1/musican-viewset/1" \
		-u admin:admin | jq

musican-viewset-sample-action:
	curl "http://127.0.0.1:8091/api/v1/musican-viewset/2/sample-action" \
		-u admin:admin | jq

## ======================================== production ================================
prod-up:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

prod-ps:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml ps

prod-down:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml down
