# 2fa-ansible-google
Google Authenticator with Ansible


Для запуска playbook:

      `ansible-palybook <b>playbook-name</b>`


1) Создание пользователя или нескольких пользователей
В переменных, находящихся в папке vars - необходимо указать пользователей users:  или user: и внести правки в переменную в task"e user/uesr
  
      `ansible-playbook user-create.yml`
      
      
 2) Удаление пользователя или нескольких пользователей

В переменных, находящихся в папке vars - необходимо указать пользователей users:  или user: и внести правки в переменную в task"e user/uesr

      `ansible-playbook user-delete.yml`
 
 
 3) Изменение пользователя или нескольких пользователей


       `ansible-playbook user-change.yml`
       
       
       
 4) Добавление пользователя в группу

 
      `ansible-playbook user-add-to-group.yml`



 5) Изменение пользователя или нескольких пользователей


       `ansible-playbook user-change.yml`
