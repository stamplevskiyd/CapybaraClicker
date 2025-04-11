## Стамплевский Дмитрий, 621 группа
### Практическая работа "Использование Kubernetes"
### Описание проекта
Веб-приложение capybara-clicker с использованием flask и mysql. 
Если уточнять -- еще sqlalchemy, flask-login, flask-sqlalchemy.

Простейшая внутренняя логика, поэтому и выбрал эту идею для задания: 
чтобы не застрять на сложной логике приложения там, где это не требуется.

### Запуск
1. Собрать docker image для приложения и "показать" его minikube:
```shell
docker build . -t capybara-clicker:latest
minikube image load capybara-clicker:latest
```
2. Запустить minikube (minikube start)
3. Запуск подов:
```shell
kubectl apply -f db-deployment.yaml
kubectl apply -f clicker-deployment.yaml
```

Остальные инструкции не обязательны, оставил их для себя.
3. Если нужно проверить, что они запущены:
```shell
kubectl get pods
```
4. Чтобы перейти на веб-страницу приложения, можно запустить команду:
```shell
minikube service clicker-service
```

Полезные команды:
```shell
kubectl exec -it <pod name, get in kubectl get pods> -- /bin/bash
```

```shell
eval $(minikube docker-env)
```