## Стамплевский Дмитрий, 621 группа
### Практическая работа "Использование Kubernetes"
### Описание проекта
Веб-приложение capybara-clicker с использованием flask и mysql. 
Если уточнять -- еще sqlalchemy, flask-login, flask-sqlalchemy.

Простейшая внутренняя логика, поэтому и выбрал эту идею для задания: 
чтобы не застрять на сложной логике приложения там, где это не требуется.

### Запуск
Пару лишних моментов расписал для себя, так как раньше работал с Docker, но не с Kubernetes
0. Собрать docker image для приложения и "показать" его minikube:
```shell
eval $(minikube docker-env)
docker build . -t capybara-clicker:latest
minikube image load capybara-clicker:latest
```
1. Запустить minikube (minikube start)
2. Запуск подов:
```shell
kubectl apply -f db-deployment.yaml
kubectl apply -f clicker-deployment.yaml
```
3. Если нужно проверить, что они запущены:
```shell
kubectl get pods
```
4. Чтобы перейти на веб-страницу приложения, можно запустить команду:
```shell
minikube service clicker-service
```

Зайти в pod:
```shell
kubectl exec -it <pod name, get in kubectl get pods> -- /bin/bash
```